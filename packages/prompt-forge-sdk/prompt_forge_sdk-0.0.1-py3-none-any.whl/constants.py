from enum import Enum

class StringConstantEnum(str, Enum):
    def __str__(self) -> str:
        return str(self.value)
    def __repr__(self) -> str:
        return str(self.value)


class URLS(StringConstantEnum):
    ENVIRONMENT = "sdk/environment"
    PROMPTS = "sdk/prompts"
    DEFAULT_API_URL = "https://api.promptforge.com/api"

class Keys(StringConstantEnum):
    ENVIRONMENT_KEY = "X-Environment-Key"
    IDENTITY_KEY = "X-Identity-Key"
    ORG_API_KEY = "X-Organization-Key"
    SERVER_KEY_PREFIX = "ser-"

class HttpMethods(StringConstantEnum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    HEAD = 'HEAD'
    OPTIONS = 'OPTIONS'
    PATCH = 'PATCH'

class DefaultEnvironmentKeys(StringConstantEnum):
    DEVELOPMENT = "dev"
    PRODUCTION = "prod"
    STAGING = "staging"