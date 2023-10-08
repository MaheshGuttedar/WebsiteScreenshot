from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Define the URL of the webpage you want to convert
webpage_url = 'https://www.w3schools.com/'

# Define the path to the output PDF file
output_pdf_file = 'C:\\Users\\pc\\Desktop\\convert_webpage_to_pdf\\output.pdf'

# Configure Chrome options (headless mode)
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
chrome_options.add_argument('--disable-gpu')  # Disable GPU for headless mode
chrome_options.add_argument('--no-sandbox')  # Disable sandbox for headless mode

# Set up the Chrome web driver
chrome_service = ChromeService(executable_path='C:\\Users\\pc\\Desktop\\convert_webpage_to_pdf\\webdriver\\chromedriver.exe')  # Replace with the actual path to chromedriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to the webpage
driver.get(webpage_url)

# Wait for the page to load (you can adjust the wait time as needed)
driver.implicitly_wait(10)  # Wait for up to 10 seconds for page elements to load

# Take a screenshot of the entire webpage
driver.save_screenshot('screenshot.png')

# Convert the screenshot to a PDF using a library like PIL (Python Imaging Library)
from PIL import Image

# Open the screenshot
screenshot = Image.open('screenshot.png')

# Convert the screenshot to PDF
screenshot.save(output_pdf_file, 'PDF')

# Close the browser
driver.quit()
