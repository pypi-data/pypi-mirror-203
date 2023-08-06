import asyncio
import json
import os
import platform
import re
import sys
import time
from importlib import metadata as importlib_metadata

import markdownify
import undetected_chromedriver as uc
import urllib3
from colorama import Fore
from pyvirtualdisplay import Display
from selenium.common import exceptions as SeleniumExceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

urllib3.disable_warnings()


class Init:
    """
    Start the webdriver\n
    Parameters:
    - proxy: the proxy you want to use\n
    - webdriver_path: pass a localy installed chrome webdriver\n
    Returns a `variable` with the driver
    """

    def __init__(self, verbose: bool = False, proxy: str = "", headless: bool = True, webdriver_path: str = "", hide: bool = False, keep: bool = False) -> None:

        self.__verbose = verbose
        self.__proxy = proxy
        self.__hide = hide
        self.__keep = keep
        if self.__proxy and not re.findall(r"(https?|socks(4|5)?):\/\/.+:\d{1,5}", self.__proxy):
            raise ValueError("Invalid proxy format")
        self._webdriver_path = webdriver_path
        self.__headless = headless
        self.__is_headless = platform.system() == "Linux" and "DISPLAY" not in os.environ
        self.__verbose_print("[0] Platform:", platform.system())
        self.__verbose_print("[0] Display:", "DISPLAY" in os.environ)
        self.__verbose_print("[0] Headless:", self.__is_headless)
        self.__init_browser()

    # def __del__(self):
    #     """
    #     Close the browser and virtual display (if any)
    #     """
    #     if hasattr(self, "driver"):
    #         self.driver.quit()
    #     if hasattr(self, "display"):
    #         self.display.stop()

    def __verbose_print(self, *args, **kwargs) -> None:
        """
        Print if verbose is enabled
        """
        if self.__verbose:
            print(*args, **kwargs)

    # def __ensure_cf(self, retry: int = 0) -> None:
    #     '''
    #     Ensure that the Cloudflare cookies is still valid\n
    #     Parameters:
    #     - retry: The number of times this function has been called recursively
    #     '''
    #     # Open a new tab
    #     self.__verbose_print('[cf] Opening new tab')
    #     original_window = self.driver.current_window_handle
    #     self.driver.switch_to.new_window('tab')

    #     # Get the Cloudflare challenge
    #     self.__verbose_print('[cf] Getting authorization')
    #     self.driver.get('https://you.com/')
    #     try:
    #         WebDriverWait(self.driver, 15).until_not(
    #             EC.presence_of_element_located((By.ID, 'challenge-form'))
    #         )
    #     except SeleniumExceptions.TimeoutException:
    #         self.driver.save_screenshot(f'cf_failed_{retry}.png')
    #         if retry <= 4:
    #             self.__verbose_print(
    #                 f'[cf] Cloudflare challenge failed, retrying {retry + 1}'
    #             )
    #             self.__verbose_print('[cf] Closing tab')
    #             self.driver.close()
    #             self.driver.switch_to.window(original_window)
    #             return self.__ensure_cf(retry + 1)
    #         else:
    #             resp_text = self.driver.page_source
    #             raise ValueError(f'Cloudflare challenge failed: {resp_text}')

    def __init_browser(self) -> None:

        """
        Initialize the browser
        """
        # Detect if running on a headless server
        if self.__is_headless:
            try:
                self.display = Display()
            except FileNotFoundError as e:
                if "No such file or directory: 'Xvfb'" in str(e):
                    raise ValueError("Headless machine detected. Please install Xvfb to start a virtual display: sudo apt install xvfb")
                raise e
            self.__verbose_print("[init] Starting virtual display")
            self.display.start()

        # Start the browser
        options = uc.ChromeOptions()
        # options.add_argument(f"--window-size={800},{600}")
        if self.__headless:
            options.add_argument("--headless")
        if self.__keep:
            options.add_experimental_option("detach", True)
        if self.__proxy:
            options.add_argument(f"--proxy-server={self.__proxy}")
        try:
            self.__verbose_print("[init] Starting browser")
            # self.driver = uc.Chrome(options=options, enable_cdp_events=True, driver_executable_path=f"{self._webdriver_path}")
            if self._webdriver_path:
                self.driver = uc.Chrome(options=options, driver_executable_path=f"{self._webdriver_path}")
            else:
                self.driver = uc.Chrome(options=options)
        except TypeError as e:
            if str(e) == "expected str, bytes or os.PathLike object, not NoneType":
                raise ValueError("Chrome installation not found")
            raise e

        # Restore session token

        # Block moderation
        # self.__ensure_cf()
        # Ensure that the Cloudflare cookies is still valid

    def browser(self):
        return self.driver
