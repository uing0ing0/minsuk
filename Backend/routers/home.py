from fastapi import APIRouter

# Configure API router
hrouter = APIRouter(
    tags=['home'],
)


@hrouter.get('/')
async def get_root():
    return {
        'name': 'MobileX-Experience-Lab-Backend',
    }
