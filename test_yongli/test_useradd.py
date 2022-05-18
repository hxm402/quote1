import pytest
import requests

from quote.base.iterface_base import interface_base
from quote.opretion.opyaml import read_yaml


class Test_useradd:

    def setup(self):
        self.client=interface_base()

    def teardown(self):
        pass
    #tianjianyonghuchenggong
    @pytest.mark.parametrize('useradddata',read_yaml("../config/useradd.yaml"))
    def test_useraddsuccess(self,useradddata):
        url = useradddata['url']
        method = useradddata['method']
        para_type = useradddata['para_type']
        data = useradddata['data']
        except_result=useradddata['except']
        res = self.client.method(url=url,method=method,para_type=para_type,data=data)
        actual_result=res.json()['message']
        assert except_result==actual_result
        print(res.json())
