from instagramBot import InstaFollower

CHROME_DRIVER_PATH = "/home/rgoshen/Development/chromedriver"

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
