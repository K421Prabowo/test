import traceback

from flask import Flask

from config import *
from modules.api import Api
from modules.helpers.logger import getLogger

app = Flask(__name__)
api = Api()

logger = getLogger("main")

logger.info("Serving on http://"+ host + ":" + str(port))

@app.get("/data")
def getData():
    return api.getData()

@app.get("/data/<int:id>")
def getDataById(id):
    return api.getDataById(id)

@app.post("/data")
def setData():
    return api.setData()

@app.put("/data/<int:id>")
def updateData(id):
    return api.updateData(id)

@app.delete("/data/<int:id>")
def deleteData(id):
    return api.deleteData(id)

@app.post("/upload")
def uploadData():
    return api.uploadData()

if __name__ == '__main__':
    try:
        from waitress import serve
        serve(app, host=host, port=port)
    except :
        logger.error(traceback.format_exc())