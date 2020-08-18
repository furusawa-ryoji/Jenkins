from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Chromeのオプション
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

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

# 現在のhtmlのtitleを取得・表示
title = driver.title
print(title)

# ログインIDを取得し、入力
driver.find_element_by_id("login_id").send_keys("rfurusawa")

# パスワードを取得し、入力
driver.find_element_by_id("login_password").send_keys("Dm453z8B")

# ログインボタンをクリック
driver.find_element_by_name("submit").click()

# 現在のhtmlのtitleを取得・表示
title = driver.title
print(title)

# ログイン画面へ遷移
driver.get("https://gw.skywill.jp/cgi-bin/cbag/ag.cgi?")

# 現在のhtmlのtitleを取得・表示
title = driver.title
print(title)

# ログインIDを取得し、入力
driver.find_element_by_name("_Account").send_keys("rfurusawa")

# パスワードを取得し、入力
driver.find_element_by_name("Password").send_keys("Dm453z8B")

# ログインボタンをクリック
driver.find_element_by_name("Submit").click()

# 現在のhtmlのtitleを取得・表示
title = driver.title
print(title)
print('これで終了')

# ブラウザを終了
driver.quit()