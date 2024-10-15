'''name=input('enter the name').strip().title();
msg ="hello {var1} !, welcome to Personalized Adeventure Guide" .format(var1 = name)
print(msg)'''

name=input('enter the name').strip().title();
msg =f"hello {name} !, welcome to Personalized Adeventure Guide"   
print(msg)

destination = input('Destination').strip().lower()
if destination == 'mountain' :
    print('you entered mountain')
elif destination == 'beach':
    print('youn entered beach')
else:
    print("you entered unknown destination")

'''
take budget/day from user. If budget is:
    >500 -> luxry
    200< budget<500 -> good
    budget<200 -> budget
'''

buget= int (input('entert the buget'))
if buget >=500:
    print('luxry')
elif 200<= buget and buget <500:
    print('good')
elif buget < 200:
    print('buget')

day = int (input('enter the days'))

def TotalCost (buget, day):
    return buget*day

print('Total cost of trip is',TotalCost(buget, day))