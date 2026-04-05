from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def test_google():
    print("Auto trigger test")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()