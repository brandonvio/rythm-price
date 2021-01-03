import os
import boto3
import botostubs
from dotenv import load_dotenv
load_dotenv(verbose=True)


boto3.setup_default_session(region_name="us-west-2")
client: botostubs.SecretsManager = boto3.client('secretsmanager')


class EnvUtil:
    @staticmethod
    def get_env(name):
        return os.getenv(name)

    @staticmethod
    def get_secret(secretId):
        val = client.get_secret_value(SecretId=secretId)
        print("// Getting secret for secretid: " + secretId)
        return val["SecretString"]
