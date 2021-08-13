from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/playlist?list=PLOltJHdid0ZWau4Fcl31o1AElKBYJRpcs')
driver.find_element_by_xpath('//*[@id="video-title"]').click()

