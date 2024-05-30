import os
import dotenv
from fastapi import FastAPI


from .routers.home import hrouter
from .routers.health import healthRouter
from .routers.functions.youtube_topic_recommendations import router

# from mobilex.Backend import routers
# Load environment variables from dotenv file
dotenv.load_dotenv()

app = FastAPI(
    # root_path=os.environ.get('BASE_URL', ''),
)

# Register all available routers
app.include_router(router)
app.include_router(healthRouter)
app.include_router(hrouter)
