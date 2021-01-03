docker pull python:3.7-slim
docker tag python:3.7-slim 778477161868.dkr.ecr.us-west-2.amazonaws.com/python-37-slim:latest
docker push 778477161868.dkr.ecr.us-west-2.amazonaws.com/python-37-slim:latest