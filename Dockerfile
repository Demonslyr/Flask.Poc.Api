FROM python:3.8.7-slim-buster as base
LABEL maintainer="Daniel Murtha <dan@mail.atriarch.systems>"
RUN apt-get clean && apt-get update -y
COPY ./app /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x startup.sh
CMD [ "./startup.sh" ]