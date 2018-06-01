def ipm(kusioner):
    print(kusioner)
    counter = 1
    while counter <= 10:
        kusioner['MK'+str(counter)].value = '4'
        counter += 1
    kusioner['txtKomentar'].value = 'Mantap'
    kusioner['chkPermanent'].value = '1'