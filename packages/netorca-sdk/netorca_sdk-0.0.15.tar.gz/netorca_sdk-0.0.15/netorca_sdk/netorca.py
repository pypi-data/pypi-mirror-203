import json
from typing import Union

from netorca_sdk.auth import AbstractNetorcaAuth
from netorca_sdk.config import (
    logger,
    API_VERSION,
    URL_PREFIX,
)
from netorca_sdk.exceptions import NetorcaException
from netorca_sdk.validations import ContextIn, InvalidContextError


class Netorca:
    def __init__(self, auth: AbstractNetorcaAuth):
        self.auth = auth

    def get_service_items(self, filters=None, context: ContextIn = None):
        """
        Fetches service items from the Netorca API based on the provided filters.

        :param context: POV for which the request is being made. Defaults to SERVICEOWNER.
        :param filters: Optional dictionary containing filters to apply to the API request.
                        Example format: {"service_name": "my_service"}
        :type filters: dict, optional

        :return: A list of service items matching the provided filters.
        :rtype: list

        :raises NetorcaException: If the API request fails or encounters an error.
        """
        logger.info(f"Fetching service items with filters: {filters}")

        url = self.create_url(endpoint="service_items", context=context)
        response = self.auth.get(url=url, authentication_required=True, filters=filters)
        if response.status_code == 200:
            return response.json()["results"]

        logger.error(f"Could not fetch Service Items due to: {response.json()}")
        raise NetorcaException(f"Could not fetch Service Items due to: {response.json()}")

    def get_deployed_items(self, filters=None, context: ContextIn = None):
        """
        Fetches deployed items from the Netorca API based on the provided filters.

        :param context: POV for which the request is being made. Defaults to SERVICEOWNER.
        :param filters: Optional dictionary containing filters to apply to the API request.
        :type filters: dict, optional

        :return: A list of deployed items matching the provided filters.
        :rtype: list

        :raises NetorcaException: If the API request fails or encounters an error.
        """
        logger.info(f"Fetching deployed items with filters: {filters}")

        url = self.create_url(endpoint="deployed_items", context=context)
        response = self.auth.get(url=url, authentication_required=True, filters=filters)
        if response.status_code == 200:
            return response.json()["results"]

        logger.error(f"Could not fetch Deployed Items due to: {response.json()}")
        raise NetorcaException(f"Could not fetch Deployed Items due to: {response.json()}")

    def get_change_instances(self, filters=None, context: ContextIn = None):
        """
        Fetches change instances from the Netorca API based on the provided filters.

        :param context: POV for which the request is being made. Defaults to SERVICEOWNER.
        :param filters: Optional dictionary containing filters to apply to the API request.
                        Example format: {"service_name": "my_service1,my_service2"}
        :type filters: dict, optional

        :return: A list of change instances matching the provided filters.
        :rtype: list

        :raises NetorcaException: If the API request fails or encounters an error.
        """
        logger.info(f"Fetching change instances with filters: {filters}")

        url = self.create_url(endpoint="change_instances", context=context)
        response = self.auth.get(url=url, authentication_required=True, filters=filters)
        if response.status_code == 200:
            return response.json()["results"]

        logger.error(f"Could not fetch Change Instances due to: {response.json()}")
        raise NetorcaException(f"Could not fetch Change Instances due to: {response.json()}")

    def create_deployed_item(self, change_instance_uuid: str, data: dict, context: ContextIn = None):
        """
        Creates a Deployed Item for a specified Change Instance in the Netorca API.

        :param context: POV for which the request is being made. Defaults to SERVICEOWNER.
        :param change_instance_uuid: UUID of the ChangeInstance to which the DeployedItem should be added.
        :type change_instance_uuid: str

        :param data: Dictionary containing the metadata of the DeployedItem to be created.
                     Example format: {"key": "value"}
        :type data: dict

        :return: A dictionary containing the updated ChangeInstance with the new DeployedItem.
        :rtype: dict

        :raises NetorcaException: If the API request fails or encounters an error.
        """
        logger.info(f"Creating deployed item for change_instance_uuid: {change_instance_uuid} with data: {data}")

        url = self.create_url(endpoint="change_instances", context=context, id=change_instance_uuid)
        data = {"deployed_item": data}
        response = self.auth.patch(url=url, data=json.dumps(data), authentication_required=True)
        if response.status_code == 200:
            return response.json()

        logger.error(f"Could not create deployed item. Log: {response.json()}")
        raise NetorcaException(f"Could not create deployed item. Log: {response.json()}")

    def update_change_instance(self, change_instance_uuid, data, context: ContextIn = None):
        """
        Update a Deployed Item for a specified Change Instance in the Netorca API.

        :param context: POV for which the request is being made. Defaults to SERVICEOWNER.
        :param change_instance_uuid: UUID of the ChangeInstance to which the DeployedItem should be added.
        :type change_instance_uuid: str

        :param data: Dictionary containing the metadata of the DeployedItem to be created.
                     Example format: {"key": "value"}
        :type data: dict

        :return: A dictionary containing the updated ChangeInstance with the new DeployedItem.
        :rtype: dict

        :raises NetorcaException: If the API request fails or encounters an error.
        """
        logger.info(f"Updating change instance with UUID: {change_instance_uuid} and data: {data}")

        url = self.create_url(endpoint="change_instances", context=context, id=change_instance_uuid)
        response = self.auth.patch(url=url, data=json.dumps(data), authentication_required=True)
        if response.status_code == 200:
            return response.json()

        logger.error(f"Could not update Change Instance. Log: {response.json()}")
        raise NetorcaException(f"Could not update change Instance. Log: {response.json()}")

    def get_service_config(self, config_uuid=None, filters=None, context: ContextIn = None):
        """
        Fetches service configuration(s) from the Netorca API based on the provided config_uuid or filters.

        :param context: POV for which the request is being made. Defaults to SERVICEOWNER.
        :param config_uuid: Optional UUID of the specific service configuration to fetch.
                            If provided, filters will be ignored.
        :type config_uuid: str, optional

        :param filters: Optional dictionary containing filters to apply to the API request.
                        Example format: {"config_name": "PR019_IIW_001_config"}
                        Ignored if config_uuid is provided.
        :type filters: dict, optional

        :return: A dictionary containing the service configuration(s) matching the provided config_uuid or filters.
                 If config_uuid is provided, a single configuration will be returned; otherwise, a list of configurations.
        :rtype: dict or list

        :raises NetorcaException: If the API request fails or encounters an error.
        """
        logger.info(f"Fetching service config with config_uuid: {config_uuid} and filters: {filters}")

        url = self.create_url(endpoint="change_instances", context=context, id=config_uuid)

        response = self.auth.get(url=url, authentication_required=True, filters=filters)
        if response.status_code == 200:
            return response.json()
        logger.error(f"Could not get service config. Log: {response.json()}")
        raise NetorcaException(f"Could not get service config. Log: {response.json()}")

    def get_dependant_service_items(self, filters=None, context: ContextIn = None):
        """
        Fetches dependent service items from the Netorca API based on the provided filters.
        :param context: POV for which the request is being made. Defaults to SERVICEOWNER.
        :param filters: Optional dictionary containing filters to apply to the API request.
                        Example format: {"service_name": "my_service"}
        :type filters: dict, optional

        :return: A list of service items matching the provided filters.
        :rtype: list

        :raises NetorcaException: If the API request fails or encounters an error.
        """
        logger.info(f"Fetching dependent service items with filters: {filters}")

        url = self.create_url(endpoint="service_items/dependant", context=context)
        response = self.auth.get(url=url, authentication_required=True, filters=filters)
        if response.status_code == 200:
            return response.json()["results"]

        logger.error(f"Could not fetch Service Items Dependent due to: {response.json()}")
        raise NetorcaException(f"Could not fetch Service Items Dependent due to: {response.json()}")

    def create_url(self, endpoint: str, context: ContextIn = ContextIn.SERVICEOWNER.value, id: Union[str, int] = None):
        id_str = f"{id.replace('/', '')}/" if id else ""
        try:
            context = ContextIn.SERVICEOWNER.value if context is None else context
            url = f"{self.auth.fqdn}{API_VERSION}{URL_PREFIX}/{context}/{endpoint}/{id_str}"
        except ValueError:
            raise InvalidContextError(
                f"{context} is not a valid ContextIn value. Options are {ContextIn.SERVICEOWNER.value} and {ContextIn.CONSUMER.value}"
            )
        return url
