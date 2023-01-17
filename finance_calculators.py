"""

-> request user input for type of calculation to apply (bond / investment)

    -> if INVESTMENT
        -> request from user the following:
            -> amount of money deposting
            -> interest rate as a persentage
            -> number of years investing
            -> type of interest (simple / compound), sotred as a variable called interest

    -> if BOND
        -> request from user the following:
            -> current value of the house
            -> the interest rate
            -> the number of months they plan to repay the bond

-> calculate the value of INVESTMENT / BOND

    -> if INVESTMENT:
        -> if SIMPLE interest:
            -> A =P*(1+r*t)
        -> if COMPOUND interest:
            -> A = P* math.pow((1+r),t)

        -> r = interest rate / 100
        -> P is the deposit
        -> t is the investment period in years
        -> A is the amount once interest is applied

    -> if BOND:
        -> x = (i.P)/(1 - (1+i)^(-n))

        -> P is the value of house
        -> i is the monthly interst rate (annual rate / 12)
        -> n is the number of months the bond is repayable over
        
"""

# import math for compound interest calculation

import math 

# request user input to determine which type of calculation is being applied, the currency,    
# and the time interval

calc_type = input("Choose either \'investment\' or \'bond\' from the menu below to proceed: \n\n"
                    "investment \t - \t to calculate the amount of interest you\'ll earn on your"
                        "investment \n"
                    "bond \t\t - \t to calculate the amount you'll have to pay on a home loan \n\n")

# error handling on calc type input requesting user to try again if not investment or bond

if calc_type.lower() != "investment" and calc_type.lower() != "bond":
    calc_type = input("\n"
                        "There seems to have been an problem with the information you provided. \n"
                        "Select either \'investment\' or \'bond\': \n\n")

####################################################################
# where the user has selected investment as their calculation method

if calc_type.lower() == "investment":

    # request user input the currency
    user_currency = input("\n"
                            "What currency will you be using? ")

    # request user input the value of their deposit
    user_deposit = float(input("\n"
                                "How much will you be depositing? " ))     

    # request user input the length of time that they will be investing for
    user_time = float(input("\n"
                        "How many years will you be investing for? "))

    # request user input the current interest rate
    user_interest_rate = float(input("\n"
                        "What is the interest rate that should be applied (as a %)? "))
    
    # request user input the length of type of interest they would like to calculate
    interest = input("\n"
                        "What type of interest would you like to calculate? Simple or Compound? ")

    # calculations based on interest type

    if interest.lower() == "simple":
        # calc based on formula A =P*(1+r*t)

        interest_return = user_deposit * (1 + (user_interest_rate / 100) * user_time)
        profit = round(interest_return - user_deposit, 2)

        print("\n"
                f"By investing {user_currency}{user_deposit} for {user_time} years, you will gain a profit of "
                f"{user_currency}{profit} when {interest} interest is applied")

    elif interest.lower() == "compound":
        # calc based on formula A = P* math.pow((1+r),t)

        interest_return = user_deposit * math.pow(1 + (user_interest_rate / 100), user_time)
        profit = round(interest_return - user_deposit, 2)

        print("\n"
                f"By investing {user_currency}{user_deposit} for {user_time} years, you will gain a profit of "
                f"{user_currency}{profit} when {interest} interest is applied")

    else:
        print("\n"
                "Something went wrong. Restart the program and try again.")
    
####################################################################
# where the user has selected bond as their calculation method

if calc_type.lower() == "bond":


    # request user input the currency
    user_currency = input("\n"
                            "What currency will you be using? ")

    # request user input present value of the house
    user_house_value = float(input("\n"
                                    "What is the current value of the house? "))

    # request user input the current interest rate
    user_interest_rate = float(input("\n"
                        "What is the annual interest rate that should be applied (as a %)? "))                               

    # request user input the length of time that they will be investing for
    user_time = float(input("\n"
                        "How many months will you repay the bond over? "))

    # calculate the monthly repayments base on formula x = (i.P)/(1 - (1+i)^(-n))

    bond_monthly_value = round(( (( user_interest_rate / 100) / 12 ) * user_house_value) / 
                                (1 - ( 1 + ((user_interest_rate / 100) / 12 )) ** (- user_time ) ), 2)
    
    print("\n"
            f"With a house of {user_currency}{user_house_value}, an annual interest rate of "
            f"{user_interest_rate}%, and a borrowing term of {user_time} months your monthly "
            f"repayments will be {user_currency}{bond_monthly_value}.")
