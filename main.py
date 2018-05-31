import re
from robobrowser import RoboBrowser

#Browse Integra ITS
browser = RoboBrowser(parser='html.parser',history=True)
browser.open('https://integra.its.ac.id/')

#Get Username and Password from User
print ("Kusioner ITS Auto Submit")
nrp = input("Your NRP? ")
password = input("Your Password? ")

#Searh for input username and password form
form = browser.get_form(id='login_form')
print(form)
form['userid'].value = nrp
form['password'].value = password
browser.submit_form(form)

#Forward to page History
print(browser.parsed)
