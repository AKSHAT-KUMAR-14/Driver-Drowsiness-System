from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class insta:
    def __init__(self, user, password):
        self.drive = webdriver.Chrome()
        self.user = user
        self.password = password
        self.drive.get("https://www.instagram.com/accounts/emailsignup/?hl=en")
        sleep(4)
        #log
        self.drive.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[2]/p/a").click()
        sleep(4)
        name = self.drive.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input").send_keys(user)
        pasw = self.drive.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
        #submit
        self.drive.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div").click()
        sleep(8)
        #notnow1
        self.drive.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(6)
        #notnow2
        self.drive.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        sleep(6)
    def followers(self):
        #profileicon
        self.drive.find_element(By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/span").click()
        sleep(6)
        #profile
        self.drive.find_element(By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div").click()
        sleep(6)
        #followers
        self.drive.find_element(By.XPATH, "").click()
        sleep(100)


instabot = insta("15.akshith", "1506akshith")
instabot.followers()
