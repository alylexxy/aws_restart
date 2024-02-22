userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply.lower() == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply.lower() == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply.lower() == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print(f"Here are {copies} copies.")
else:
    print("Thank you, please come again.")  