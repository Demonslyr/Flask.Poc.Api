# Python.Api.Poc

## Info
A demonstration python api using [FastAPI](https://fastapi.tiangolo.com), [Uvicorn](https://www.uvicorn.org), and [Gunicorn](https://docs.gunicorn.org)

## To build
docker build -t pythonpoc -f ./Dockerfile .

## To run
docker run -d --name pythonfastAPI -p 8080:80 pythonpoc

## Log & Access log sample
```
[2020-12-27 10:43:23 +0000] [17] [INFO] Waiting for application startup.
[2020-12-27 10:43:23 +0000] [17] [INFO] Application startup complete.
[2020-12-27 10:43:23 +0000] [18] [INFO] Started server process [18]
[2020-12-27 10:43:23 +0000] [18] [INFO] Waiting for application startup.
[2020-12-27 10:43:23 +0000] [18] [INFO] Application startup complete.
172.17.0.1:44978 - "GET /docs HTTP/1.1" 200
172.17.0.1:44978 - "GET /openapi.json HTTP/1.1" 200
172.17.0.1:44984 - "GET /owo_proxy/love%20that%20uwu%20text HTTP/1.1" 200
172.17.0.1:44992 - "GET /owo_proxy/love%20that%20uwu%20text HTTP/1.1" 200
172.17.0.1:44992 - "GET /owo_proxy/love%20that%20uwu%20text HTTP/1.1" 200
172.17.0.1:44992 - "GET /owo_proxy/love%20that%20uwu%20text HTTP/1.1" 200
```
