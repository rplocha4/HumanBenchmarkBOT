import time
from selenium import webdriver


def skip(driver):
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[3]/button").click()
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div/button").click()


def aim_trainer(driver):
    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[1]/a[3]').click()
    time.sleep(1)
    start_button = driver.find_element_by_class_name("css-1k4dpwl")
    start_button.click()

    for i in range(30):
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div/div/div/div[5]').click()


def reaction_time(driver):
    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[1]/a[1]').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]').click()
    element = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]')

    while True:
        if element.get_attribute('class').split(' ')[0] == 'view-go':
            element.click()
            element.click()


def typing(driver):
    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[3]/a[2]').click()
    text = driver.find_elements_by_css_selector('.letters span')
    letters = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div')
    keys = []

    for letter in text:
        if letter.text == '':
            keys.append(' ')
        else:
            keys.append(letter.text)

    for i in range(len(keys)):
        letters.send_keys(keys[i])


def verbal_memory(driver, points):
    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[2]/a[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[4]/button').click()
    words = [driver.find_elements_by_class_name('word')[0].text]

    new_button = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[2]')
    seen_button = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[1]')
    new_button.click()

    for i in range(int(points)):
        word = driver.find_elements_by_class_name('word')[0].text
        if word in words:
            seen_button.click()
        else:
            words.append(word)
            new_button.click()


def number_memory(driver, points):
    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[2]/a[1]').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button').click()
    delay = 3

    for i in range(int(points)):
        number = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[1]').text
        time.sleep(delay)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[2]/input').send_keys(
            number)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[3]/button').click()
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/button').click()
        delay += 1


def chimp_test(driver):
    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[2]/a[3]').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]/button').click()

    for i in range(38):
        elements = driver.find_elements_by_css_selector('.css-gmuwbf .css-19b5rdt')
        elements.sort(key=lambda x: int(x.text), reverse=False)

        for element in elements:
            element.click()
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[3]/button').click()


def visual_memory(driver, points):
    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/div[3]/a[1]').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/button').click()
    time.sleep(0.5)
    el = driver.find_elements_by_css_selector('.css-hvbk5q .active')

    for i in range(int(points)):
        time.sleep(2)
        for e in el:
            e.click()
        time.sleep(2)
        el = driver.find_elements_by_css_selector('.css-hvbk5q .active')


def open_site():
    chrome_driver = "D:\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver)
    driver.get("https://humanbenchmark.com/")
    skip(driver)
    return driver


if __name__ == "__main__":
    choice = input("Choose game:\n1.Typing\n2.Visual Memory\n3.Number Memory\n4.Verbal Memory\n5.Chimp Test\n"
                   "6.Aim Trainer\n7.Reaction Time\n")
    if choice == "1":
        driver = open_site()
        typing(driver)
    elif choice == "2":
        points = input("How much points would you like?")
        driver = open_site()
        visual_memory(driver, points)
    elif choice == "3":
        points = input("How much points would you like?")
        driver = open_site()
        number_memory(driver, points)
    elif choice == "4":
        points = input("How much points would you like?")
        driver = open_site()
        verbal_memory(driver, points)
    elif choice == "5":
        driver = open_site()
        chimp_test(driver)
    elif choice == "6":
        driver = open_site()
        aim_trainer(driver)
    elif choice == "7":
        driver = open_site()
        reaction_time(driver)
    else:
        print("Wrong choice")

