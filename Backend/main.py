import os
import dotenv
from fastapi import FastAPI

from mobilex.Backend import routers

# Load environment variables from dotenv file
dotenv.load_dotenv()

app = FastAPI(
    root_path=os.environ.get('BASE_URL', ''),
)

# Register all available routers
app.include_router(routers.functions.youtube_topic_recommendations.router)
app.include_router(routers.health.router)
app.include_router(routers.home.router)
