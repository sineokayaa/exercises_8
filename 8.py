import datetime


def log_file(filename):
    '''
    function with fixed param for decorator
    :param filename: name of the file where will be mistakes
    :return: with_log result
    '''
    def with_log(func):
        '''
        decorator that creates a file with exception and time when it occured
        :param func: decorated func
        :return: wrapped
        '''
        def wrapped(*arg, **kwargs):
            '''
            decorated function checking for mistakes
            :param arg: any arguments
            :param kwargs: any keyword arguments
            :return: result of func if no mistakes, else None
            '''
            with open(filename, 'a') as f_out:
                try:
                    res = func(*arg, **kwargs)
                    return res
                except Exception as e:
                    print(e, datetime.datetime.now(), file=f_out)
            return

        return wrapped

    return with_log


@log_file(filename='out.txt')
def div(a, b):
    '''
    division
    :param a: num1
    :param b: num2
    :return: dividing a/b
    '''
    return a / b


@log_file(filename='mist.txt')
def errors(text):
    '''
    function checking for upper words
    :param text: any string
    :return: exception "Caps!" if text is upper, else  "It's okay."
    '''
    if text.isupper():
        raise Exception("Caps!")
    return "It's okay."


print(div(2, 0))
print(errors('AAa'))
