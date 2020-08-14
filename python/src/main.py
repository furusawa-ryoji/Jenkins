from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Chromeのオプション
options = webdriver.ChromeOptions()
# options.add_argument('--headless')

# pathを設定
import glob
driver_path = glob.glob('./webdriver/chromedriver*')[0]

# Driverの生成
driver = webdriver.Chrome(
    executable_path=driver_path,
    options=options
    )

# URLにアクセス
driver.get('https://gw.skywill.jp')

# # htmlを取得・表示
# html = driver.page_source
# print(html)

# ログインIDを取得し、入力
driver.find_element_by_id("login_id").send_keys("rfurusawa")

# パスワードを取得し、入力
driver.find_element_by_id("login_password").send_keys("Dm453z8B")

# ログインボタンをクリック
driver.find_element_by_name("submit").click()

# # htmlを取得・表示
# html = driver.page_source
# print(html)

# ログイン画面へ遷移
driver.get("https://gw.skywill.jp/cgi-bin/cbag/ag.cgi?")

# # htmlを取得・表示
# html = driver.page_source
# print(html)

# ログインIDを取得し、入力
driver.find_element_by_name("_Account").send_keys("rfurusawa")

# パスワードを取得し、入力
driver.find_element_by_name("Password").send_keys("Dm453z8B")

# ログインボタンをクリック
driver.find_element_by_name("Submit").click()

# # htmlを取得・表示
# html = driver.page_source
# print(html)

# # ブラウザを終了
# driver.quit()