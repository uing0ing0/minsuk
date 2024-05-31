from typing import Literal

from pydantic import BaseModel, Field


class InputModel(BaseModel):

    target_viewers: Literal[
        'Students',
        'Freelancers',
        'employee',
        'Technician',
        'Public official',
    ] = Field(
        default='Freelancers',
    )
    target_age: Literal[
        'junior',
        'teenager',
        '20s-30s',
        '40s-',
    ] = Field(
        default='junior',
    )
    target_country: Literal[
        'USA',
        'Korea',
        'United Kingdom',
        'North Korea'
    ] = Field(
        default='Korea',
    )

    llm_type: Literal['chatgpt', 'huggingface'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )


class OutputModel(BaseModel):
    output: str = Field(
        description='Expected Questions',
    )
