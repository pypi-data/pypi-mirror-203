from selenium.webdriver.chrome.service import Service as ChromeService
from pathlib import Path
import os
from arklibrary import Ini


class Service:
    def __init__(self):
        self.path = self.chrome_driver_path()
        self.service = self._service()

    @classmethod
    def chrome_driver_path(self):
        path = self.driver_path_from_env()
        if path:
            return path
        path = self.driver_path_from_ini()
        if path:
            return path
        path = self.find_chrome_driver()
        if path:
            return path

    @classmethod
    def driver_path_from_env(cls):
        key = 'CHROME_DRIVER'
        env_path = os.getenv(key)
        if env_path is not None:
            path = Path(env_path)
            if path.exists():
                return path

    @classmethod
    def driver_path_from_ini(cls):
        key = 'CHROME_DRIVER'
        ini = Ini('config.ini')
        if key in ini and 'path' in ini[key]:
            path = Path(ini[key]['path'])
            if path.exists():
                return path

    def find_chrome_driver(self):
        # TODO: if you can't find in directories, download it
        pass

    def download_chrome_driver(self):
        # TODO: download it
        pass

    def _service(self):
        if self.path:
            return ChromeService(executable_path=str(self.path))
        return ChromeService()

    def bind(self):
        return self.service

    def __repr__(self):
        path = self.path
        return f"<Service(path={repr(path)})>"

