def res_func(func):
    '''
    decorator for wrapped function
    :param func: decorated func
    :return: return of function 'wrapped'
    '''
    def wrapped(sing_arg):
        '''
        start function with single argument
        :param sing_arg: any param
        :return: result of function with single param
        '''
        res = func(sing_arg)
        return res
    return wrapped

@res_func
def checked_a(word):
    '''
    function checks if english letter 'a' is in string
    :param word: any string
    :return: 1 if there is a letter 'a', else 0
    '''
    if 'a' in word.lower():
        return 1
    return 0


print(checked_a('Mama'))

