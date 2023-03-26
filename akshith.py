from tkinter import Label, Entry, Button, Tk, messagebox, Checkbutton, BooleanVar, PhotoImage, font


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import exit
from selenium.webdriver.common.keys import Keys
from threading import Thread


class insta:
    def __init__(self, user, password):
        self.drive = webdriver.Chrome()
        self.user = user
        self.password = password
        self.drive.get("https://www.instagram.com/accounts/emailsignup/?hl=en")
        sleep(4)

        #log
        try:
            self.drive.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[2]/p/a").click()
            sleep(4)
        except:
            messagebox.showerror("Error","An Unknown Error has occurred. \n Please try Again")
        usrname = self.drive.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input").send_keys(self.user)
        pasw = self.drive.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input").send_keys(self.password)

        #submit
        try:
            self.drive.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div").click()
            sleep(8)
        except:
            messagebox.showerror("login error", "Invalid Credentials")
            exit()




        #notnow1
        try:
            self.drive.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button").click()
            sleep(2)
        except:
            pass


        #notnow2
        try:
            self.drive.find_element(By.XPATH, "//button[text()='Not Now']").click()
            sleep(4)

        except:
            pass

    def notfollowingback(self):

        #profileicon
        self.drive.find_element(By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]").click()
        sleep(4)

        #profile
        self.drive.find_element(By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div").click()
        sleep(4)

        #followers
        self.no_of_names = int(self.drive.find_element(By.XPATH, "//li[2]/a/span").text)
        self.drive.find_element(By.XPATH, "//a[contains(@href,'/followers')]").click()
        followers = self.mynames()
        self.drive.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[1]/div/div[2]/button").click()

        #following
        self.no_of_names = int(self.drive.find_element(By.XPATH, "//li[3]/a/span").text)
        self.drive.find_element(By.XPATH, "//a[contains(@href,'/following')]").click()
        following = self.mynames()
        self.drive.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[1]/div/div[2]/button").click()

        #notfollowingback
        if followers==None and following!=None:
            messagebox.showinfo("list",following)
            self.copybtn = Button(w,text="Copy to Clipboard",command=gui().copy)
            self.copybtn.grid(row=20,column=8,font=("consolas",15))
            w.clipboard_append(following)


        elif following==None:
            messagebox.showinfo("Result","You are not following anyone")
        else:
            notfollowingyouback = [name for name in following if name not in followers]
            messagebox.showinfo("list", notfollowingyouback)
            self.copybtn = Button(w, text="Copy to Clipboard", command=gui().copy)
            self.copybtn.grid(row=20, column=8,font=("consolas",15))
            w.clipboard_append(notfollowingyouback)


    def mynames(self):
        try:
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

            listofname = box.find_elements(By.TAG_NAME, "a")
            names = [name.text for name in listofname if name.text!= ""]
            return names[0:self.no_of_names]

        except:
            pass


    def like(self,hashtag,comment,no_of_posts):

        #search
        self.drive.find_element(By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys("#"+hashtag+Keys.ENTER)
        sleep(2)
        self.drive.get("https://www.instagram.com/explore/tags/{}/".format(hashtag))
        sleep(2)


        #condition
        no_of_posts_in_hashtag = self.drive.find_element(By.XPATH, "/html/body/div[1]/section/main/header/div[2]/div/div[2]/span/span").text
        no_of_posts_in_hashtag = no_of_posts_in_hashtag.replace(",","")
        no_of_posts_in_hashtag = int(no_of_posts_in_hashtag)
        if no_of_posts<=no_of_posts_in_hashtag:

            # openpost
            self.drive.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]").click()
            sleep(4)

            # no_of_posts
            for i in range(no_of_posts):
                # likebutton
                self.drive.find_element(By.XPATH,
                                        "/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
                sleep(2)

                # commentbutton
                self.drive.find_element(By.XPATH,
                                        "/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/button").click()
                sleep(4)
                self.drive.find_element(By.CLASS_NAME, "Ypffh").send_keys(comment + Keys.ENTER)
                sleep(6)

                # nextpost
                self.drive.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/button").click()
                sleep(4)
        else:
            messagebox.showerror("Value is greater","Value entered for Number of posts is higher than Number of posts present in hashtag")





class gui():

    def start(self):
        Thread(target=self.login).start()

    def copy(self):
        messagebox.showinfo("Success","Copied to Clipboard Successfully")


    def Next(self):
        if input_user.get() != "" and input_pass.get() != "":
            # fornotfollowing
            if checkvar_for_following.get() == True and checkvar_for_likeandcomment.get() == False:
                next.configure(text="Login", command=self.start, font=("consolas",15))

            # for_likeandcomment
            elif checkvar_for_likeandcomment.get() == True and checkvar_for_following.get() == False:
                next.configure(text="Login", command=self.start, font=("consolas",15))

                # hashtaggui
                hashtag_label = Label(w, text="Enter Hashtag without #")
                self.hashtag = Entry(w)
                hashtag_label.grid(row=12, column=2, sticky="w")
                self.hashtag.grid(row=12, column=6)
                hashtag_label.configure(font=(5))

                # commentgui
                comment_label = Label(w, text="Enter Comment")
                self.comment = Entry(w)
                comment_label.grid(row=13, column=2, sticky="w")
                self.comment.grid(row=13, column=6)
                comment_label.configure(font=(5))

                # no_of_posts
                post_label = Label(w, text="Number of posts to like and comment")
                self.post = Entry(w)
                post_label.grid(row=14, column=2)
                self.post.grid(row=14, column=6)
                post_label.configure(font=(5))


            # for_both_selected
            elif checkvar_for_likeandcomment.get() == True and checkvar_for_following.get() == True:
                next.configure(text="Login", command=self.start, font=("consolas",15))

                # hashtaggui
                hashtag_label = Label(w, text="Enter Hashtag without #")
                self.hashtag = Entry(w)
                hashtag_label.grid(row=12, column=2, sticky="w")
                self.hashtag.grid(row=12, column=6)
                hashtag_label.configure(font=("consolas",15))

                # commentgui
                comment_label = Label(w, text="Enter Comment")
                self.comment = Entry(w)
                comment_label.grid(row=13, column=2, sticky="w")
                self.comment.grid(row=13, column=6)
                comment_label.configure(font=("consolas",15))

                # no_of_posts
                post_label = Label(w, text="Number of posts to like and comment")
                self.post = Entry(w)
                post_label.grid(row=14, column=2)
                self.post.grid(row=14, column=6)
                post_label.configure(font=("consolas",15))




            # for_none_selected
            elif checkvar_for_likeandcomment.get() == False and checkvar_for_following.get() == False:
                messagebox.showwarning("No Options Selected", "Select one option")


        else:
            messagebox.showwarning("Missing Info", "Enter Info")




    def login(self):

        # fornotfollowing
        if checkvar_for_following.get() == True and checkvar_for_likeandcomment.get() == False:
            instabot = insta(input_user.get(), input_pass.get())
            instabot.notfollowingback()

        # forlikeandcomment
        elif checkvar_for_likeandcomment.get() == True and checkvar_for_following.get() == False:
            sleep(2)
            if input_user.get()!= "" and input_pass.get()!= "" and self.hashtag.get() != "" and self.comment.get() != "" and self.post.get() != "":

                try:
                    int(self.post.get())
                    instabot = insta(input_user.get(), input_pass.get())
                    sleep(4)

                    instabot.like(self.hashtag.get(), self.comment.get(), int(self.post.get()))
                    sleep(4)
                except:
                    messagebox.showerror("Invalid Value","The value entered for number of posts should be a number without any alphabets,characters,space")

            else:
                messagebox.showwarning("Missing Info","Enter Info")

        # for_both_selected
        elif checkvar_for_likeandcomment.get() == True and checkvar_for_following.get() == True:
            if input_user.get()!= "" and input_pass.get()!= "" and self.hashtag.get() != "" and self.comment.get() != "" and self.post.get() != "":
                try:
                    int(self.post.get())
                    instabot = insta(input_user.get(), input_pass.get())
                    instabot.notfollowingback()
                    sleep(3)
                    instabot = insta(input_user.get(), input_pass.get())
                    sleep(4)
                    instabot.like(self.hashtag.get(), self.comment.get(), int(self.post.get()))
                    sleep(4)
                except:
                    messagebox.showerror("Invalid Value","The value entered for number of posts should be a number without any alphabets,characters,space")

            else:
                messagebox.showwarning("Missing Info","Enter Info")

        # for_none_selected
        elif checkvar_for_likeandcomment.get() == False and checkvar_for_following.get() == False:
            messagebox.showwarning("No Options Selected", "Select one option")










#GUI
w = Tk()
w.title('Instabot')
w.geometry("1000x500")
logo = PhotoImage(file = "instabot_logo.png")
w.iconphoto(True,logo)

#logininput
username = Label(w,text='Username')
password = Label(w,text='Password')
input_user = Entry(w)
input_pass = Entry(w)
next = Button(w,text='Next',command=gui().Next,font=("consolas",15))
username.grid(row=7,column=2,sticky="w")
password.grid(row=9,column=2,sticky="w")
input_user.grid(row=7,column=6)
input_pass.grid(row=9,column=6)
username.configure(font=("consolas",15))
password.configure(font=("consolas",15))


#botfunction_notfollowing
checkvar_for_following = BooleanVar()
notfollowing = Checkbutton(w,text="Not Following Back",variable=checkvar_for_following)
notfollowing.grid(row=10,column=2)
notfollowing.configure(font=("consolas",15))

#botfunction_likeandcomment
checkvar_for_likeandcomment = BooleanVar()
likeandcomment = Checkbutton(w,text="Like and comment",variable=checkvar_for_likeandcomment)
likeandcomment.grid(row=10,column=6)
likeandcomment.configure(font=("consolas",15))

#nextbutton
next.grid(row=20,column=6)


w.mainloop()







