from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def test_file_upload():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/upload")

    file_path = os.path.abspath("test_upload_file.txt")

    upload_input = driver.find_element(By.ID, "file-upload")
    upload_input.send_keys(file_path)

    driver.find_element(By.ID, "file-submit").click()

    result = driver.find_element(By.TAG_NAME, "h3").text
    assert result == "File Uploaded!"

    driver.quit()

