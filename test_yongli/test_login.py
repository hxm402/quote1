import pytest
import requests

from quote.base.iterface_base import interface_base
from quote.opretion.opyaml import read_yaml


class Test_login:

    def setup_class(self):
        self.client=interface_base()

    def teardown_class(self):
        pass


    @pytest.mark.parametrize('udata',read_yaml('../config/login.yaml'))
    def test_01(self,udata):
        url=udata['url']
        para_type =udata['para_type']
        method=udata['method']
        data=udata['data']
        except_result=udata['except']
        res=self.client.method(url=url,method=method,para_type=para_type,data=data)
        actual_result=res.json()['message']
        assert except_result==actual_result
        print(res.json())
