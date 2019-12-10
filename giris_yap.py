from selenium import webdriver
import time
import kullanici

# firefox browserımı kullanacağımı belirtiyorum.
browser = webdriver.Firefox()
# açılan browserı kullanarak hangi linke gideceğini belirtiyoruz
browser.get("https://twitter.com/")
time.sleep(2)

# username ve pass kısmının xpath'lerini belirliyorum nereye gireceğimi
username = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]/div[1]/form/div[1]/input")
password = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]/div[1]/form/div[2]/input")

# username ve pass kısmını başka bir dosyadan çekiyorum gözükmemesi için
username.send_keys(kullanici.user)
password.send_keys(kullanici.passw)

# login butonunun xpath'ini belirliyoruz ve click yaparak tıklıyoruz.
login = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]/div[1]/form/input[1]")
login.click()
time.sleep(10)

browser.close()