import pdfkit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

USERNAME = "YOUR username"
PASSWORD = "Your password"
LOGIN_URL = "http://online-tests.aceenggacademy.com/logins/aceLogin.jsp"
chrome_path = r"C:\Users\BLUE\PycharmProjects\madeeasy\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_path)
browser.get(LOGIN_URL)
username = browser.find_element_by_name("icoreiEduuser")
password = browser.find_element_by_name("icoreiEdupass")
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
browser.switch_to.window(browser.window_handles[0])
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()
try:
    WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(text(),'Progressing')]")))
    print("Home Page is ready!")
except TimeoutException:
    print("Home Page Loading took too much time!")
html = ""
unattempted = browser.find_element_by_xpath("//div[contains(text(),'Progressing')]")
unattempted.click()
tests = browser.find_elements_by_xpath("//a[contains(text(),'Progressing')]")
for index in range(len(tests)) :
    browser.switch_to.window(browser.window_handles[0])
    test = tests[index]
    print(index+1)
    html = test.get_attribute("outerHTML")
    html = html[205:209]
    test_url = "http://online-tests.aceenggacademy.com/liveTest.jhtm?type=startTest&tcId=" + html + "&tId=" + html + "&qoId=1"
    test_url = "'" + test_url + "'"
    script = "window.open(" + test_url + ",'_blank');"
    print(test_url)
    browser.execute_script(script)
    browser.switch_to.window(browser.window_handles[1])
    print(browser.current_url)
    try:
        WebDriverWait(browser, 30).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='psgId']")))
        print("Test Page is ready!")
    except TimeoutException:
        print("Test Page Loading took too much time!")
    submit_button= browser.find_element_by_xpath("//button[contains(text(),'Submit Test')]")
    test_title = browser.find_element_by_xpath('//div[@id="testTitle"]')
    test_title_string = test_title.text
    test_title_string = test_title_string.strip()
    test_title_string = test_title_string.replace("/", "").replace("-", "").replace("(", "").replace(")", "").replace(
        ":", "").replace("���","")
    test_title_string = "ACE" + test_title_string + ".pdf"
    print(test_title_string)

    browser.close()
browser.switch_to.window(browser.window_handles[0])





try:
    WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(text(),'Un Attempted')]")))
    print("Home Page is ready!")
except TimeoutException:
    print("Home Page Loading took too much time!")
html = ""
unattempted = browser.find_element_by_xpath("//div[contains(text(),'Un Attempted')]")
unattempted.click()
tests = browser.find_elements_by_xpath("//a[contains(text(),'UnAttempted')]")
for index in range(len(tests)) :
    browser.switch_to.window(browser.window_handles[0])
    test = tests[index]
    print(index+1)
    html = test.get_attribute("outerHTML")
    html = html[201:205]
    test_url = "http://online-tests.aceenggacademy.com/liveTest.jhtm?type=startTest&tcId=" + html + "&tId=" + html + "&qoId=1"
    test_url = "'" + test_url + "'"
    script = "window.open(" + test_url + ",'_blank');"
    print(test_url)
    browser.execute_script(script)
    browser.switch_to.window(browser.window_handles[1])
    print(browser.current_url)
    try:
        WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='psgId']")))
        print("Test Page is ready!")
    except TimeoutException:
        print("Test Page Loading took too much time!")
    view_button = browser.find_element_by_xpath("//button[@id='viewQPButton']")
    view_button.click()
    FullQuestionPaper = browser.find_element_by_xpath("//div[@id='questionPaperFullViewBlock']")
    pdf_string = FullQuestionPaper.get_attribute("outerHTML")
    test_title = browser.find_element_by_xpath('//div[@id="testTitle"]')
    test_title_string = test_title.text
    test_title_string = test_title_string.strip()
    test_title_string = test_title_string.replace("/", "").replace("-", "").replace("(", "").replace(")", "").replace(
        ":", "").replace("���","")
    test_title_string = "ACE" + test_title_string + ".pdf"
    print(test_title_string)
    pdfkit.from_string(pdf_string, test_title_string)
    browser.close()
















