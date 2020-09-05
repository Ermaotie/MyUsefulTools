import os

path = 'D:/临时'


def delete(path):
    try:
        _list = os.listdir(path)
        for each in _list:
            each = os.path.join(path, each)
            print(each)
            if os.path.isfile(each):
                os.remove(each)
            if os.path.isdir(each):
                delete(each)
                os.rmdir(each)
    except:
        print('出现错误')


delete(path)
