from selenium import webdriver
class insta:
  def __init__(self):
    self.drive = webdriver.Chrome()
    self.drive.get("https://www.instagram.com/?hl=en")
insta()
