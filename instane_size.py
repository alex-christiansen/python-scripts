from dotenv import load_dotenv
import requests
import os
import json
from urllib.parse import urlparse

# Set Globals / import env variables
load_dotenv()
base_url = os.getenv('base_url')
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

# Log into the API and grab bearer token
api_call = f'/login?client_id={client_id}&client_secret={client_secret}'
response = requests.request("POST", base_url+api_call)
bearer_token = json.loads(response.text)['access_token']
headers = {
  'Authorization': 'Bearer %s' % bearer_token
}

# Get all lookml models
api_call = '/lookml_models'
response = requests.request("GET", base_url+api_call, headers=headers)
model_response_time = response.elapsed.total_seconds()
total_models = len(json.loads(response.text))

# Project Data
api_call = '/projects'
response = requests.request("GET", base_url+api_call, headers=headers)
project_response_time = response.elapsed.total_seconds()
total_projects = len(json.loads(response.text))

print(f"""
The {urlparse(base_url)[1].split(".")[0]} instance has the following statistics:
    Total Models: {total_models}
    Model Response Time: {model_response_time}
    Total Projects: {total_projects}
    Project Response Time: {project_response_time}
""")
