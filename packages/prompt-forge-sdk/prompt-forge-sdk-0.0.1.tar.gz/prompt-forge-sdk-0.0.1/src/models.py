from datetime import datetime
from typing import Optional, Union
from dateutil.parser import parse as parse_datetime
from pydantic import BaseModel, validator, ValidationError
from constants import DefaultEnvironmentKeys

class TimestampMixin(BaseModel):
    createdAt: datetime
    updatedAt: datetime
    deletedAt: Optional[datetime] = None

    @validator('createdAt', 'updatedAt', 'deletedAt', pre=True)
    def parse_datetime(cls, value):
        if value is None:
            return value
        if isinstance(value, datetime):
            return value
        return parse_datetime(value)
    
class PromptForgeClientError(Exception):
    pass


class PromptForgeAPIError(PromptForgeClientError):
    pass

class PromptForgeApiMixin(BaseModel):
    id: str 



class PromptResponse(PromptForgeApiMixin):
    content: str
    promptId: str
    promptVersionId: str

class PromptVersion(PromptForgeApiMixin, TimestampMixin):
    name: str
    content: str
    version: int
    promptId: str

    def __str__(self) -> str:
        return self.content
class Prompt(PromptForgeApiMixin, TimestampMixin):
    name: str
    collectionId: str
    versions: list[PromptVersion]
    responses: list[PromptResponse]

class Collection(PromptForgeApiMixin, TimestampMixin):
    name: str
    prompt: list[Prompt]
    orgId: str

class LatestPromptVersions(BaseModel):
    prompts: list[PromptVersion]
    prompts_by_id: dict[str, PromptVersion] = {}
    prompts_by_name: dict[str, PromptVersion] = {}

    @validator('prompts_by_id', always=True)
    def parse_prompts(cls, value, values) -> dict[str, PromptVersion]:
        latest_prompts: list[PromptVersion] = values['prompts']
        if latest_prompts is None:
            raise ValueError(f'prompts must be set, but got {latest_prompts}')

        return {prompt.promptId: prompt for prompt in latest_prompts}
    
    @validator('prompts_by_name', always=True)
    def parse_prompts_by_name(cls, value, values) -> dict[str, PromptVersion]:
        latest_prompts: list[PromptVersion] = values['prompts']
        if latest_prompts is None or not isinstance(latest_prompts, list):
            raise ValueError(f'prompts must be set, but got {latest_prompts}')

        return {prompt.name: prompt for prompt in latest_prompts}

class EnvironmentModel(BaseModel):
    latest_prompts: LatestPromptVersions

class EnvironmentRequestBody(BaseModel):
    application_env_string: Union[str, DefaultEnvironmentKeys] = DefaultEnvironmentKeys.DEVELOPMENT
