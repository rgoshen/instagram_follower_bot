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
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass
