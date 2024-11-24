import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(60)
    yield driver
fake = Faker()
random_email = fake.email()

email_list = []
if not (random_email in email_list):
    email_list.append(random_email)

# Test №1 Check valid email
def test_1_new_valid_email(driver):
    driver.get('https://hd.getbraavo.com/hd-gen-01-test/index.html')
    email_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[2]/input')
    email_input.click()
    email_input.send_keys(random_email)
    button_continue = driver.find_element(By.TAG_NAME, 'button')
    button_continue.click()
    page_title = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]')
    assert page_title.text == 'Your trauma Self-Healing Plan is Ready'


# Test №2 Check if verification page opens after entering existing email
def test_2_old_valid_email(driver):
    driver.get('https://hd.getbraavo.com/hd-gen-01-test/index.html')
    email_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[2]/input')
    email_input.click()
    email_input.send_keys(random_email)
    button_continue = driver.find_element(By.TAG_NAME, 'button')
    button_continue.click()
    exist_page_title = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[8]/a')
    assert exist_page_title.text == 'Use a different email'


# Test №3 Check invalid emails - without '@'
def test_3_invalid_email(driver):
    driver.get('https://hd.getbraavo.com/hd-gen-01-test/index.html')
    email_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[2]/input')
    email_input.click()
    random_valid_email = fake.email()
    invalid_email = random_valid_email.replace('@', '')
    email_input.send_keys(invalid_email)
    button_continue = driver.find_element(By.TAG_NAME, 'button')
    before_click_url = driver.current_url
    button_continue.click()
    time.sleep(1)
    after_click_url = driver.current_url
    assert before_click_url == after_click_url, f"not /registration URL: {after_click_url}"


# Test №4 Check invalid emails - without '.'
def test_4_invalid_email(driver):
    driver.get('https://hd.getbraavo.com/hd-gen-01-test/index.html')
    email_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[2]/input')
    email_input.click()
    random_valid_email = fake.email()
    invalid_email = random_valid_email.replace('.', '')
    email_input.send_keys(invalid_email)
    button_continue = driver.find_element(By.TAG_NAME, 'button')
    before_click_url = driver.current_url
    button_continue.click()
    time.sleep(1)
    after_click_url = driver.current_url
    assert before_click_url == after_click_url, f"not /registration URL: {after_click_url}"


# Test №5 Check invalid emails - with spase instead '@'
def test_5_invalid_email(driver):
    driver.get('https://hd.getbraavo.com/hd-gen-01-test/index.html')
    email_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[2]/input')
    email_input.click()
    random_valid_email = fake.email()
    invalid_email = random_valid_email.replace('@', ' ')
    email_input.send_keys(invalid_email)
    button_continue = driver.find_element(By.TAG_NAME, 'button')
    before_click_url = driver.current_url
    button_continue.click()
    time.sleep(1)
    after_click_url = driver.current_url
    assert before_click_url == after_click_url, f"not /registration URL: {after_click_url}"


# Test №6 Check invalid emails - plus additional '.' in the end
def test_6_invalid_email(driver):
    driver.get('https://hd.getbraavo.com/hd-gen-01-test/index.html')
    email_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[2]/input')
    email_input.click()
    random_valid_email = fake.email()
    invalid_email = random_valid_email + '.'
    email_input.send_keys(invalid_email)
    button_continue = driver.find_element(By.TAG_NAME, 'button')
    before_click_url = driver.current_url
    button_continue.click()
    time.sleep(1)
    after_click_url = driver.current_url
    assert before_click_url == after_click_url, f"not /registration URL: {after_click_url}"


# Test №7 Check invalid emails - with '.' in the beginning
def test_7_invalid_email(driver):
    driver.get('https://hd.getbraavo.com/hd-gen-01-test/index.html')
    email_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[2]/input')
    email_input.click()
    random_valid_email = fake.email()
    invalid_email = '.' + random_valid_email
    email_input.send_keys(invalid_email)
    button_continue = driver.find_element(By.TAG_NAME, 'button')
    before_click_url = driver.current_url
    button_continue.click()
    time.sleep(1)
    after_click_url = driver.current_url
    assert before_click_url == after_click_url, f"not /registration URL: {after_click_url}"


# Test №8 Check invalid emails - with '!'
def test_8_invalid_email(driver):
    driver.get('https://hd.getbraavo.com/hd-gen-01-test/index.html')
    email_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[2]/input')
    email_input.click()
    random_valid_email = fake.email()
    invalid_email = random_valid_email + '!'
    email_input.send_keys(invalid_email)
    button_continue = driver.find_element(By.TAG_NAME, 'button')
    before_click_url = driver.current_url
    button_continue.click()
    time.sleep(1)
    after_click_url = driver.current_url
    assert before_click_url == after_click_url, f"not /registration URL: {after_click_url}"


# Test №9 Checking the display of the timer on the page
def test_9_find_discount_timer(driver):
    new_random_email = fake.email()
    driver.get('https://hd.getbraavo.com/hd-gen-01-test/index.html')
    email_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[2]/input')
    email_input.click()
    email_input.send_keys(new_random_email)
    button_continue = driver.find_element(By.TAG_NAME, 'button')
    button_continue.click()
    discount_timer = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[1]/div[1]')
    assert discount_timer.text == 'Discount expires:'

# Test №10 Check Comparison section (2 blocks: "Now" and "Your Goal")
def test_10_comparison_section(driver):
    driver.get('https://hd.getbraavo.com/hd-gen-01-test/index.html')
    email_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[2]/input')
    email_input.click()
    random_email = fake.email()
    email_input.send_keys(random_email)
    button_continue = driver.find_element(By.TAG_NAME, 'button')
    button_continue.click()
    title_progress_container_tpc = driver.find_element(By.CSS_SELECTOR, '.title-progress-container')
    elements_in_tpc = title_progress_container_tpc.find_elements(By.TAG_NAME, 'div')
    assert len(elements_in_tpc) == 2


# Test №11 Check Comparison section (3 metrics * 2 blocks: stress level, focus level, and self-esteem level)
def test_metrics_in_section(driver):
    driver.get('https://hd.getbraavo.com/hd-gen-01-test/index.html')
    email_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[2]/input')
    email_input.click()
    random_email = fake.email()
    email_input.send_keys(random_email)
    button_continue = driver.find_element(By.TAG_NAME, 'button')
    button_continue.click()
    progress_desc_container_pdc = driver.find_element(By.CSS_SELECTOR, '.progress-description-container')
    elements_in_pdc = progress_desc_container_pdc.find_elements(By.CSS_SELECTOR, '.section-name')
    assert len(elements_in_pdc) == 6

# Check Payment Methods

# Test №12 Check 4-week subscription with 1-week trial: card Visa -valid Card Number, valid Expiry Date, valid CVV
def test_12_payments_visa(driver):
    driver.get('https://hd.getbraavo.com/hd-gen-01-test/index.html')
    email_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[2]/input')
    email_input.click()
    random_email = fake.email()
    email_input.send_keys(random_email)
    button_continue = driver.find_element(By.TAG_NAME, 'button')
    button_continue.click()
    button_subs = driver.find_element(By.XPATH, '//span[contains(text(), "GET MY PLAN")]')
    button_subs.click()
    time.sleep(3)
    iframe_block = driver.find_elements(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe_block[1])

    input_card_number = driver.find_element(By.CSS_SELECTOR, '#Field-numberInput')
    input_card_number.click()
    input_card_number.send_keys('4242424242424242')

    input_expiry_date = driver.find_element(By.CSS_SELECTOR, '#Field-expiryInput')
    input_expiry_date.click()
    input_expiry_date.send_keys('1233')

    input_cvv = driver.find_element(By.CSS_SELECTOR, '#Field-cvcInput')
    input_cvv.click()
    input_cvv.send_keys('123')

    driver.switch_to.default_content()

    btn_continue_payments = driver.find_elements(By.TAG_NAME, 'button')
    btn_continue_payments[10].click()

    success_title = driver.find_element(By.CLASS_NAME, 'success-title')
    assert success_title == (driver.find_element(By.XPATH, f"//div[contains(text(), '{'Payment Success!'}')]"))


# Test №13 Check 4-week subscription with 1-week trial:  not enough money
def test_13_payments_not_enough_money(driver):
    driver.get('https://hd.getbraavo.com/hd-gen-01-test/index.html')
    email_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[2]/input')
    email_input.click()
    random_email = fake.email()
    email_input.send_keys(random_email)
    button_continue = driver.find_element(By.TAG_NAME, 'button')
    button_continue.click()
    button_subs = driver.find_element(By.XPATH, '//span[contains(text(), "GET MY PLAN")]')
    button_subs.click()
    time.sleep(3)
    iframe_block = driver.find_elements(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe_block[1])

    input_card_number = driver.find_element(By.CSS_SELECTOR, '#Field-numberInput')
    input_card_number.click()
    input_card_number.send_keys('4000000000009995')

    input_expiry_date = driver.find_element(By.CSS_SELECTOR, '#Field-expiryInput')
    input_expiry_date.click()
    input_expiry_date.send_keys('1027')

    input_cvv = driver.find_element(By.CSS_SELECTOR, '#Field-cvcInput')
    input_cvv.click()
    input_cvv.send_keys('777')

    driver.switch_to.default_content()

    btn_continue_payments = driver.find_elements(By.TAG_NAME, 'button')
    btn_continue_payments[10].click()
    time.sleep(7)
    current_url = driver.current_url
    assert 'payment-failed' in current_url

# Test №14 Check 4-week subscription with 1-week trial: card Visa, invalid 1 or 2 signs in CVV
def test_14_payments_visa_1_sign(driver):
    driver.get('https://hd.getbraavo.com/hd-gen-01-test/index.html')
    email_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[2]/input')
    email_input.click()
    random_email = fake.email()
    email_input.send_keys(random_email)
    button_continue = driver.find_element(By.TAG_NAME, 'button')
    button_continue.click()
    button_subs = driver.find_element(By.XPATH, '//span[contains(text(), "GET MY PLAN")]')
    button_subs.click()
    time.sleep(3)
    iframe_block = driver.find_elements(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe_block[1])

    input_card_number = driver.find_element(By.CSS_SELECTOR, '#Field-numberInput')
    input_card_number.click()
    input_card_number.send_keys('4242424242424242')

    input_expiry_date = driver.find_element(By.CSS_SELECTOR, '#Field-expiryInput')
    input_expiry_date.click()
    input_expiry_date.send_keys('1027')

    input_cvv = driver.find_element(By.CSS_SELECTOR, '#Field-cvcInput')
    input_cvv.click()
    input_cvv.send_keys('5')
    input_cvv.send_keys(Keys.RETURN)
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.text_to_be_present_in_element((By.ID, 'Field-cvcError'), "Your card's security code is incomplete."))

    assert element, "Expected text not found in the element."


# Test №15 Check 4-week subscription with 1-week trial: card Visa, invalid 4 signs in CVV for VISA/Mastercard
def test_15_payments_visa_4_signs(driver):
    driver.get('https://hd.getbraavo.com/hd-gen-01-test/index.html')
    email_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/form/div[2]/input')
    email_input.click()
    random_email = fake.email()
    email_input.send_keys(random_email)
    button_continue = driver.find_element(By.TAG_NAME, 'button')
    button_continue.click()
    button_subs = driver.find_element(By.XPATH, '//span[contains(text(), "GET MY PLAN")]')
    button_subs.click()
    time.sleep(3)
    iframe_block = driver.find_elements(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe_block[1])

    input_cvv = driver.find_element(By.CSS_SELECTOR, '#Field-cvcInput')
    input_cvv.click()
    input_cvv.send_keys('1234')

    input_expiry_date = driver.find_element(By.CSS_SELECTOR, '#Field-expiryInput')
    input_expiry_date.click()
    input_expiry_date.send_keys('1027')

    input_card_number = driver.find_element(By.CSS_SELECTOR, '#Field-numberInput')
    input_card_number.click()
    input_card_number.send_keys('4242424242424242')

    current_url = driver.current_url
    input_cvv.send_keys(Keys.RETURN)
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.url_changes(current_url))
        print("URL has changed to:", driver.current_url)
    except:
        print("URL without changes:", driver.current_url)

    new_url = driver.current_url
    assert new_url == current_url, "URL has changed"