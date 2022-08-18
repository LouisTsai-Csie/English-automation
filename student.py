import database
import mode

def userInfoInit(LineID, userName):
    student = database.getStudentDB()
    info = {
        'name': userName,
        'LineID': LineID,
        'state': mode.STUDENT_NO_CLASS,
        'mode': mode.NORMAL,
        'testing': {
            'exam': '',
            'index': 0,
        }
        'classes': '',
        'score': {
            'first': 0,
            'second': 0
        }
    }
    student.insert_one(info)
    return

def getUser(LineID, userName):
    student = database.getStudentDB()
    condition = {'LineID': LineID}
    user = student.find_one(condition)
    if user is None:
        userInfoInit(LineID, userName)
        return student.find_one(condition)
    return user

def userModeUpdate(user, mode):
    student = database.getStudentDB()
    condition = {'LineID': user['LineID']}
    option = {'$set': {'mode': mode}}
    student.update_one(condition, option)
    return 

def userStateUpdate(user, state):
    student = database.getStudentDB()
    condition = {'LineID': user['LineID']}
    option = {'$set': {'state': state}}
    student.update_one(condition, option)
    return

def userExamUpdate(user, exam, index):
    student = database.getExamDB()
    condition = {'LineID': user['LineID']}
    op = {
        'exam': exam,
        'index': index
    }
    option = {'$set': {'testing': op}}
    student.update_one(condition, option)
    return

def userScoreUpdate(user, type):
    if type == 'first':
        pass
    elif type == 'second':
        pass
    return