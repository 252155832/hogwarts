class Testcalc:
    def test_add(self,get_calc,add_datas):
        result = get_calc.add(add_datas[0], add_datas[1])
        assert add_datas[2] == result
    def test_sub(self,get_calc,sub_datas):
        result = get_calc.sub(sub_datas[0],sub_datas[1])
        if isinstance(result,float):
            result = round(result,2)
        assert sub_datas[2] == result
    def test_mul(self,get_calc,mul_datas,):
        result = get_calc.mul(mul_datas[0],mul_datas[1])
        if isinstance(result,float):
            result = round(result,2)
        assert mul_datas[2] == result
    def check_div(self,get_calc,div_datas):
        result = get_calc.div(div_datas[0],div_datas[1])
        assert div_datas[2] == result