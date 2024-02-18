num = 0
tot = 0.0
list = []

while True :
    sval = input('Enter a number: ')
    if sval.lower() == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
    #print (fval)
    num = num + 1
    tot = tot + fval
    list.append(fval)
#print('ALL DONE')
print('\nTotal: ' + str(tot) + '\nMin: ' + str(min(list)) + '\nMax: ' + str(max(list)) + '\n')