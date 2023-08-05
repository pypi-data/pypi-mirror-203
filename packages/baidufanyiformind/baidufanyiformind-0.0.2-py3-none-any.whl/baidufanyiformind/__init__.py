#-*- coding: utf-8 -*-

name = "baidufanyiformind"

__all__ = ['_errcodeswitch','setAccount','baiduFanyi']

__version__ = '0.0.2'

import requests
import hashlib
import random



_baidufanyi_appid=''
_baidufanyi_sec=''

def _errcodeswitch(code=0):
    if code == '52000':
        return '成功'
    elif code == '52001':
        return '请求超时, 请重试'
    elif code == '52002':
        return '系统错误 , 请重试'
    elif code == '52003':
        return '未授权用户'
    elif code == '54000 ':
        return '缺少参数'
    elif code == '54001':
        return '签名错误'
    elif code == '54003':
        return '访问频率受限'
    elif code == '54004':
        return '账户余额不足'
    elif code == '54005':
        return '请求频繁'
    elif code == '58000':
        return '客户端IP非法'
    elif code == '58001':
        return '不支持的语言'
    elif code == '58002':
        return '服务已关闭'
    elif code == '90107':
        return ' 认证失败'
    else:
        return '未知错误'

def setAccount(appid,sec):
    global _baidufanyi_appid,_baidufanyi_sec
    if (len(appid) < 2) or (len(sec) < 2):
        print("error1: id或密钥为空，https://fanyi-api.baidu.com/")
    _baidufanyi_appid=appid.strip()
    _baidufanyi_sec=sec.strip()


def baiduFanyi(input_q='你好',tolan='en'):
    apiurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    if (len(_baidufanyi_appid) < 2) or (len(_baidufanyi_sec) < 2):
        print("error2: id或密钥为空，https://fanyi-api.baidu.com/")
        return "-1"
    salt=str(random.randint(3000, 65536))
    #print(baidufanyi_appid)
    sign=_baidufanyi_appid+input_q+salt+_baidufanyi_sec
    sign=hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()
    
    try:
        url="%s?q=%s&from=auto&to=%s&appid=%s&salt=%s&sign=%s"%(apiurl,input_q,tolan,_baidufanyi_appid,salt,sign)
        #print(url)
        baidu_response = requests.get(url)
        baidu_response.raise_for_status()
        #print((str("HTTPCode: ") + str(baidu_response.status_code)))
        resjson = baidu_response.json()
        #print((str("return:") + str(baidu_response.json())))
        if 'trans_result' in resjson:
            return ((resjson.get("trans_result")[0]).get("dst"))
        elif 'error_code' in resjson:
            print(_errcodeswitch(resjson.get('error_code')))
            return 'error'
        else:
            print("None")
            print((str("HTTPCode: ") + str(baidu_response.status_code)))
            return 'error'
    except:
        print("请求失败,检查网络连接")
        
        return 'error'
