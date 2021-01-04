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
                        // sh 'cdk deploy "RythmPriceCdkStackPriceSvcStackB5E813AA" --require-approval=never'
                    }
                }
            }
        }

        // stage('Build') {
        //     parallel {
        //         stage('Build Lambda') {
        //             steps {
        //                 dir('lambda-app') {
        //                     sh 'npm install'
        //                     sh 'npm run build'
        //                     sh 'cp -r ./build ../cdk-app-02/builds/lambda-app-build'
        //                 }
        //             }
        //         }

        //         stage('Build React') {
        //             steps {
        //                 dir('react-app') {
        //                     sh 'npm install'
        //                     sh 'npm run build'
        //                     sh 'cp -r ./build ../cdk-app-02/builds/react-app-build'
        //                 }
        //             }
        //         }
        //     }
        // }

    // stage('Deploy') {
    //     parallel {
    //         stage('Run the CDK') {
    //             steps {
    //                 dir('cdk-app-02') {
    //                     withAWS(credentials: 'build-credentials', region: 'us-east-1') {
    //                         sh 'aws s3 ls'
    //                         sh 'npm install'
    //                         sh 'npm run build'
    //                         sh 'cdk deploy \\"*\\" --require-approval=never'
    //                         sh 'aws s3 sync builds/react-app-build/build s3://origin.mytodos.xyz --acl public-read'
    //                         sh 'aws cloudfront create-invalidation --distribution-id E3B6B3IT43ZK0P --paths "/*"'
    //                     }
    //                 }
    //             }
    //         }
    //     }
    // }
    }
}
