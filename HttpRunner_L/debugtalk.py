import random
import requests



def get_search_word():
    word_list=['newdream','12306','火车票','新梦想软件测试']
    num=random.randint(0,len(word_list)-1)
    return word_list[num]

def setup_case(set_name):
    print('测试用例%s 执行'%set_name)

def teardown_case(set_name):
    print('测试用例%s 结束'%set_name)

def get_true():
    return True

def get_access_token():
    p_dict={
        'grant_type': 'client_credential',
        'appid': 'wxb6807ba1b89130e1',
        'secret': '652d6c4b429791c80f0badbda6a00829'
    }
    try:
        response=requests.get(url='https://api.weixin.qq.com/cgi-bin/token',
                              params=p_dict)
        token=response.json()['access_token']
    except KeyError as e:
        token=None
    return token








if __name__=='__main__':
    print(get_access_token())
