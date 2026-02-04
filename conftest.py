import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture
def driver():
    driver = webdriver.Safari()
    driver.set_window_size(1280, 800)
    yield driver
    driver.quit()

@pytest.fixture
def go_to_elements_text_box(driver):
    driver.get("https://demoqa.com")
    wait = WebDriverWait(driver, 10)

    elements_card = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
    elements_card.click()

    text_box_item = wait.until(EC.element_to_be_clickable((By.ID, "item-0")))
    text_box_item.click()

    return driver

@pytest.fixture
def go_to_elements_check_box(driver):
    driver.get("https://demoqa.com")
    wait = WebDriverWait(driver, 10)

    elements_card = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
    elements_card.click()

    text_box_item = wait.until(EC.element_to_be_clickable((By.ID, "item-1")))
    text_box_item.click()

    return driver

@pytest.fixture
def go_to_elements_radio_button(driver):
    driver.get("https://demoqa.com")
    wait = WebDriverWait(driver, 10)

    elements_card = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
    elements_card.click()

    text_box_item = wait.until(EC.element_to_be_clickable((By.ID, "item-2")))
    text_box_item.click()

    return driver

@pytest.fixture
def go_to_elements_web_tables(driver):
    driver.get("https://demoqa.com")
    wait = WebDriverWait(driver, 10)

    elements_card = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
    elements_card.click()

    text_box_item = wait.until(EC.element_to_be_clickable((By.ID, "item-3")))
    text_box_item.click()

    return driver

@pytest.fixture
def go_to_elements_links(driver):
    driver.get("https://demoqa.com")
    wait = WebDriverWait(driver, 10)

    elements_card = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
    elements_card.click()

    text_box_item = wait.until(EC.element_to_be_clickable((By.ID, "item-5")))
    text_box_item.click()

    return driver

@pytest.fixture
def go_to_elements_broken_images(driver):
    driver.get("https://demoqa.com")
    wait = WebDriverWait(driver, 10)

    elements_card = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
    elements_card.click()

    text_box_item = wait.until(EC.element_to_be_clickable((By.ID, "item-6")))
    text_box_item.click()

    return driver

@pytest.fixture
def go_to_elements_dynamic_prop(driver):
    driver.get("https://demoqa.com")
    wait = WebDriverWait(driver, 30)

    elements_card = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']"))
    )
    elements_card.click()

    # Wait for left sidebar to appear
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "element-list")))

    dynamic_prop_item = wait.until(
        EC.element_to_be_clickable((By.ID, "item-8"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", dynamic_prop_item)
    wait.until(EC.element_to_be_clickable((By.ID, "item-8")))
    dynamic_prop_item.click()

    return driver

@pytest.fixture
def go_to_forms_box(driver):
    driver.get("https://demoqa.com")
    wait = WebDriverWait(driver, 10)

    form_card = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Forms']")))
    form_card.click()

    # Wait for left sidebar to appear
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "element-list")))

    form_box_item = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Practice Form']")))
    form_box_item.click()

    return driver

@pytest.fixture
def go_to_alerts_frame_windows(driver):
    driver.get("https://demoqa.com")
    wait = WebDriverWait(driver, 10)

    card = wait.until(EC.presence_of_element_located((By.XPATH, "//h5[text()='Alerts, Frame & Windows']")))

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
    driver.execute_script("arguments[0].click();", card)

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "element-list")))

    browser_windows = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Browser Windows']")))

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", browser_windows)
    browser_windows.click()

    return driver

@pytest.fixture
def go_to_alerts(driver):
    driver.get("https://demoqa.com")
    wait = WebDriverWait(driver, 10)

    card = wait.until(EC.presence_of_element_located((By.XPATH, "//h5[text()='Alerts, Frame & Windows']")))

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
    driver.execute_script("arguments[0].click();", card)

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "element-list")))

    browser_windows = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Alerts']")))

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", browser_windows)
    browser_windows.click()

    return driver

@pytest.fixture
def go_to_frames(driver):
    driver.get("https://demoqa.com")
    wait = WebDriverWait(driver, 10)

    card = wait.until(EC.presence_of_element_located((By.XPATH, "//h5[text()='Alerts, Frame & Windows']")))

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
    driver.execute_script("arguments[0].click();", card)

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "element-list")))

    browser_windows = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Frames']")))

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", browser_windows)
    browser_windows.click()

    return driver