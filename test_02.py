# coding=utf-8

import unittest
from test_apple import InitTest


class SinaTest(InitTest):


    def test_baidu_news(self):
        '"验证：测试百度首页点击新闻后的跳转"'
        self.driver.find_element_by_link_text("新闻").click()
        self.driver.get("http://www.baidu.com")


    def test_baidu_map(self):
        '"验证：测试百度首页点击地图后的跳转"'
        self.driver.find_element_by_link_text("地图").click()
        self.driver.get("http://www.baidu.com")


if __name__ == "__main__":

    suite = unittest.TestSuite()

    suite.addTest(SinaTest("test_baidu_news"))
    suite.addTest(SinaTest("test_baidu_map"))
    unittest.TextTestRunner(verbosity=2).run(suite)