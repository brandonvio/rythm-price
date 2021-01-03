FROM 778477161868.dkr.ecr.us-west-2.amazonaws.com/python-37-slim:latest

WORKDIR /usr/oanda-stream
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src/ ./src
COPY ./app.py .
COPY .env .
ENTRYPOINT ["python", "app.py"]