import os

from fastapi import APIRouter

from llm.chat import build
from llm.store import LLMStore
from models.characterize import InputModel, OutputModel

# Configure API router
router = APIRouter(
    tags=['functions'],
)

# Configure metadata
NAME = os.path.basename(__file__)[:-3]

# Configure resources
store = LLMStore()

###############################################
#                   Actions                   #
###############################################


@router.post(f'/func/{NAME}')
async def call_acrostic_generator(model: InputModel) -> OutputModel:
    # Create a LLM chain
    chain = build(
        name=os.path.basename(__file__)[:-3],
        llm=store.get(model.llm_type),
    )

    return OutputModel(
        output=chain.invoke({
            'input_context': f'''
                # About Charactor
                * Animation name: {model.animation}
                * Charactor name: {model.charactor}
                * Charactor's current situation: {model.situation}

                # User's Talk
                {model.context}
            ''',
        }),
    )
