'''
database schema: exam

exams = [
    {
        'problem': string,
        'option': [string, string, ...],
        'answer': string,
        'category': string,
        'index': int,
        'description': string,
    },
    ...
]
'''

'''
exams = [
    {
        'problem': '',
        'option': ['', '', '', ''],
        'answer': '',
        'category': '',
        'index': 0,
        'description': ''
    }
]
'''

import database

def getExam(category, index):
    exam = database.getExamDB()
    condition = {'category': category}
    items = exam.find(condition)
    for item in items:
        if item['index'] == index:
            return item
    return None

