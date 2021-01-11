weight = int(input("What is your weight? "))
type_of_weight = str(input("(L)bs or (K)g ")).lower()

if type_of_weight == "l":
    kilo = round(weight / 2.205, 3)
    print(f'You are {kilo} kilograms')
elif type_of_weight == 'k':
    pound = round(weight * 2.205, 3)
    print(f'You are {pound} pounds.')
else:
    print('Invalid')