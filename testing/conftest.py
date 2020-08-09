import pytest
import yaml

from testing.calc import Calculator
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

with open('./calc.yml',encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    adddatas = datas['add']['datas']
    addid = datas['add']['myid']
    subdatas = datas['sub']['datas']
    subid = datas['sub']['myid']
    muldatas = datas['mul']['datas']
    mulid = datas['mul']['myid']
    divdatas = datas['div']['datas']
    divid = datas['div']['myid']
@pytest.fixture(params=adddatas,ids=addid)
def add_datas(request):
    data = request.param
    return data
@pytest.fixture(params=subdatas,ids=subid)
def sub_datas(request):
    data = request.param
    return data
@pytest.fixture(params=muldatas,ids=mulid)
def mul_datas(request):
    data = request.param
    return data
@pytest.fixture(params=divdatas,ids=divid)
def div_datas(request):
    data = request.param
    return data

@pytest.fixture(scope='class')
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("计算结束")