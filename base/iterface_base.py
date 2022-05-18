
import requests


class interface_base:

    def __init__(self):
        self.seesion=requests.session()

    def method(self,url,method,para_type,data,**kwargs):
        method=method.upper()
        para_type=para_type.upper()
        if 'GET'==method:
            res=self.seesion.request(method=method,url=url,params=data)
        elif 'POST'==method:
            if 'JSON'==para_type:
                res=self.seesion.request(method=method,url=url,json=data)
            else:
                res=self.seesion.request(method=method, url=url, data=data)
        elif 'PUT'==method:
            if 'JSON'==para_type:
                res=self.seesion.request(method=method,url=url,json=data)
            else:
                res=self.seesion.request(method=method, url=url, data=data)
        elif 'DELETE'==method:
            if 'JSON'==para_type:
                res=self.seesion.request(method=method,url=url,json=data)
            else:
                res=self.seesion.request(method=method, url=url, data=data)
        else:
            raise ValueError
        return res

    def close_session(self):
        self.seesion.close()
