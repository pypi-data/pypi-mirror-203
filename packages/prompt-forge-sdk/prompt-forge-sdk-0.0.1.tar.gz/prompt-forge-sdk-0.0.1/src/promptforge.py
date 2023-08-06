
import logging
import typing
from json import JSONDecodeError
from pydantic import ValidationError
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from models import PromptForgeAPIError, PromptForgeClientError, LatestPromptVersions, EnvironmentModel, EnvironmentRequestBody, LatestPromptVersions, PromptVersion
from polling_manager import EnvironmentDataPollingManager
from constants import HttpMethods, URLS, Keys, DefaultEnvironmentKeys

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class PromptForge:
    """A PromptForge client. Provides an interface to the PromptForge API."""    
    def __init__(
        self,
        org_api_key: str,
        application_env_string:typing.Union[DefaultEnvironmentKeys, str] = DefaultEnvironmentKeys.DEVELOPMENT,
        api_url: str = URLS.DEFAULT_API_URL,
        custom_headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_timeout_seconds: typing.Optional[int] = None,
        enable_local_evaluation: bool = False,
        environment_refresh_interval_seconds: typing.Union[int, float] = 60,
        retries: typing.Optional[Retry] = None,
    ):
        """_summary_

        :param environment_key: _description_
        :type environment_key: str
        application_env_string: The name of the application environment for which you want to fetch prompts, defaults to DefaultEnvironmentKeys.DEVELOPMENT
        :type application_env_string: typing.Union[DefaultEnvironmentKeys, str], optional
        :param api_url: _description_, defaults to `https://api.promptforge.com`
        :type api_url: str, optional
        :param custom_headers: _description_, defaults to None
        :type custom_headers: typing.Optional[typing.Dict[str, typing.Any]], optional
        :param request_timeout_seconds: _description_, defaults to None
        :type request_timeout_seconds: typing.Optional[int], optional
        :param enable_local_evaluation: if true, use a poller in the background instead of fetching data from api on every request, defaults to False
        :type enable_local_evaluation: bool, optional
        :param environment_refresh_interval_seconds: _description_, defaults to 60
        :type environment_refresh_interval_seconds: typing.Union[int, float], optional
        :param retries: _description_, defaults to None
        :type retries: typing.Optional[Retry], optional
        """
        self._session = requests.Session()
        self._session.headers.update(
            **{str(Keys.ORG_API_KEY): org_api_key}, **(custom_headers or {})
        )
        retries = retries or Retry(total=3, backoff_factor=0.1)

        self._api_url = api_url if api_url.endswith("/") else f"{api_url}/"
        self._request_timeout_seconds = request_timeout_seconds
        self._session.mount(self._api_url, HTTPAdapter(max_retries=retries))
        self._environment_refresh_interval_seconds = environment_refresh_interval_seconds
        self._environment_key = org_api_key
        self._application_env_string = application_env_string
        self._environment_url = f"{self._api_url}{URLS.ENVIRONMENT}"
        self._prompts_url = f"{self._api_url}{URLS.PROMPTS}"

        self._environment = None
        if enable_local_evaluation:
            if not org_api_key.startswith(Keys.SERVER_KEY_PREFIX):
                raise ValueError(
                    "In order to use local evaluation, please generate a server key "
                    "in the environment settings page."
                )

            self.environment_data_polling_manager_thread = (
                EnvironmentDataPollingManager(
                    main=self,
                    refresh_interval_seconds=environment_refresh_interval_seconds,
                )
            )
            self.environment_data_polling_manager_thread.start()
    
    def get_environment_prompts(self) -> LatestPromptVersions:
        """
        Get all the default for flags for the current environment.

        :return: Flags object holding all the flags for the current environment.
        """
        if self._environment:
            return self._environment.latest_prompts
        return self._get_prompts_from_api()
    
    def get_prompt_by_id(self, prompt_id: str) -> PromptVersion:
        """Get a prompt by prompt id.

        :param prompt_id: _description_
        :type prompt_id: str
        :raises PromptForgeAPIError: _description_
        :return: _description_
        :rtype: PromptVersion
        """        
        try:
            if self._environment:
                return self._environment.latest_prompts.prompts_by_id[prompt_id]
            return self._get_prompts_from_api().prompts_by_id[prompt_id]
        except KeyError as e:
            raise PromptForgeAPIError(f"Prompt with id {prompt_id} not found.") from e
    
    def get_prompt_by_name(self, prompt_name: str) -> PromptVersion:
        """
        Get a prompt by prompt name.
        
        :param prompt_name: _description_
        :type prompt_name: str
        :raises PromptForgeAPIError: _description_
        :return: _description_
        :rtype: PromptVersion
        """        
        try:
            if self._environment:
                return self._environment.latest_prompts.prompts_by_name[prompt_name]
            return self._get_prompts_from_api().prompts_by_name[prompt_name]
        except KeyError as e:
            raise PromptForgeAPIError(f"Prompt with name {prompt_name} not found.") from e

    
    def update_environment(self):
        logger.debug(f"Updating environment for {self._environment_key}")
        self._environment = self._get_environment_from_api()
    
    def _get_prompts_from_api(self) -> LatestPromptVersions:
        # TODO: switch to using prompts endpoint once it exists
        environment_data = self._get_json_response(self._environment_url, method=HttpMethods.GET, body=EnvironmentRequestBody(application_env_string=self._application_env_string).dict())
        try:
            env = EnvironmentModel(**environment_data)
            return env.latest_prompts
        except ValidationError as e:
            raise PromptForgeAPIError(
                "Unable to get valid response from PromptForge API."
            ) from e
    
    def _get_environment_from_api(self) -> EnvironmentModel:
        environment_data = self._get_json_response(self._environment_url, method=HttpMethods.GET, body=EnvironmentRequestBody(application_env_string=self._application_env_string).dict())
        try:
            return EnvironmentModel(**environment_data)
        except ValidationError as e:
            raise PromptForgeAPIError(
                "Unable to get valid response from PromptForge API."
            ) from e
    
    def _get_json_response(self, url: str, method: HttpMethods, body: typing.Optional[dict] = None) -> dict:
        """Get a JSON response from the API.

        :param url: _description_
        :type url: str
        :param method: _description_
        :type method: HttpMethods
        :param body: _description_, defaults to None
        :type body: typing.Optional[dict], optional
        :raises PromptForgeClientError: _description_
        :raises PromptForgeClientError: _description_
        :raises PromptForgeAPIError: _description_
        :raises PromptForgeAPIError: _description_
        :return: _description_
        :rtype: dict
        """        
        valid_methods = [HttpMethods.GET, HttpMethods.POST]
        try:
            if method not in valid_methods:
                raise PromptForgeClientError(
                    f"Invalid HTTP method: {method}. Must be one of {HttpMethods}."
                )
            request_method = None
            if method == HttpMethods.GET:
                request_method = self._session.get
            elif method == HttpMethods.POST:
                request_method = self._session.post
            else:
                raise PromptForgeClientError(
                    f"Invalid HTTP method: {method}. Currently implemented methods are {valid_methods}."
                )
            response = request_method(
                url, json=body, timeout=self._request_timeout_seconds
            )
            if response.status_code != 200:
                raise PromptForgeAPIError(
                    f"Invalid request made to Flagsmith API. Response status code: {response.status_code} Text: {response.text}",
                )
            return response.json()
        except (requests.ConnectionError, JSONDecodeError) as e:
            raise PromptForgeAPIError(
                "Unable to get valid response from PromptForge API."
            ) from e
    
    def __del__(self):
        if hasattr(self, "environment_data_polling_manager_thread"):
            self.environment_data_polling_manager_thread.stop()