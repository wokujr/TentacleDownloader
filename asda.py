import requests
import undetected_chromedriver as uc
import time
import io
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://nhentai.net/g/"
url_input = input("enter your nuke code : ")
new_url = url + url_input + "/"  #nuke code temp : 420328
driver = uc.Chrome(use_subprocess=True)
driver.get(new_url)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "lazyload")))

img_set = set()
hero_img = driver.find_elements(By.CLASS_NAME, "lazyload")
for img in hero_img:
    if img.get_attribute('src') and 'http' in img.get_attribute('src'):
        img_set.add(img.get_attribute('src'))



#image downloader
def image_downloader(download_path,url, file_name):
    image_content = requests.get(url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file)
    file_path = download_path + file_name
    with open(file_path, "wb") as file:
        image.save(file, "JPEG")
    print("SUCCEED")

for i, url in enumerate(img_set):
    image_downloader("hentai/", url, str(i) + ".jpg")

time.sleep(40)
driver.quit()
