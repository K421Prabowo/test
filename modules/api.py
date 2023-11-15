
import json
import traceback

from flask import request
from requests.models import Response

from config import *
from modules.libs.upload_data import uploadDatas
from modules.helpers.logger import getLogger
from modules.helpers.response import getResponse
from modules.controllers.indexs import Data, Datas

logger = getLogger("api")

class Api:
    data = Data()
    objData = Datas()
    datas = []

    def __init__(self):
        self.data = Data()
        self.objData = Datas()
        self.datas = []
        pass

    def getData(self):
        try:
            args = request.args
            page = args.get("page", default=1, type=int)
            limit = args.get("limit", default=10, type=int)
            results = []
            params = self.objData.getAll(page, limit)
            for item in params:
                results.append(item)
            return getResponse(200, results)
        except Exception as e :
            logger.error(e)
            logger.error(traceback.format_exc())
            return getResponse(404, traceback.format_exc())

    def getDataById(self, id):
        try:
            results = self.objData.getById(id)
            return getResponse(200, results)
        except Exception as e :
            logger.error(e)
            logger.error(traceback.format_exc())
            return getResponse(404, traceback.format_exc())

    def setData(self):
        try:
            jData = request.get_json()
            
            param = Data()
            param.type = jData["type"]
            param.froms = jData["froms"]
            param.status = jData["status"]
            param.text = jData["text"]
            param.attachment = jData["attachment"]
            param.meta = jData["meta"]
            param.data_date = jData["data_date"]
            
            results = self.objData.setData(param)
            return getResponse(200, results)
        except Exception as e :
            logger.error(e)
            logger.error(traceback.format_exc())
            return getResponse(404, traceback.format_exc())

    def updateData(self, id):
        try:
            jData = request.get_json
            
            param = Data()
            param.type = jData["type"]
            param.froms = jData["froms"]
            param.status = jData["status"]
            param.text = jData["text"]
            param.attachment = jData["attachment"]
            param.meta = jData["meta"]
            param.data_date = jData["data_date"]
            
            results = self.objData.setData(param)
            return getResponse(200, results)
        except Exception as e :
            logger.error(e)
            logger.error(traceback.format_exc())
            return getResponse(404, traceback.format_exc())

    def deleteData(self, id):
        try:
            self.objData.deleteData(id)
            return getResponse(200, f"delete data with id {id} success")
        except Exception as e :
            logger.error(e)
            logger.error(traceback.format_exc())
            return getResponse(404, e)

    def uploadData(self):
        try :
            for field, file in request.files.items():
                if field == "file":
                    print('filename:', file.filename)
                    if file.filename:
                        fileName = file.name
                        out_file = open(fileName,'w')
                        out_file.write(file.read())
            return getResponse(200, f"upload data success")
        except Exception as e :
            logger.error(e)
            logger.error(traceback.format_exc())
            return getResponse(404, traceback.format_exc())
