import pymongo as pg
import certifi
import os

def connectDataBase():
    client = pg.MongoClient(os.environ(CONNECT_STRING),tlsCAFile=certifi.where())#,ssl=True)#,ssl_cert_reqs='CERT_NONE')
    return client['automatest']

def getTemp():
    return client['TempDB']

def getExamDB():
    return connectDataBase()['exam']

def getSequenceDB():
    return connectDataBase()['sequence']

def getStudentDB():
    return connectDataBase()['student']

def getClassesDB():
    return connectDataBase()['classes']
