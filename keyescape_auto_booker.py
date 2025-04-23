from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains

# Set up Selenium webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()

# Load the booking page
driver.get("https://www.keyescape.co.kr/web/home.php?go=rev.make")

# Wait until the booking spot is available
wait = WebDriverWait(driver, 10)
wait_time = 0.3

########## STEP1 지점/날짜/테마 선택 ##########
time_not_avaliable = True
while time_not_avaliable == True:
    # Check if the page contains the text "죄송합니다"
    if "죄송합니다" in driver.page_source:
        # Find the element that contains the text "키이스케이프 홈페이지로 이동"
        # redirect_btn = driver.find_element(By.XPATH, "//*[contains(text(), '키이스케이프 홈페이지로 이동')]")
        redirect_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '키이스케이프 홈페이지로 이동')]")))
        # Click the element
        redirect_btn.click()

    # Select location
    time.sleep(wait_time)
    location_available = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '우주라이크')]")))
    # location_available = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div/div[4]/dl[1]/dd/div/ul/a[4]/li")))
    # Scroll to the element to make it clickable
    actions = ActionChains(driver)
    actions.move_to_element(location_available).perform()
    location_available.click()
    time.sleep(wait_time)
    # Select date
    date_available = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '28')]")))
    date_available.click()
    time.sleep(wait_time)
    # Select theme
    theme_available = None
    while theme_available is None:
        try:
            theme_available = driver.find_element(By.XPATH, f"//*[contains(text(), 'US')]")
        except:
            pass
    theme_available.click()

    time.sleep(wait_time)

    # 예약 가능 시간 아닐 시
    # Check if the page contains the text "죄송합니다"
    if "예약가능시간이 아닙니다" in driver.page_source:
        driver.refresh()
    else:
        time_not_avaliable = False

# Select time
time_available = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '09:55')]")))
time_available.click()
# Reserve button
reserve_button = driver.find_element(By.CLASS_NAME, "b")
reserve_button.click()

########## STEP2 예약정보 입력 ##########
name_input = driver.find_element(By.NAME, "name")
name_input.send_keys("홍길동")
middle_phone_number_input = driver.find_element(By.NAME, "mobile2")
middle_phone_number_input.send_keys("1234")
end_phone_number_input = driver.find_element(By.NAME, "mobile3")
end_phone_number_input.send_keys("5678")
person_btn = driver.find_element(By.NAME, "person")
person_btn.click()
person_number = driver.find_element(By.XPATH, f"//*[contains(text(), '4 명')]")
person_number.click()
agree_btn = driver.find_element(By.NAME, "ck_agree")
agree_btn.click()




# Perform any necessary actions to complete the booking, such as filling out forms, selecting options, etc.
# You'll need to inspect the elements on the website and modify the code accordingly to interact with them.

time.sleep(10000)

# Close the browser
# driver.quit()
