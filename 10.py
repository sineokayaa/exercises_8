import time

def reqs(time_limit, num_of_calls):
    '''
    function with requirements
    :param time_limit: limit of time
    :param num_of_calls: limit of calls
    :return: result of stop
    '''
    def stop(func):
        '''
        decorator for func
        :param func: any func
        :return: result of wrapper
        '''
        calls = [0]
        calls_time = [0]

        def wrapper(*args, **kwargs):
            '''
            decorated func
            :param args: any args
            :param kwargs: any keyword arguments
            :return: exception 'Time limit' if time of performing a function
            is more than given time, exception 'Calls limit' if number of calls
            is more than given number, else calls_time, calls, res


            '''
            calls[0] += 1
            time_start = time.time()
            res = func(*args, **kwargs)
            time_finish = time.time()
            time_ = time_finish - time_start
            calls_time[0] += time_

            if calls_time[0] > time_limit:
                raise Exception('Time limit')

            if calls[0] > num_of_calls:
                raise Exception('Calls limit')

            return calls_time, calls, res

        return wrapper

    return stop


@reqs(10, 100)
def slow_func(a):
    time.sleep(3)
    return a + 1


for i in range(6):
    print(slow_func(2))
