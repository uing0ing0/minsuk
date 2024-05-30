from fastapi import APIRouter

# Configure API router
healthRouter = APIRouter(
    tags=['health'],
)


@healthRouter.get('/_health')
async def get_health():
    return {
        'status': 'Ok',
    }
