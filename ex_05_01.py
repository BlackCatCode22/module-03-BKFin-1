num = 0
tot = 0.0

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
#print('ALL DONE')
print(tot, num, tot/num)