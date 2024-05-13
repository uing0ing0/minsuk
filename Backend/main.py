import dotenv
from fastapi import FastAPI

import routers

# Load environment variables from dotenv file
dotenv.load_dotenv()

app = FastAPI()

# Register all available routers
app.include_router(routers.functions.acrostic_generator.router)
app.include_router(routers.health.router)
app.include_router(routers.home.router)
