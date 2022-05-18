import os

import pytest

if __name__ == '__main__':
    pytest.main(['-sv','--alluredir','../alure-result'])
    os.system('allure generate ../alure-result -o ../reports')
