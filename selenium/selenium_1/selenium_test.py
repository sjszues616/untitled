from selenium import webdriver

driver = webdriver.Chrome()
url = 'http://www.baidu.com'
driver.get(url)


element = driver.find_element_by_id('kw')
element.send_keys('曾大饼是大傻瓜')
driver.find_element_by_id('su').click()

# # 关闭当前页
# driver.close()
# #关闭浏览器
# driver.quit()