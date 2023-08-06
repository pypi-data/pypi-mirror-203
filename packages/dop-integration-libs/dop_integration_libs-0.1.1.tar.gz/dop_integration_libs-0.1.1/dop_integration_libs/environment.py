import os
import requests

class Environment(object):
    def __init__(self):
        self.LOG_API_TOKEN = os.environ['LOG_API_TOKEN']
        self.LOG_API_BASE_URL = os.environ['LOG_API_BASE_URL']
        self.API_BASE_URL = os.environ['API_BASE_URL']
        self.REMOTE_TOKEN = os.environ['REMOTE_TOKEN']


    
    @staticmethod
    def get_envirement():
        return Environment()
