# coding=utf-8

import unittest
import os


def test_all():
    """获取所有测试模块"""
    suite=unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),
        pattern="test*.py",
        top_level_dir = None)  # 应该为None
    """
    1、因为unittest中规定，测试用例必须test开头，所以discover中的.pattern格式才是test*.py
    2、start_dir是存放测试用例的目录
    unittest 框架默认根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0~9，A~Z,a~z 
如果要让某个测试用例先执行，不能使用默认的main()方法，需要通过TestSuite类的addTest（）方法按照一定的顺序来加载
    """
    return suite


if __name__ == "__main__":  # 多了一个空格
    unittest.TextTestRunner(verbosity=2).run(test_all())
