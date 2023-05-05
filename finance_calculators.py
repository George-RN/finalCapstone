import math

#The two options are written here as functions. They will be called in the while loop below once the user has inputted their option.

def investment_calc():

    #The first three variables take the user entered amounts and convert them to integar so that they can be used for calculations below.
    deposit = int(input('Enter deposit amount: '))
    interest_rate = int(input('Enter interest rate: '))
    years = int(input('Enter number of years investment is planned for: '))
    #This interest variable is left as a string for the user to enter the type.
    interest = input('Enter if the interest is simple or complex: ')

    #interest rate is adjusted to match the task outline before used in the formula below.
    interest_rate = interest_rate / 100

    #Depending on the user choice for the interest variable, the formula used matches the one given in the task outline.
    #The print statements show the total interest. The interest has been rounded down for simplicity. 
    if interest == 'simple':
        simple_interest = deposit * (1 + (interest_rate) * years)
        print(f'Total amount with simple interest is: {math.floor(simple_interest)}')
    elif interest == 'complex':
        complex_interest = deposit * math.pow((1 + interest_rate), years)
        print(f'Total amount with complex interest is: {math.floor(complex_interest)}')
        #print(f'Total amount with complex interest is: {complex_interest}')

def bond_calc():

    #These three variables take the user entered amounts and convert them to integar so that they can be used for calculations below.
    value = int(input('Enter value of the house: '))
    interest_rate = int(input('Enter interest rate: '))
    repayment_time = int(input('Enter of number of months planned to repay the bond: '))

    #interest rate is adjusted to match the task outline before used in the formula below.
    interest_rate = (interest_rate / 100) / 12

  
    #This is the formula used to calculate the bond from the task outline.
    #The repayment value has been rounded down for simplicity. 
    repayment = (interest_rate * value) / (1 - (1 + interest_rate) ** (-repayment_time))
    print(math.floor(repayment))

#User instructions 
print('''investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan''')

#Input stored as user_option allows user to enter string based on which option they want to use. 
user_option = input('Enter either "investment" or "bond" from the menu above to proceed: ')

#While loop to ensure the user enters a valid option. Users .lower() to user_options so that it won't be case sensitive.

while True:
    #Checks for investment option and runs the corresponding function then breaks the loop so it only shows investment.
    if user_option.lower() == 'investment':
        investment_calc()
        break
    
    #Checks for bond option and runs the corresponding function then breaks the loop so it only shows bond.
    elif user_option.lower() == 'bond':
        bond_calc()
        break
    
    #Else clause displays error message if option not given correctly and will keep running until user enters valid option. 
    else:
        user_option = input('Option not recognised. Please select either investment or bond from the menu above: ')



    
