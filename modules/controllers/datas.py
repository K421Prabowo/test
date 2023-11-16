import json
import traceback

from modules.helpers.pgdb import conn 
from modules.helpers.logger import getLogger
from modules.models.datas import Data

logger = getLogger("datas")

class Datas():
    cur = None
    def __init__(self):
        if conn != None:
            self.cur = conn.cursor()

    def set(self, data):
        param = Data()
        param.id = data[0]
        param.type = data[1]
        param.froms = data[2]
        param.status = data[3]
        param.text = data[4]
        param.attachment = data[5]
        param.meta = data[6]
        param.data_date = data[7]

        return param
       
    def get(self, sql):
      self.cur.execute(sql)
      tempDatas = self.cur.fetchall()
      result = []
      for data in tempDatas:
         result.append(self.set(data))
      conn.commit()
      return result
    
    def getById(self, id):
      sql = f"SELECT * FROM public.datas where id = {id}"
      self.cur.execute(sql)
      tempData = self.cur.fetchone()
      result = self.set(tempData)
      conn.commit()
      return result

    def getAll(self, page, limit):
      offset = limit * (page - 1)
      sql = f"SELECT * FROM public.datas ORDER BY id LIMIT {limit} OFFSET {offset}"
      logger.info(sql)
      self.cur.execute(sql)
      tempDatas = self.cur.fetchall()
      result = []
      for data in tempDatas:
         result.append(self.set(data))
      conn.commit()
      return result

    def setData(self, data: Data):
      sql = f"""INSERT INTO public.datas(
                    type, froms, status, text, attachment, meta, data_date
                ) VALUES (
                    '{data.type}', '{data.froms}', '{data.status}', '{data.text}', '{data.attachment}', '{data.meta}', '{data.data_date}'
                ) RETURNING id;"""
      self.cur.execute(sql)
      result = self.cur.fetchone()[0]
      conn.commit()
      return result

    def updateData(self, data: Data):
      sql = f"SELECT * FROM public.datas where id = {data.id}"
      self.cur.execute(sql)
      tempdb = self.cur.fetchall()
      if len(tempdb) > 0:
        sql = f"""UPDATE public.datas
                    SET type='{data.type}', froms='{data.froms}', status='{data.status}', text='{data.text}', attachment='{data.attachment}', meta='{data.meta}', data_date='{data.data_date}'
                WHERE id = {data.id} RETURNING id;"""
        self.cur.execute(sql)
        result = self.cur.fetchone()[0]
        conn.commit()
        return {"status": True}
      else:
        return {"status": False}

    def deleteData(self, id: int):
      sql = f"SELECT * FROM public.datas where id = {id}"
      self.cur.execute(sql)
      tempdb = self.cur.fetchall()
      if len(tempdb) > 0:
        sql = f"DELETE FROM public.datas WHERE id = {id};"
        self.cur.execute(sql)
        conn.commit()
        return {"status": True}
      else:
        return {"status": False}