from selenium.webdriver import Chrome
from selenium.webdriver.remote.command import Command
import datetime

class AutoChartWebDriver(Chrome):
    def __init__(self, port=5000):
        self.url= f'http://localhost:{port}'

    def start(self):
        super().__init__()
        self.get(self.url)

    def quit(self):
        Chrome.quit(self)
        self.session_id = None

    def screenshot(self):
        name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.save_screenshot(f'{name}.png')


#TODO: Screen shot command
