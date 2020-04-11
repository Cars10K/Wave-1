Squarefeet_Per_Acre = 43560
Length = float(input("Please enter the length of the field in feet: "))
Width = float(input("Please enter the width of the field in feet: "))
acres = Length * Width / Squarefeet_Per_Acre
print("The area of the field is", acres, "acres")
