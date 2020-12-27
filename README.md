# Python.Api.Poc

## Info
A demonstration python api using [FastAPI](https://fastapi.tiangolo.com), [Uvicorn](https://www.uvicorn.org), and [Gunicorn](https://docs.gunicorn.org)

## To build
docker build -t pythonpoc -f ./Dockerfile .

## To run
docker run -d --name pythonfastAPI -p 8080:80 pythonpoc
