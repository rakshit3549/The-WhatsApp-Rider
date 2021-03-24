from selenium import webdriver
from time import sleep

# Opening Chrome and Loading Whatsapp web.
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

print('This program works only with Chrome Version 89')
input('\nPress Enter after scanning QR code \n')

# Name of the recipient.
name = input('\nEnter receiver name as saved in Phone Contact :  ')
print("\nMAKE SURE THE RECEIVER'S NAME DOESNOT CONTAINS EMOJOS\nPRESS ENTER IF NOT\nAND IF THERE THEN EDIT THE NAME")

try:

    # Message the need to be send to the recipient.
    msg = input('\nWrite the message you want to send : ')
    count = int(input('\nNo of times to send the message : '))

    # Searching for the recipient in chat Whatsapp list and click on it.
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()

    # Searching for message box in side chat section.
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    # Looping through to send the required number of message send.
    for i in range(count):
        sleep(1)
        msg_box.send_keys(msg) # Adding message inside the message box.
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click() # click on the send botton.
    print('sucess')
except:
    print("Something went wrong :(")

# Close all browser windows
input('\nPress Enter to close all browser windows \n')
driver.quit()
