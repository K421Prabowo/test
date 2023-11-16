import json
from flask import jsonify 

def getResponse(code, data):
    return jsonify(data), code