import os
import boto3
import botostubs
from dotenv import load_dotenv
load_dotenv(verbose=True)


class EnvUtil:
    @staticmethod
    def get_env(name):
        return os.getenv(name)
