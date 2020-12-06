import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

op = Options()
# --headlessだけではOSによって動かない、プロキシが弾かれる、
# CUI用の省略されたHTMLが帰ってくるなどの障害が出ます。
# 長いですが、これら6行あって最強かつどんな環境でも動きますので、必ず抜かさないようにしてください。
op.add_argument("--disable-gpu")
op.add_argument("--disable-extensions")
op.add_argument("--proxy-server='direct://'")
op.add_argument("--proxy-bypass-list=*")
op.add_argument("--start-maximized")
op.add_argument("--incognito")
op.add_argument("--headless")
op.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=op.to_capabilities(),
    options=op,
)

# 英和辞書
word = "share"
url = "https://ejje.weblio.jp/content/{}".format(word)

driver.get(url)

# element = WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((By.ID, "myDynamicElement"))


# 単語の取得
Explanation = str
xpath: Explanation = "/html/body/div[3]/div[1]/div/div[1]/div[3]/div[2]/table/tbody/tr/td[2]"

# 型ヒントはつけたいよね
content_explanation: driver = WebDriverWait(driver, 10) \
    .until(
    EC.presence_of_element_located((By.XPATH, xpath))
)

element: Explanation = content_explanation.find_element_by_xpath(xpath)
print("単語の意味", element.text)

# 品詞

xpath = "/html/body/div[3]/div[1]/div/div[1]/div[3]/table[2]/tbody/tr/td[2]/div"
content: driver = WebDriverWait(driver, 10) \
    .until(
    EC.presence_of_element_located((By.XPATH, xpath))
)
element_out = content.find_element_by_xpath(xpath)
element_in = element_out.find_elements_by_tag_name("a")

index = [index.text for index in element_in]

from lib import part_of_speech as ps

val =map(ps.part_of_speech, index)
print(next(val))


# ブラウザを終了する
driver.quit()
