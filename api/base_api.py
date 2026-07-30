import json
import requests
from logger import logger


with open("config/api_config.json", "r") as file:
    config = json.load(file)

BASE_URL = config["BASE_URL"]
last_request = {}
last_response = {}


def get(endpoint):
    logger.info(f"Sending GET request to {BASE_URL}{endpoint}")

    response = requests.get(f"{BASE_URL}{endpoint}")

    logger.info(f"Received response with status code {response.status_code}")

    return response
    


def post(endpoint, body):
    global last_request, last_response



    last_request = {
        "method": "POST",
        "url": f"{BASE_URL}{endpoint}",
        "body": body
    }

    logger.info(f"POST Request: {BASE_URL}{endpoint}")
    logger.info(f"Request Body: {body}")

    response = requests.post(
        f"{BASE_URL}{endpoint}",
        json=body
    )

    last_response = {
        "status_code": response.status_code,
        "body": response.json()
    }

    logger.info(f"Status Code: {response.status_code}")

    return response

    
   
def put(endpoint, body):
    logger.info(f"Sending PUT request to {BASE_URL}{endpoint} with body: {body}")

    response = requests.put(
        f"{BASE_URL}{endpoint}",
        json=body
    )

    logger.info(f"Received response with status code {response.status_code}")

    return response
    


def delete(endpoint):
    logger.info(f"Sending DELETE request to {BASE_URL}{endpoint}")

    response = requests.delete(f"{BASE_URL}{endpoint}")

    logger.info(f"Received response with status code {response.status_code}")

    return response