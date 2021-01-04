// Testing webhook. #9
pipeline {
    agent any
    stages {
        stage('Validate') {
            steps {
                sh 'aws --version'
                sh 'cdk --version'
                sh 'node --version'
                sh 'npm --version'
                sh 'tsc --version'
            }
        }

        stage('Building') {
            steps {
                withAWS(credentials: 'build-credentials', region: 'us-west-2') {
                    dir('rythm-price-cdk') {                        
                        sh 'npm install'
                        sh 'cdk list'
                        sh 'cdk synth --all'
                        sh 'cdk deploy "RythmPriceCdkStackPriceEcrStackC0F5E0B6" --require-approval=never'
                    }
                    dir('rythm-price-svc') {
                        sh 'aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 778477161868.dkr.ecr.us-west-2.amazonaws.com'
                        sh 'docker build -t rythm-svc-price .'
                        sh 'docker tag rythm-svc-price:latest 778477161868.dkr.ecr.us-west-2.amazonaws.com/rythm-svc-price:latest'
                        sh 'docker push 778477161868.dkr.ecr.us-west-2.amazonaws.com/rythm-svc-price:latest'
                    }
                    dir('rythm-price-cdk') {
                        sh 'cdk deploy "RythmPriceCdkStackPriceSvcStackB5E813AA" --require-approval=never'
                    }
                }
            }
        }

        stage('ECS') {
            steps {
                withAWS(credentials: 'build-credentials', region: 'us-west-2') {
                    sh 'aws ecs update-service --desired-count 0 --cluster rythm-cluster --service rythm-price-service'
                    sh 'aws ecs wait services-stable --cluster rythm-cluster --services rythm-price-service'
                    sh 'aws ecs update-service --desired-count 1 --cluster rythm-cluster --service rythm-price-service --force-new-deployment'
                }
            }
        }
    }
}
