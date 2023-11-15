
import json
import traceback
import pandas as pd

from flask import request

from config import *
from modules.libs.upload_data import uploadDatas
from modules.helpers.logger import getLogger
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
            return json.dumps(results)
        except Exception as e :
            logger.error(e)
            logger.error(traceback.format_exc())

    def getDataById(self, id):
        try:
            params = self.objData.getById
            results = params
            return json.dumps(results)
        except Exception as e :
            logger.error(e)
            logger.error(traceback.format_exc())

    def setData(self):
        try:
            results = None
            return json.dumps(results)
        except Exception as e :
            logger.error(e)
            logger.error(traceback.format_exc())

    def updateData(self, id):
        try:
            results = None
            return json.dumps(results)
        except Exception as e :
            logger.error(e)
            logger.error(traceback.format_exc())

    def deleteData(self, id):
        try:
            results = None
            return json.dumps(results)
        except Exception as e :
            logger.error(e)
            logger.error(traceback.format_exc())

    def uploadData(self):
        try :
            for field, file in request.files.items():
                if field == "file":
                    print('filename:', file.filename)
                    if file.filename:
                        xls = pd.ExcelFile(file)
                        logger.info(xls.sheet_names)
                        uploadDatas(xls, file)
            return "OK" 
            # return result
        except Exception as e :
            logger.error(e)
            logger.error(traceback.format_exc())
