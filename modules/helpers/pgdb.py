import psycopg2
import traceback
from config import dbhost, dbname, dbpass, dbuser
from modules.helpers.logger import getLogger

logger = getLogger("pgdb")

def connectDB():
    try:
        result = psycopg2.connect(
                host=dbhost,
                database=dbname,
                user=dbuser,
                password=dbpass)
        return result 
    except Exception as e :
        logger.error(e)
        logger.error(traceback.format_exc())

conn = connectDB()
