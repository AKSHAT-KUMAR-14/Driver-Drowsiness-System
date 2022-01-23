from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        sleep(2)

        #notnow2
        self.drive.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[3]/button[2]").click()
        sleep(6)
    def notfollowingback(self):

        #profileicon
        self.drive.find_element(By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/span").click()
        sleep(6)

        #profile
        self.drive.find_element(By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div").click()
        sleep(6)

        #followers
        self.drive.find_element(By.XPATH, "//a[contains(@href,'/followers')]").click()
        followers = self.mynames()
        self.drive.find_element(By.XPATH, "/html/body/div[6]/div/div/div[1]/div/div[2]/button").click()

        #following
        self.drive.find_element(By.XPATH, "//a[contains(@href,'/following')]").click()
        following = self.mynames()
        self.drive.find_element(By.XPATH, "/html/body/div[6]/div/div/div[1]/div/div[2]/button").click()
        
        #notfollowingback
        notfollowingyouback = [name for name in following if name not in followers]
        print(notfollowingyouback)
    def mynames(self):
        box = WebDriverWait(
          self.drive, 2).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='isgrP']")))
        total_ht,ht = 0,1
        while total_ht!=ht:
            total_ht = ht
            sleep(2)
            ht = self.drive.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """,box)
        link = box.find_elements(By.TAG_NAME, "a")
        names = [name.text for name in link if name.text!= ""]
        return names



username = input("Enter username")
password = input("Enter password")
instabot = insta(username,password)
instabot.notfollowingback()
