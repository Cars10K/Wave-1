InterestRate = 0.04 

amount = float(input("How much money is initially deposited into the savings account: $"))

interest = amount * InterestRate
amount += interest
print("The balance at the end of Year 1: ${0:0.2f}.".format(amount))

interest = amount * InterestRate
amount += interest
print("The balance at the end of Year 2: ${0:0.2f}.".format(amount))

interest = amount * InterestRate
amount += interest
print("The balance at the end of Year 3: ${0:0.2f}.".format(amount))
