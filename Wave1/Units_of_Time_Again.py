TotalSeconds = int(input("Please enter a number of seconds: "))

Days = int(TotalSeconds / 60 / 60 / 24)
TotalSeconds -= Days * 60 * 60 * 24

Hours = int(TotalSeconds / 60 / 60)
TotalSeconds -= Hours * 60 * 60

Minutes = int(TotalSeconds / 60)
TotalSeconds -= Minutes * 60

Seconds = TotalSeconds

print("Amount of time in the form D:HH:MM:SS : {}:{}:{}:{}".format(Days, Hours, Minutes, Seconds))
