aws ecs list-tasks --cluster rythm-cluster --service-name rythm-price-service
aws ecs describe-tasks --cluster rythm-cluster --tasks arn:aws:ecs:us-west-2:778477161868:task/rythm-cluster/ef1bf2bc055a46f8801303b50755c85d
# aws ecs stop-task --cluster rythm-cluster --task arn:aws:ecs:us-west-2:778477161868:task/rythm-cluster/c2c3ecb055194d06ad4e2ea5b2ebd10f