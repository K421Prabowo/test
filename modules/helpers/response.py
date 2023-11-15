import json
from requests.models import Response

def getResponse(code, data):
    res = Response()
    res.status_code = code
    res.content = data
    return res.json()