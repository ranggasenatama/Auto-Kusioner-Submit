import re
from robobrowser import RoboBrowser
import meta_redirect
import fill_ipd

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
matkul = browser.get_form(id='sipform')

#Trying to count select value and insert in array
n = len(matkul['mk_kuesioner'].options)
arrOptionValue = matkul['mk_kuesioner'].options
print(arrOptionValue)
while n>1:
    n -= 1
    print(arrOptionValue[n])
    matkul['mk_kuesioner'].value = arrOptionValue[n]
    browser.submit_form(matkul)
    kusioner = browser.get_form(id='form2')
    # print(kusioner.parsed)
    # if browser.select('input#MK11'):
    #     fill_ipd.ipm(kusioner)
    #     browser.submit_form(kusioner)
    #     break
    if browser.select(''):
        print('Tidak ada')