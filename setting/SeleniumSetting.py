
class SeleniunmSetting:
    def __init__(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        # from selenium.webdriver.common.by import By
        # from selenium.webdriver.support.ui import WebDriverWait
        # from selenium.webdriver.support import expected_conditions as EC

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

        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',  # docker
            desired_capabilities=op.to_capabilities(),
            options=op,
        )

    def _get_url(self ,url: str):
        self.url = url

    def driver_get(self):
        self.driver.get(self.url)
