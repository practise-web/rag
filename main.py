from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(".env")  # Load environment variables from a .env file if present
#make sure load_dotenv is called before importing routes
#it save env in system environment
from routes import base
app = FastAPI()
app.include_router(base.base_router)