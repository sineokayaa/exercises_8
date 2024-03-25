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
                if str == type(res):
                    root = ET.Element("root")
                    data = ET.SubElement(root, "data")
                    ET.SubElement(data, "string").text = res
                    res = ET.tostring(root, encoding="unicode")
                elif dict == type(res):
                    root = ET.Element("root")
                    for key, value in res.items():
                        element = ET.SubElement(root, key)
                        element.text = str(value)
                    res = ET.tostring(root, encoding="unicode")
                    return res
                elif list == type(res):
                    root = ET.Element("root")
                    data = ET.SubElement(root, "data")
                    for i in res:
                        ET.SubElement(data, 'item').text = str(i)
                    res = ET.tostring(root, encoding='unicode')
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
