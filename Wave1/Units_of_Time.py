days = int(input("Please enter an amount of time in days: "))
hours = int(input("Please enter an amount of time in hours: "))
minutes = int(input("Please enter an amount of time in minutes: "))
seconds = int(input("Please enter an amount of time in seconds: "))

totalSeconds = seconds
totalSeconds += minutes * 60
totalSeconds += hours * 60 * 60
totalSeconds += days * 60 * 60 * 24

print("The total number of seconds is {}.".format(totalSeconds))