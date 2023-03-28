while(True):
    print("Press q to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:                                      # this try block will always run
        print("Trying...")
        a = int(a)                            # for example , when user input a string instead of an integer then except block will run
        if a>6:
            print("You entered a number greater than 6")
    except Exception as e:                     # if the code written in try block throws an error then the except block will run otherwise not
        print(f"Your input resulted in an error: {e}")

print("Thanks for playing this game")


# when a specific code throws an error , then system directly goes into except block, didn't matter if some code is present below that code which throwed error


