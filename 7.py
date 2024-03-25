import json
import functools

def to_json(func):
    '''
    decorator convert python object to json object
    :param func: decorated finction
    :return: wrapped function
    '''
    @functools.wraps(func)
    def wrapped(*arg, **kwargs):
        '''
        function which we decorate
        :param arg: any arguments
        :param kwargs: keyword arguments
        :return: result of function
        '''
        res = func(*arg, **kwargs)
        res_json = json.dumps(res)
        return res_json
    return wrapped


@to_json
def mult(a, b):
    '''
    multiplies a and b
    :param a: number or string
    :param b: number
    :return: result of a multiplied by b
    '''
    return a*b

@to_json
def cr_dict(a, b):
    '''
    creating a dictionary
    :param a: key
    :param b: value
    :return: dictionaru
    '''
    classroom = {}
    classroom[a] = b
    return classroom

@to_json
def check(word):
    '''
    checking if word is upper
    :param word: any string
    :return: "Caps!" if word is upper, else "It's fine."
    '''
    if word == word.upper():
        return "Caps!"
    return "It's fine."


print(mult(2,4))
print(cr_dict('num_students', 5))
print(check('OKAY'))