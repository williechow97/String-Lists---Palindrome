# Palinedrome 
# Ask the user for a string and print out whether this string 
# is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

'''
fix to catch numbers 
make so ignores spaces and exclamation
best to separate string into list of char and check conditions and create the reverse string 
'''

def Palinedrome(string):
    revString = ''
    for i in string:
        revString = i + revString # concatenate char to the begin of revString 
    if revString.lower() == string.lower(): # compare string(non-case sentitive) 
        print(string, "is a palinedrome")
    else:
        print(string, "is not a palinedrome")
        
def main():
    symbols = ['!',',' '.', '?', '@', '#', '$', '%', '&', '*']
    again = True
    userInput = input("Enter a string: ")
    while again:
        if not userInput.isdigit():
            if userInput not in symbols:
                Palinedrome(userInput)
                again = False
            else:
                print('No special symbols')
                userInput = input('Enter a string: ')
        else:
            print('Please enter only characters:')
            userInput = input('Enter a string: ')
main()
