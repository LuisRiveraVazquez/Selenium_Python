from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import math

drive = webdriver.Chrome(executable_path='../drivers/chromedriver')

drive.get('https://learn.letskodeit.com/p/practice')

drive.maximize_window()

'''
#radio button
drive.find_element_by_id('bmwradio').click()
drive.implicitly_wait(50)

#Select class Example
drive.find_element_by_id('carselect').click()
drive.implicitly_wait(500)
drive.find_element_by_xpath('//*[@id="carselect"]/option[2]').click()

#Multiple Select Example
drive.find_element_by_xpath('//*[@id="multiple-select-example"]/option[3]').click()
drive.find_element_by_xpath('//*[@id="multiple-select-example"]/option[2]').click()

#Check Box Example
drive.find_element_by_xpath('//*[@id="bmwcheck"]').click()

#Switch Windows Example
drive.find_element_by_id('openwindow').click()
drive.switch_to.window(drive.window_handles[1])
drive.implicitly_wait(500)
drive.find_element_by_xpath('//*[@id="search-courses"]').send_keys("Selenium")
drive.switch_to.window(drive.window_handles[0])
drive.implicitly_wait(500)

#Switch to alert example
drive.find_element_by_xpath('//*[@id="name"]').send_keys("Luis")
drive.implicitly_wait(500)
#Switch to alert example ---> Alert
drive.find_element_by_xpath('//*[@id="alertbtn"]').click()
drive.implicitly_wait(500)
alert = drive.switch_to_alert()
drive.implicitly_wait(500)
alert.accept()
drive.implicitly_wait(500)
#Switch to alert example ---> Confirm
drive.find_element_by_xpath('//*[@id="name"]').send_keys("Luis")
drive.implicitly_wait(500)
drive.find_element_by_xpath('//*[@id="confirmbtn"]').click()
drive.implicitly_wait(500)
alert2 = drive.switch_to_alert()
alert2.dismiss()
drive.implicitly_wait(500)
#Switch Windows Example
drive.find_element_by_xpath('//*[@id="opentab"]').click()
'''
#Web table example
drive.find_element_by_xpath('//*[@id="block-1069048"]/div/div/div/div[3]/div[1]/fieldset/legend').location_once_scrolled_into_view
drive.implicitly_wait(30)
data = drive.find_element_by_xpath('//*[@id="product"]/tbody/tr[2]/td[2]').text
print(data)

#Element displayed example
drive.find_element_by_xpath('//*[@id="hide-textbox"]').click()
#drive.implicitly_wait(10)
time.sleep(5)
if drive.find_element_by_xpath('//*[@id="displayed-text"]').is_displayed():
    drive.find_element_by_xpath('//*[@id="displayed-text"]').send_keys("Luis")
    print('the botton is enable')
else:
    print('the botton is not enable')

#Mouse hover example

action = ActionChains(drive)
mouseHover = drive.find_element_by_xpath('//*[@id="mousehover"]')
action.move_to_element(mouseHover).perform()
time.sleep(3)
top = drive.find_element_by_xpath('//*[@id="block-1069048"]/div/div/div/div[4]/div/fieldset/div/div/a[1]')
action.move_to_element(top).perform()
time.sleep(3)
Reload = drive.find_element_by_xpath('//*[@id="block-1069048"]/div/div/div/div[4]/div/fieldset/div/div/a[2]')

#iFrame Example
drive.switch_to_frame()
drive.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[8]/p/a/button').click()
#drive.close()
'''
print('Weight: ' )
weight = input()
print('(L)bs or (K)g: ' )
option = input()
if option == 'L':
    print('You are ' + option * 0.453592)
option1 = input()
if option1 == 'K':
    print('You are ' + option1 * 0.220462)*/
'''
'''
numberWin = 9
counter = 0
while counter < 3:
    number = int(input('Guess: '))
    counter = counter + 1
    if number != numberWin:
        print('you do not win')
        break
    else:
        print('you win')
'''
'''
command = ""
command1 = ""
while command.lower() != "quit":
    command = input("> ")
    if command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
        while command1.lower() != "quit":
            command1 = input("> ")
            if command1 == 'start':
                print("Car started... Ready to go!")
            elif command1 == 'stop':
                print("Car stopped")
            elif command1 == 'quit':
                print("quit - to exit")
            else:
                print('Invalid command')
    else:
        print('Invalid command')
'''
'''
for item in range(20):
    print(item)
'''
'''
price = [10,20,30,40]
for price in [sum(price)]:
    print (f"Total :  {price}")
'''
'''
number = [5,2,5,2,2]
for n in number:
    print('x' * n)
'''
'''
number = [1,2,3,4,5,6,14,21,45,32,100]
for n in number:
    print(max(number))
'''
'''
numbers = [4,5,7,9,1,5,5]
for n in numbers:
    numbers.remove(5)
    print(numbers)
'''
''''
numbers = [4,5,7,9,1,5,5]
numberDel = ""
for numberDel in numbers:
        print(numberDel)
'''





