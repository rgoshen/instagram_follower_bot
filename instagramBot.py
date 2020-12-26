from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "rgoshen72"
PASSWORD = "NitL10n$#1"


class InstaFollower:
    """
    Class to create an instagram follower bot.
    """

    def __init__(self, path):
        """
        Instagram follower bot constructor.
        """
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        """
        Method to login into instagram account.
        """
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        pass

    def follow(self):
        pass
