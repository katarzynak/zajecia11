#To jest program bedacy kalkulatorem
def dodawanie():
    a = int(input('Wprowadz pierwsza liczbe'))
    b = int(input('Wprowadz druga liczbe'))
    print (a+b)

dodawanie()

def dodawanie(a,b):
    return a+b
l1 = int(input('Wprowadz pierwsza liczbe'))
l2 = int(input('Wprowadz druga liczbe'))
print(dodawanie(l1,l2))
