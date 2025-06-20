from decouple import config
from service import addServiceLayer
from fastapi import FastAPI, Path, HTTPException

api = FastAPI()

addServiceLayer(api)