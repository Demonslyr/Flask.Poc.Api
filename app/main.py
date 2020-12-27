import base64
import json
import sys
import time
#https://realpython.com/python-requests/
import requests

from html import escape
from fastapi import Depends, FastAPI, HTTPException, status, Request, Header
from jose import JWTError, jwt
from pydantic import BaseModel
app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get("/owo_proxy/{text}")
def owo_proxy(text):
    response = requests.get(f'https://owo.drinkpoint.me/{escape(text)}')
    return {"message": response.content}

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/hello")
def hello_endpoint():
    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    message = f"Hello world! From Uvicorn with Gunicorn. Using Python {version}".encode("utf-8")
    return {"message": message}

@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}

@app.get("/items_int/{item_id}")
def read_item_int(item_id: int):
    return {"item_id": item_id}

class DataWithSecretsIn(BaseModel):
    data: str
    secret: str

class DataWithSecretsOut(BaseModel):
    data: str

@app.post("/data/", response_model=DataWithSecretsOut)
def ingest_data_and_secrets(dataPayload: DataWithSecretsIn):
    return dataPayload

@app.get("/jwtDecode")
def reurn_decoded_JWT(authorize: str = Header(None)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token = authorize.split(' ')[1]
        token_parts = token.split('.')
        decoded_payload = json.loads(base64.b64decode(token_parts[1]).decode("utf-8"))

        username: str = decoded_payload["sub"]

        # payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username