from typing import Dict, List

from pyspark.sql import DataFrame
from pyspark.sql.functions import expr

from databricks.feature_store.entities.feature_spec import FeatureSpec
from databricks.feature_store.unity_catalog_client import FunctionInfo
from databricks.feature_store.utils import utils


def _udf_expr(udf_name: str, arguments: List[str]) -> expr:
    """
    Generate a Spark SQL expression, e.g. expr("udf_name(col1, col2)")
    """
    arguments_str = ", ".join(utils.sanitize_identifiers(arguments))
    return expr(f"{udf_name}({arguments_str})")


def _validate_apply_functions_df(
    feature_spec: FeatureSpec,
    df: DataFrame,
    uc_function_infos: Dict[str, FunctionInfo],
):
    """
    Validate the following:
    1. On-demand input columns specified by FeatureSpec.on_demand_column_infos exist in the DataFrame.
    2. On-demand input columns have data types that match those of UDF parameters.
    """
    for odci in feature_spec.on_demand_column_infos:
        function_info = uc_function_infos[odci.udf_name]

        for p in function_info.input_params:
            arg_column = odci.input_bindings[p.name]
            if arg_column not in df.columns:
                raise ValueError(
                    f"FeatureFunction argument column '{arg_column}' for UDF '{odci.udf_name}' parameter '{p.name}' "
                    f"does not exist in provided DataFrame with schema '{df.schema}'."
                )

            # TODO (ML-29944): Validate on-demand input binding dtypes match UDF parameters if necessary.
            #   Spark and UC data types have different names (e.g. INTEGER vs INT) and are not directly comparable.


def apply_functions_if_not_overridden(
    feature_spec: FeatureSpec,
    df: DataFrame,
    uc_function_infos: Dict[str, FunctionInfo],
) -> DataFrame:
    """
    For all on-demand features, in the order defined by the FeatureSpec:
    If the feature does not already exist, append the evaluated UDF expression.
    Existing column values or column positions are not modified.

    `_validate_apply_functions_df` validates UDFs can be applied on `df` schema.

    The caller should validate:
    1. FeatureFunction bound argument columns for UDF parameters exist in FeatureSpec defined features.
    2. FeatureFunction output feature names are unique.
    """
    _validate_apply_functions_df(
        feature_spec=feature_spec, df=df, uc_function_infos=uc_function_infos
    )

    columns = {}
    for odci in feature_spec.on_demand_column_infos:
        if odci.output_name not in df.columns:
            function_info = uc_function_infos[odci.udf_name]
            # Resolve the bound arguments in the UDF parameter order
            udf_arguments = [
                odci.input_bindings[p.name] for p in function_info.input_params
            ]
            columns[odci.output_name] = _udf_expr(odci.udf_name, udf_arguments)
    return df.withColumns(columns)
