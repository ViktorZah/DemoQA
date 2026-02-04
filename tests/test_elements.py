from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait ,Select
from selenium.webdriver.support import expected_conditions as EC
import pytest
import requests
import time

@pytest.mark.forms
def test_user_name(go_to_elements_text_box):
    driver = go_to_elements_text_box
    wait = WebDriverWait(driver, 10)

    name_field = wait.until(EC.visibility_of_element_located((By.ID,"userName")))
    driver.execute_script("arguments[0].scrollIntoView();",name_field)
    name_field.send_keys("Viktor Z")
    assert name_field.get_attribute("value") == "Viktor Z"

@pytest.mark.forms
def test_user_email(go_to_elements_text_box):
    driver = go_to_elements_text_box
    wait = WebDriverWait(driver, 10)
    field = wait.until(EC.visibility_of_element_located((By.ID,"userEmail")))
    driver.execute_script("arguments[0].scrollIntoView();",field)
    field.send_keys("Viktor@gmail.com")
    assert field.get_attribute("value") == "Viktor@gmail.com"

@pytest.mark.forms
def test_user_address(go_to_elements_text_box):
    driver = go_to_elements_text_box
    wait = WebDriverWait(driver, 10)

    current_address = wait.until(EC.visibility_of_element_located((By.ID,"currentAddress")))
    driver.execute_script("arguments[0].scrollIntoView();",current_address)
    current_address.send_keys("bat-yam")
    assert current_address.get_attribute("value") == "bat-yam"

@pytest.mark.forms
def test_user_permaddress(go_to_elements_text_box):
    driver = go_to_elements_text_box
    wait = WebDriverWait(driver, 10)

    perm_address = wait.until(EC.visibility_of_element_located((By.ID,"permanentAddress")))
    driver.execute_script("arguments[0].scrollIntoView();",perm_address)
    perm_address.send_keys("bat-yam")
    assert perm_address.get_attribute("value") == "bat-yam"

@pytest.mark.checkBox
def test_check_box(go_to_elements_check_box):
    driver = go_to_elements_check_box
    wait = WebDriverWait(driver, 10)

    checkMark = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='tree-node-home'] span.rct-checkbox")))
    checkMark.click()

    checkClicked = driver.find_element(By.ID, "tree-node-home")
    assert checkClicked.is_selected()

    message = driver.find_element(By.ID,"result")
    assert message.is_displayed()
    assert "You have selected :" in message.text
    assert "home" in message.text

@pytest.mark.checkBox
def test_expanded(go_to_elements_check_box):
    driver = go_to_elements_check_box
    wait = WebDriverWait(driver, 10)

    expand_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.rct-collapse")))
    expand_button.click()
    
@pytest.mark.checkBox
def test_expanded_mark(go_to_elements_check_box):
    driver = go_to_elements_check_box
    wait = WebDriverWait(driver, 10)

    expand_home = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Toggle']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", expand_home)
    driver.execute_script("arguments[0].click();", expand_home)

    desktop = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='Desktop']")))
    assert desktop.is_displayed()

    documents = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='Documents']")))
    assert documents.is_displayed()

    downloads = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='Downloads']")))
    assert downloads.is_displayed()


@pytest.mark.radioButton
def test_circle_press_yes(go_to_elements_radio_button):
    driver = go_to_elements_radio_button
    wait = WebDriverWait(driver, 10)

    yes_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='yesRadio']")))
    yes_label.click()

    yes_input = driver.find_element(By.ID, "yesRadio")
    assert yes_input.is_selected()

    message = driver.find_element(By.CLASS_NAME,"mt-3")
    message2 = driver.find_element(By.CLASS_NAME,"text-success")
    assert message.is_displayed()
    assert message2.is_displayed()
    assert "You have selected " in message.text
    assert "Yes" in message2.text

@pytest.mark.radioButton
def test_circle_press_impressive(go_to_elements_radio_button):
    driver = go_to_elements_radio_button
    wait = WebDriverWait(driver, 10)

    yes_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='impressiveRadio']")))
    yes_label.click()

    impressive_input = driver.find_element(By.ID, "impressiveRadio")
    assert impressive_input.is_selected()

    message = driver.find_element(By.CLASS_NAME,"mt-3")
    message2 = driver.find_element(By.CLASS_NAME,"text-success")
    assert message.is_displayed()
    assert message2.is_displayed()
    assert "You have selected " in message.text
    assert "Impressive" in message2.text

@pytest.mark.webTables
def test_webTable_add(go_to_elements_web_tables):
    driver = go_to_elements_web_tables
    wait = WebDriverWait(driver, 10)

    addBtn = wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton")))
    addBtn.click()

    first_name_input = wait.until(EC.visibility_of_element_located((By.ID, "firstName")))
    assert first_name_input.is_displayed()
    assert driver.find_element(By.ID, "lastName").is_displayed()
    assert driver.find_element(By.ID, "userEmail").is_displayed()

    driver.find_element(By.ID, "firstName").send_keys("John")
    driver.find_element(By.ID, "lastName").send_keys("Doe")
    driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "age").send_keys("30")
    driver.find_element(By.ID, "salary").send_keys("50000")
    driver.find_element(By.ID, "department").send_keys("Engineering")

    driver.find_element(By.ID, "submit").click()

    table = driver.find_element(By.CLASS_NAME, "rt-table")
    assert "John" in table.text
    assert "Doe" in table.text

@pytest.mark.webTables
def test_webTable_del(go_to_elements_web_tables):
    driver = go_to_elements_web_tables

    rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    assert len(rows) > 0

    target_row = None
    for r in rows:
        if r.text.strip():
            target_row = r
            break
    assert target_row is not None

    row_text = target_row.text
    first_word = row_text.split()[0]

    delete_btn = target_row.find_element(By.CSS_SELECTOR, "span[title='Delete']")
    delete_btn.click()

    table = driver.find_element(By.CLASS_NAME, "rt-table")
    assert first_word not in table.text

@pytest.mark.webTables
def test_webTable_edit(go_to_elements_web_tables):
    driver = go_to_elements_web_tables
    wait = WebDriverWait(driver, 10)

    rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    assert len(rows) > 0

    target_row = None
    for r in rows:
        if r.text.strip():
            target_row = r
            break
    assert target_row is not None

    edit_btn = target_row.find_element(By.CSS_SELECTOR, "span[title='Edit']")
    edit_btn.click()

    first_name = wait.until(EC.visibility_of_element_located((By.ID, "firstName")))
    first_name.clear()

    driver.find_element(By.ID, "firstName").send_keys("Alex")
    driver.find_element(By.ID, "submit").click()

    table = driver.find_element(By.CLASS_NAME, "rt-table")
    assert "Alex" in table.text

@pytest.mark.links
def test_reg_link(go_to_elements_links):
    driver = go_to_elements_links

    link = driver.find_element(By.ID, "simpleLink")
    link.click()

    driver.switch_to.window(driver.window_handles[-1])

    assert "demoqa.com" in driver.current_url

@pytest.mark.links
def test_api_link(go_to_elements_links):
    driver = go_to_elements_links
    wait = WebDriverWait(driver, 10)

    created_link = wait.until(EC.element_to_be_clickable((By.ID, "created")))

    driver.execute_script("arguments[0].scrollIntoView(true);", created_link)

    created_link.click()

    response_elem = wait.until(EC.visibility_of_element_located((By.ID, "linkResponse")))

    response = response_elem.text

    assert "201" in response
    assert "Created" in response

@pytest.mark.images
def test_broken_images(go_to_elements_broken_images):
    driver = go_to_elements_broken_images
    images = driver.find_elements(By.TAG_NAME, "img")

    broken_images = []
    for img in images:
        if driver.execute_script("return arguments[0].naturalWidth;", img) == 0:
            broken_images.append(img)

    assert len(broken_images) >= 1

@pytest.mark.images
def test_at_least_one_valid_image(go_to_elements_broken_images):
    driver = go_to_elements_broken_images
    images = driver.find_elements(By.TAG_NAME, "img")

    valid_images = [img for img in images if driver.execute_script("return arguments[0].naturalWidth;", img) > 0 ]

    assert len(valid_images) >= 1

@pytest.mark.images
def test_valid_image_links(go_to_elements_broken_images):
    driver = go_to_elements_broken_images
    images = driver.find_elements(By.TAG_NAME, "img")

    valid_images = [
        img.get_attribute("src") for img in images
        if driver.execute_script("return arguments[0].naturalWidth;", img) > 0
    ]

    for src in valid_images:
        response = requests.get(src)
        assert response.status_code == 200, f"Valid image link broken: {src}"

@pytest.mark.images
def test_broken_image_links(go_to_elements_broken_images):
    driver = go_to_elements_broken_images
    images = driver.find_elements(By.TAG_NAME, "img")

    broken_images = [
        img.get_attribute("src")
        for img in images
        if driver.execute_script("return arguments[0].naturalWidth;", img) == 0]

    assert len(broken_images) >= 1

@pytest.mark.dynamicProp
def test_dynamic_prop(go_to_elements_dynamic_prop):
    driver = go_to_elements_dynamic_prop
    wait = WebDriverWait(driver, 10)

    color_btn = driver.find_element(By.ID, "colorChange")
    initial_color = color_btn.value_of_css_property("color")
    
    timerKey = wait.until(EC.visibility_of_element_located((By.ID, "visibleAfter")))
    assert timerKey.is_displayed()

    enable_btn = driver.find_element(By.ID, "enableAfter")
    assert enable_btn.is_enabled()

    wait.until(lambda d: color_btn.value_of_css_property("color") != initial_color)
    new_color = color_btn.value_of_css_property("color")
    assert initial_color != new_color


@pytest.mark.formsBox
def test_forms_box(go_to_forms_box):
    driver = go_to_forms_box
    wait = WebDriverWait(driver, 10)

    head = driver.find_element(By.XPATH, "//h5[text()='Student Registration Form']")
    assert head.is_displayed()

    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("Alex")

    assert first_name.get_attribute("value") == "Alex"

    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Zz")

    assert last_name.get_attribute("value") == "Zz"

    user_email = driver.find_element(By.ID, "userEmail")
    user_email.send_keys("Zz@gmail.com")

    assert user_email.get_attribute("value") == "Zz@gmail.com"

    gender_label = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
    gender_label.click()

    gender_input = driver.find_element(By.ID, "gender-radio-1")
    assert gender_input.is_selected()
    
    phone = driver.find_element(By.ID, "userNumber")
    phone.send_keys("0501234567")
    assert phone.get_attribute("value") == "0501234567"

    date = wait.until(EC.element_to_be_clickable((By.ID, "dateOfBirthInput")))
    date.click()

    date_picker = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker")))
    assert date_picker.is_displayed()

    year_select = Select(wait.until(EC.presence_of_element_located((By.CLASS_NAME, "react-datepicker__year-select"))))
    year_select.select_by_visible_text("1995")
    assert year_select.first_selected_option.text == "1995"

    month_select = Select(wait.until(EC.presence_of_element_located((By.CLASS_NAME, "react-datepicker__month-select"))))
    month_select.select_by_visible_text("May")
    assert month_select.first_selected_option.text == "May"

    day = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,
         "//div[contains(@class,'react-datepicker__day') "
         "and not(contains(@class,'react-datepicker__day--outside-month')) "
         "and text()='15']")))

    day.click()
    assert date.get_attribute("value") == "15 May 1995"

    submit_btn = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    driver.execute_script("arguments[0].click();", submit_btn)

    modal_title = wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
    assert modal_title.text == "Thanks for submitting the form"


    modal_body = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-body")))
    assert "Alex Zz" in modal_body.text
    assert "Zz@gmail.com" in modal_body.text
    assert "Male" in modal_body.text
    assert "15 May,1995" in modal_body.text
    assert "0501234567" in modal_body.text

@pytest.mark.browserWindows
def test_new_tab(go_to_alerts_frame_windows):
    driver = go_to_alerts_frame_windows
    wait = WebDriverWait(driver, 10)

    original_window = driver.current_window_handle
    assert len(driver.window_handles) == 1

    new_tab_btn = wait.until(EC.element_to_be_clickable((By.ID, "tabButton")))
    new_tab_btn.click()

    wait.until(lambda d: len(d.window_handles) == 2)

    new_window = [w for w in driver.window_handles if w != original_window][0]
    driver.switch_to.window(new_window)

    text = wait.until(EC.visibility_of_element_located((By.ID, "sampleHeading")))
    assert text.text == "This is a sample page"

@pytest.mark.browserWindows
def test_new_window(go_to_alerts_frame_windows):
    driver = go_to_alerts_frame_windows
    wait = WebDriverWait(driver, 10)

    original_window = driver.current_window_handle

    window_btn = wait.until(EC.element_to_be_clickable((By.ID, "windowButton")))
    window_btn.click()

    wait.until(lambda d: len(d.window_handles) == 2)

    new_window = [w for w in driver.window_handles if w != original_window][0]
    driver.switch_to.window(new_window)

    heading = wait.until(EC.visibility_of_element_located((By.ID, "sampleHeading")))
    assert heading.text == "This is a sample page"
    
@pytest.mark.browserWindows
def test_new_window_message(go_to_alerts_frame_windows):
    driver = go_to_alerts_frame_windows
    wait = WebDriverWait(driver, 10)

    original_window = driver.current_window_handle

    msg_btn = wait.until(EC.element_to_be_clickable((By.ID, "messageWindowButton")))
    msg_btn.click()

    wait.until(lambda d: len(d.window_handles) == 2)

    new_window = [w for w in driver.window_handles if w != original_window][0]
    driver.switch_to.window(new_window)

    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Knowledge increases by sharing" in body_text

@pytest.mark.alerts
def test_alerts(go_to_alerts):
    driver = go_to_alerts
    wait = WebDriverWait(driver, 10)

    simple_alert_btn = wait.until(EC.element_to_be_clickable((By.ID, "alertButton")))
    simple_alert_btn.click()

    alert = driver.switch_to.alert
    assert alert.text == "You clicked a button"
    alert.accept()

@pytest.mark.alerts
def test_alert_5(go_to_alerts):
    driver = go_to_alerts
    wait = WebDriverWait(driver, 10)

    timer_alert_btn = driver.find_element(By.ID, "timerAlertButton")
    timer_alert_btn.click()

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert "5 seconds" in alert.text
    alert.accept()

@pytest.mark.alerts
def test_alerts_confirm(go_to_alerts):
    driver = go_to_alerts

    confirm_btn = driver.find_element(By.ID, "confirmButton")
    confirm_btn.click()

    alert = driver.switch_to.alert
    assert alert.text == "Do you confirm action?"
    alert.accept()

    confirm_result = driver.find_element(By.ID, "confirmResult")
    assert "Ok" in confirm_result.text

@pytest.mark.alerts
def test_alerts_name(go_to_alerts):
    driver = go_to_alerts
    wait = WebDriverWait(driver, 10)

    prompt_btn = driver.find_element(By.ID, "promtButton")
    prompt_btn.click()

    alert = driver.switch_to.alert
    alert.send_keys("Alex")
    alert.accept()

    prompt_result = driver.find_element(By.ID, "promptResult")
    assert "Alex" in prompt_result.text

@pytest.mark.frames
def test_frames(go_to_frames):
    driver = go_to_frames
    wait = WebDriverWait(driver, 10)

    #Frame 1
    frame1 = wait.until(
        EC.presence_of_element_located((By.ID, "frame1"))
    )
    driver.switch_to.frame(frame1)

    frame1_text = wait.until(
        EC.visibility_of_element_located((By.ID, "sampleHeading"))
    )
    assert frame1_text.text == "This is a sample page"
    driver.switch_to.default_content()

    #Frame 2
    frame2 = wait.until(
        EC.presence_of_element_located((By.ID, "frame2"))
    )
    driver.switch_to.frame(frame2)

    frame2_text = wait.until(
        EC.visibility_of_element_located((By.ID, "sampleHeading"))
    )
    assert frame2_text.text == "This is a sample page"

    driver.switch_to.default_content()