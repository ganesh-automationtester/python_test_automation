class Test_Allure:

    def test_pass(self):
        assert True
        print('Test passed')

    def test_fail(self):
        print('Test failed')
        assert False