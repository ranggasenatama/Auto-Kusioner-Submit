import re
from robobrowser import RoboBrowser
import meta_redirect

#Browse Integra ITS
browser = RoboBrowser(parser='html.parser',history=True)
browser.open('https://integra.its.ac.id/')

#Get Username and Password from User
print ("Kusioner ITS Auto Submit")
nrp = input("Your NRP? ")
password = input("Your Password? ")

#Searh for input username and password form
form = browser.get_form(id='login_form')
form['userid'].value = nrp
form['password'].value = password
browser.submit_form(form)

#Forward to page Dashboard Integra
browser.open('https://integra.its.ac.id/dashboard.php?sim=AKADX__-__')

#Extract meta data refresh integra
browser.open(meta_redirect.getUrl(str(browser.parsed)))

#Let's go to select kusioner dosen and mk page
browser.open('http://akademik3.its.ac.id/ipd_kuesionermk.php')
form = browser.get_form(id='sipform')

#Trying to count select value and insert in array
n = len(form['mk_kuesioner'].options)
arrOptionValue = form['mk_kuesioner'].options
print(arrOptionValue)
while n>1:
    n -= 1
    print(arrOptionValue[n])