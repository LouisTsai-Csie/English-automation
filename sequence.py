'''
sequence = {
    'seq': [string, string, string, ...]
    'index': int,
    'des': string,
}
'''
sequence = {
    'category': ['1_1', '1_2', '2_1', '2_2'],
    'index': 2,
    'des': 'test',
}

def getExamCategory():
    index = sequence['index'] #index of which category of exam they should take.
    category = sequence['category'] #the exam itself
    sequence['index'] = (index+2) % len(category)
    return (category[index], category[(index+1)%len(category)])



    