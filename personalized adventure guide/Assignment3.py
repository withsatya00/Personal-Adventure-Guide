def GetValue(prompt):
    while True:
        try:
            a = int(input(prompt))
            return a
            break
        except ValueError:
            print('enter the valid input')

def Destination(destination):
    if destination == 'mountain' :
        print('you entered mountain')
    elif destination == 'beach':
        print('youn entered beach')
    else:
        print("you entered unknown destination")
    
def Buget(buget):
    if buget >=500:
        print('luxry trip')
    elif 200<= buget and buget <500:
        print('good trip')
    elif buget < 200:
        print('buget friendly trip')
        
def TotalCost (buget, day):
    return buget*day

name=input('enter the name ').strip().title();
msg =f"hello {name} !, welcome to Personalized Adeventure Guide"   
print(msg)
dest = input('Destination ').strip().lower()
Destination(dest)
buget=GetValue('buget ')
Buget(buget)
days=GetValue('days ')
print('Total cost of trip is',TotalCost(buget, days))