import allure

from Params.params import Portfolio
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert


class TestPortfolio:

    #@allure.feature：功能点的描述，可以理解成模块，相当于class级的标签
    #@allure.story：故事，可以理解为场景，相当于method级的标签  feature是story的父级，标记装饰器来标记测试，并且可以同步展示到测试报告内
    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_00(self, action):
        """
            用例描述：获我的的组合列表
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header
        api_url = req_url + urls[0]
        response = request.get_request(api_url, params[0], headers[0])
        assert test.assert_code(response['code'], 200)
        assert test.assert_in_text(response['body'],'1751')
        assert test.assert_time(response['time_consuming'], 500)
        Consts.RESULT_LIST.append('第一个True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_01(self, action):
        """
            用例描述：获取组合产品信息
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        req_url = 'https://dq.10jqka.com.cn'
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[1]
        response = request.get_request(api_url, params[1], headers[1])
        test_data=response['body']
        test_value=test_data.get('data',{}).get('chargeInfo',{}).get('goodsId',{})
        test_group=test_data.get('data',{}).get('gid',{})
        assert response['code'] == 200
        assert test.assert_text(test_value,'2022111843VJQhxYsx144939')   # 返回数据的商品id正确
        assert test.assert_time(response['time_consuming'], 500)
        Consts.RESULT_LIST.append('第二个True')
        # 记录该组合对应的群聊信息，在case10中会用到
        return test_group

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_02(self, action):
        """
            用例描述：获取主理人信息
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        req_url = 'https://dq.10jqka.com.cn'
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[2]
        response = request.get_request(api_url, params[2], headers[2])
        test_data = response['body']
        test_value = test_data.get('data', {}).get('userId', {})
        assert response['code'] == 200
        assert test.assert_text(test_value,361412857)    # 判断主理人id是否正确
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_03(self, action):
        """
            用例描述：获取投顾信息
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[3]
        response = request.get_request(api_url, params[3], headers[3])
        test_code= response['code']
        test_data = response['body']
        test_value_brokerageId = test_data.get('result', {}).get('brokerageId', {})
        test_value_brokerageName = test_data.get('result', {}).get('brokerageName', {})
        assert test.assert_code(test_code,200)
        assert test.assert_text(test_value_brokerageId,219)
        assert test.assert_text(test_value_brokerageName,'平安测试券商2')
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_04(self, action):
        """
            用例描述：获取组合持仓收益、回撤信息
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[4]
        response = request.get_request(api_url, params[4], headers[4])
        test_data=response['body']
        test_value=test_data.get('data',{}).get('createAt',{})
        assert response['code'] == 200
        assert test.assert_text(test_value,'2021-11-16')
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_05(self, action):
        """
            用例描述：组合详情页-获取组合收益走势信息
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[5]
        response = request.get_request(api_url, params[5], headers[5])
        test_data=response['body']
        test_value=test_data.get('result',{})
        assert response['code'] == 200
        assert test.assert_length_atleast(test_value,1)    # 判断返回数据条数大于等于1条
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_06(self, action):
        """
            用例描述：获取产品slogan和标签信息详细信息
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        req_url = 'https://dq.10jqka.com.cn'
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[6]
        response = request.get_request(api_url, params[6], headers[6])
        test_data = response['body']
        test_value=test_data.get('data',{}).get('labels',{})
        assert response['code'] == 200
        assert test.assert_not_text(test_value,[])   # 判断labels字段不为空
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_07(self, action):
        """
            用例描述：组合详情页-获取组合持仓分布（行业）
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[7]
        response = request.get_request(api_url, params[7], headers[7])
        test_data = response['body']
        test_value = test_data.get('data', {})
        assert response['code'] == 200
        assert test.assert_length_atleast(test_value, 1)  # 判断返回持仓数据条数大于等于1条
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_08(self, action):
        """
            用例描述：组合详情页-获取持仓/调仓展示数据
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[8]
        response = request.get_request(api_url, params[8], headers[8])
        test_data = response['body']
        test_value = test_data.get('result', {}).get('holdingCount',{})
        assert response['code'] == 200
        assert test.assert_not_text(test_value,'')     # 判断持仓不为空
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_09(self, action):
        """
            用例描述：组合详情页-判断用户是否在群里
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[9]
        response = request.get_request(api_url, params[9], headers[9])
        test_data = response['body']
        test_value = test_data.get('result', {}).get('gid', {})
        #test_member = test_data.get('result', {}).get('isMember', {})
        expected_group=self.test_portfolio_01(action)
        assert response['code'] == 200
        assert test.assert_text(test_value,expected_group)    # 判断群id是否是infos接口里返回的群id
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_10(self, action):
        """
            用例描述：组合详情页-获取组合最新的一笔调仓动态
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[10]
        response = request.get_request(api_url, params[10], headers[10])
        test_data = response['body']
        test_value = test_data.get('data', {}).get('relocateList', {})
        assert response['code'] == 200
        assert test.assert_length_atleast(test_value,1)   # 判断最新的一笔调仓请求成功
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_11(self, action):
        """
            用例描述：组合详情页-获取组合盈利概率，盈利概率没有符合条件的数据时data字段为null。这里只需要判断接口请求成功即可
        """
        conf = Config()
        data = Portfolio()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[11]
        response = request.get_request(api_url, params[11], headers[11])
        assert response['code'] == 200
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_12(self, action):
        """
            用例描述：组合详情页-获取组合收益能力，收益能力没有符合条件的数据时data字段为null。这里只需要判断接口请求成功即可
        """
        conf = Config()
        data = Portfolio()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[12]
        response = request.get_request(api_url, params[12], headers[12])
        assert response['code'] == 200
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_13(self, action):
        """
            用例描述：组合详情页-获取未订阅时群聊信息
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        req_url = 'https://dq.10jqka.com.cn'
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[13]
        response = request.get_request(api_url, params[13], headers[13])
        test_data = response['body']
        test_value = test_data.get('data', {}).get('name', {})
        assert response['code'] == 200
        #assert test.assert_text(test_value,'Z涨停平安组合付费群5941')  # 判断未订阅群聊名称一致,这是群聊的接口，需要群聊的x-user-access-token，cookie请求数据为空
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_14(self, action):
        """
            用例描述：组合详情页-获取组合历史最佳调仓列表,每次请求可能结果不一样
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[14]
        response = request.get_request(api_url, params[14], headers[14])

        assert response['code'] == 200
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_15(self, action):
        """
            用例描述：组合详情页-持仓详情页—获取组合持仓数据（投顾访问）
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[15]
        response = request.get_request(api_url, params[15], headers[15])
        test_data = response['body']
        test_value = test_data.get('result', {}).get('positions', {})
        assert response['code'] == 200
        assert test.assert_length_atleast(test_value, 0)  # 判断持仓详情
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_16(self, action):
        """
            用例描述：组合详情页-持仓详情页—获取组合持仓数据（用户访问）
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[16]
        response = request.get_request(api_url, params[16], headers[16])
        test_data = response['body']
        test_value = test_data.get('result', {}).get('positions', {})
        assert response['code'] == 200
        assert test.assert_length_atleast(test_value, 0)  # 判断持仓详情
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Portfolio')
    def test_portfolio_17(self, action):
        """
            用例描述：组合详情页-持仓详情页—获取股票的成分类别（获取股票行业板块）
        """
        conf = Config()
        data = Portfolio()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[17]
        response = request.get_request(api_url, params[17], headers[17])
        test_data = response['body']
        test_value_categoryName = test_data.get('result', {})[0].get('categoryName', {})
        test_value_stockIndustryNumber= test_data.get('result', {})[0].get('stockIndustryNumber', {})
        test_value_type = test_data.get('result', {})[0].get('type', {})
        assert response['code'] == 200
        assert test.assert_text(test_value_categoryName,'计算机应用')    # 判断30033的行业板块和行业代码
        assert test.assert_text(test_value_stockIndustryNumber,'881163')
        assert test.assert_text(test_value_type, 1)   # 1代表股票
        Consts.RESULT_LIST.append('True')
#
