# coding=utf-8

import unittest
from test_apple  import InitTest


class BaiduTest(InitTest):


    def test_002(self):
        """验证：点击百度也新闻"""
        self.driver.find_element_by_link_text("新闻").click()
        self.assertEqual(self.driver.current_url,"http://www.baidu.com/")
    def test_baidu_map(self):
        '"验证：测试百度首页点击地图后的跳转"'
        self.driver.find_element_by_link_text("地图").click()
        self.assertEqual(self.driver.current_url, "http://www.baidu.com/")


if __name__ == "__main__":
    unittest.main(verbosity=2)
