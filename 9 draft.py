import json
import yaml
import xml.etree.ElementTree as ET


def to_format(form=None):
    '''
    function converting python obj to other given format
    :param form: json, yaml, xml
    :return: format result
    '''
    def format(func):
        '''
        decorator for function
        :param func: decorated func
        :return: wrapped
        '''
        def wrapped(*arg, **kwargs):
            '''
            function that converts result of func to other format
            :param arg: any args
            :param kwargs: keyword arguments
            :return: result in needed format
            '''
            res = func(*arg, **kwargs)
            if form is None or form.lower() == 'json':
                res = json.dumps(res)
            elif form.lower() == 'xml':
                with open('file_res.xml', 'w') as f_xml:
                    print(res, file=f_xml)
            elif form.lower() == 'yaml':
                res = yaml.dump(res)
            return res

        return wrapped

    return format


@to_format()
def dictionary(a, b, c, d):
    '''
    function crated dictionary
    :param a: key1
    :param b: value1 for key1
    :param c: key 2
    :param d: value2 for key2
    :return: dictionary
    '''
    dict_ = {str(a): b, str(c): d}
    return dict_


print(dictionary(2, 4, 6, 8))
