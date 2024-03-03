from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service
# Create a Service object with the path to the Chrome WebDriver executable
service = Service("C:\\browser driver\\chromedriver.exe")

# Create an instance of Chrome WebDriver, passing the Service object
driver = webdriver.Chrome(service=service)

# Open the currency converter web page
driver.get("http://localhost:5000")

# Wait for the page title to contain "Currency Converter"
WebDriverWait(driver, 10).until(EC.title_contains("Currency Converter"))

# Test data
amount_value = "50"
from_currency_value = "USD"
to_currency_value = "EUR"

# Wait for the amount input field to be visible
amount_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "amount")))
amount_input.send_keys(amount_value)

# Wait for the source currency dropdown to be visible
from_currency_dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "from_currency")))
from_currency_dropdown.click()

# Select the source currency from the dropdown
from_currency_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//select[@id='from_currency']/option[@value='{from_currency_value}']")))
from_currency_option.click()

# Wait for the target currency dropdown to be visible
to_currency_dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "to_currency")))
to_currency_dropdown.click()

# Select the target currency from the dropdown
to_currency_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//select[@id='to_currency']/option[@value='{to_currency_value}']")))
to_currency_option.click()

# Wait for the convert button to be clickable
convert_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Convert')]")))
convert_button.click()

# Wait for the result to be displayed
time.sleep(2)

# Get the result
result_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "result")))
result_text = result_element.text

# Verify the result
expected_result = "Result: " + amount_value
assert result_text == expected_result, f"Test failed: Expected '{expected_result}', but got '{result_text}'"

# Calculate the number of passed tests
num_passed_tests = 1  # Since we only have one test assertion here

# Calculate the total number of tests
total_tests = 1  # You can increase this value if you add more test assertions

# Calculate the percentage of test passes
percentage_passed = (num_passed_tests / total_tests) * 100

# Print the percentage of test passes
print(f"Percentage of test passes: {percentage_passed:.2f}%")

# Close the browser
driver.quit()
