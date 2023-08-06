"""
create by cxo on 2023.03.16
用于通过accessId与指定的服务器进行通信
可以进行数据的查询下载，并返回pandas的dataFrame
"""
import pandas as pd
import json
import requests as rq

class DataApi:

    __token = ''
    __http_url = 'http://www.asieai.com/quant/php/bar_pro.php'
    __uid = 'data_share'

    def __init__(self, token='', uid='data_share', timeout=120):
        """
        Parameters
        ----------
        token: str
            API接口的接入密钥字符串，用于用户的认证
        """
        self.__token = token
        self.__timeout = timeout
        self.__uid = uid

    def query(self, api_name, fields='', **kwargs):
        req_params = {
            'api': api_name,
            'tok': self.__token,
            'uid': self.__uid,
            'params': kwargs
        }

        res = rq.post(self.__http_url, json=req_params, timeout=self.__timeout)

        if not res:
            return pd.DataFrame()
        try:
            result = json.loads(res.text)
        except Exception as e:
            return pd.DataFrame()

        return pd.DataFrame(result['data'], columns=result['cols'])