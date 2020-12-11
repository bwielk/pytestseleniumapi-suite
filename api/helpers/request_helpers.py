from requests import Request, Session, Response
import json


def simple_get(endpoint_path):
    request = Session()
    response = request.get(endpoint_path)
    json = response.json()
    return json