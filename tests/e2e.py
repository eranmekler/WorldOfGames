from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

def test_scores_service(app_url):
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor='http://localhost:4442/wd/hub',
        options=chrome_options
    )

    try:
        driver.get(app_url)
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "score")))
        score = int(element.text)
        sleep(2)
        driver.quit()
        return True if 1 <= score <= 1000 else False

    except Exception as ex:
        print(ex.args[0])
        driver.quit()
        return False
def main_function():
    result = test_scores_service('http://web:5000')
    if result == True:
        return 0
    else:
        return -1

if __name__ == '__main__':
    res = main_function()
    print(res)

