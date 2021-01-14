aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 778477161868.dkr.ecr.us-west-2.amazonaws.com
docker build -f DockerfileOanda  -t rythm-svc-oanda .