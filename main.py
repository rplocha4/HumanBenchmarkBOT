import time
from selenium import webdriver

chrome_driver = "D:\chromedriver\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver)


driver.get("https://humanbenchmark.com/")

time.sleep(2)
try:
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div/button").click()
except:
    pass

########################## AIM TRAINER ##################################################

# driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[1]/a[3]').click()
#
# time.sleep(2)
#
# start_button = driver.find_element_by_class_name("css-1k4dpwl")
#
#
# start_button.click()
# for i in range(30):
#     driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div/div/div/div[5]').click()

########################## AIM TRAINER ##################################################


########################## REACTION TIME ##################################################

# driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[1]/a[1]').click()
#
# driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]').click()
#
# element = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]')
# while True:
#     if element.get_attribute('class').split(' ')[0] == 'view-go':
#         element.click()
#         element.click()

########################## REACTION TIME ##################################################


########################## TYPING ##################################################

# driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[3]/a[2]').click()
# text = driver.find_elements_by_css_selector('.letters span')
# letters = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div')
#
# keys = []
#
# for letter in text:
#     if letter.text == '':
#         keys.append(' ')
#     else:
#         keys.append(letter.text)
#
#
# for i in range(len(keys)):
#     letters.send_keys(keys[i])

########################## TYPING ##################################################


########################## VERBAL MEMORY ##################################################

# driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[2]/a[2]').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[4]/button').click()
# words = [driver.find_elements_by_class_name('word')[0].text]
#
# new_button = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[2]')
# seen_button = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[1]')
# new_button.click()
#
# for i in range(5000):
#     word = driver.find_elements_by_class_name('word')[0].text
#     if word in words:
#         seen_button.click()
#     else:
#         words.append(word)
#         new_button.click()

########################## VERBAL MEMORY ##################################################


########################## NUMBER MEMORY ##################################################

# driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[2]/a[1]').click()
# driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button').click()
#
# delay = 3
# for i in range(30):
#     number = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[1]').text
#     time.sleep(delay)
#     driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[2]/input').send_keys(number)
#     driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[3]/button').click()
#     driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/button').click()
#     delay += 1

########################## NUMBER MEMORY ##################################################


########################## CHIMP TEST ##################################################

# driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[2]/a[3]').click()
# driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]/button').click()
#
#
# for i in range(38):
#     elements = driver.find_elements_by_css_selector('.css-gmuwbf .css-19b5rdt')
#
#     elements.sort(key=lambda x: int(x.text), reverse=False)
#
#     for element in elements:
#         element.click()
#     driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[3]/button').click()

########################## CHIMP TEST ##################################################


########################## VISUAL MEMORY ##################################################

# driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[3]/a[1]').click()
# driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/button').click()
# time.sleep(0.5)
# el = driver.find_elements_by_css_selector('.css-hvbk5q .active')
#
# for i in range(50):
#     time.sleep(2)
#     for e in el:
#         e.click()
#     time.sleep(2)
#     el = driver.find_elements_by_css_selector('.css-hvbk5q .active')

########################## VISUAL MEMORY ##################################################





