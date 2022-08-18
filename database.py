import pymongo as pg
import certifi
import os

def connectDataBase():
    c = 'mongodb+srv://LouisTsai:Q3731722Q@cluster0.so4ff.mongodb.net/AKASWAP?retryWrites=true&w=majority'
    client = pg.MongoClient(c,tlsCAFile=certifi.where())#,ssl=True)#,ssl_cert_reqs='CERT_NONE')
    return client['automatest']

def getExamDB():
    return connectDataBase()['exam']

def getSequenceDB():
    return connectDataBase()['sequence']

def getStudentDB():
    return connectDataBase()['student']

def getClassesDB():
    return connectDataBase()['classes']
