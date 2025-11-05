from fastapi import FastAPI, APIRouter
import os
base_router  =  APIRouter (
    prefix =  "/api/v1",#prefix for all routes in this router
    tags =  ["Base"] #tag for grouping routes in documentation
)
@base_router.get("/")

def welcome():
    app_name=os.getenv("APP_NAME")
    app_version=os.getenv("APP_VERSION")
    return {"message": "Welcome to Mini-Rag API!"
            ,"app_name":app_name
            ,"app_version":app_version
        }
