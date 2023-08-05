import json
from typing import List, Optional

from databricks.feature_store.entities._feature_store_object import _FeatureStoreObject
from databricks.feature_store.utils.rest_utils import http_request, verify_rest_response


class FunctionParameterInfo(_FeatureStoreObject):
    def __init__(self, name: str, type_name: str):
        self._name = name
        self._type_name = type_name

    @property
    def name(self) -> str:
        return self._name

    @property
    def type_name(self) -> str:
        return self._type_name

    @classmethod
    def from_dict(cls, function_parameter_info_json):
        return FunctionParameterInfo(
            function_parameter_info_json["name"],
            function_parameter_info_json["type_name"],
        )


class FunctionInfo(_FeatureStoreObject):
    """
    Helper entity class that exposes properties in GetFunction's response JSON as attributes.
    https://docs.databricks.com/api-explorer/workspace/functions/get

    Note: empty fields (e.g. when 0 input parameters) are not included in the response JSON.
    """

    # Python UDFs have external_language = "Python"
    PYTHON = "Python"

    def __init__(
        self,
        full_name: str,
        input_params: List[FunctionParameterInfo],
        routine_definition: str,
        external_language: Optional[str],
    ):
        self._full_name = full_name
        self._input_params = input_params
        self._routine_definition = routine_definition
        self._external_language = external_language

    @property
    def full_name(self) -> str:
        return self._full_name

    @property
    def input_params(self) -> List[FunctionParameterInfo]:
        return self._input_params

    @property
    def routine_definition(self) -> str:
        return self._routine_definition

    @property
    def external_language(self) -> Optional[str]:
        """
        Field is None if language is SQL (not an external language).
        """
        return self._external_language

    @classmethod
    def from_dict(cls, function_info_json):
        input_params = function_info_json.get("input_params", {}).get("parameters", [])
        return FunctionInfo(
            full_name=function_info_json["full_name"],
            input_params=[FunctionParameterInfo.from_dict(p) for p in input_params],
            routine_definition=function_info_json["routine_definition"],
            external_language=function_info_json.get("external_language", None),
        )


class UnityCatalogClient:
    """
    Internal client for making REST calls to Unity Catalog.

    Note: Sending requests to UC from Python requires a personal access token, as the default token is not UC scoped.
    To use this client, provide a `get_host_creds` that resolves a credentials object with host, token attributes.

    TODO (ML-29922): Replace this client with an alternative that does not require PATs.
    """

    def __init__(self, get_host_creds):
        self._get_host_creds = get_host_creds

    def get_function(self, name: str) -> FunctionInfo:
        """
        https://docs.databricks.com/api-explorer/workspace/functions/get
        """
        endpoint = f"/api/2.1/unity-catalog/functions/{name}"
        response = self._call_endpoint(endpoint=endpoint, method="GET")
        return FunctionInfo.from_dict(response)

    def _call_endpoint(self, endpoint: str, method: str):
        response = http_request(
            host_creds=self._get_host_creds(),
            endpoint=endpoint,
            method=method,
        )
        response = verify_rest_response(response, endpoint)
        return json.loads(response.text)
