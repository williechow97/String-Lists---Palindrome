# Palindrome 
# Ask the user for a string and print out whether this string 
# is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

'''
fix to catch numbers 
make so ignores spaces and exclamation
best to separate string into list of char and check conditions and create the reverse string 
'''

SYMBOLS = ['!',',' '.', '?', '@', '#', '$', '%', '&', '*', '[', ']', '{', '}']  # Global variable of a list of special characters

def Palindrome(string):
    '''@param: string
        check to see if string is palindrome or not
    '''
    revString = ''  # empty that will hold the reverse string
    newString = ''  # empty string that will hold the string without spaces
    for i in string:
        if not i.isspace() and i not in SYMBOLS:    #disregards spaces and special symbols
            newString = newString + i # concatenate string to have same chars as string parameter
            revString = i + revString # concatenate char to the begin of revString 
    if revString.lower() == newString.lower(): # compare string(non-case sentitive) 
        print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome")
        
def main():
    
    again = True
    userInput = input("Enter a string: ")
    while again:
        if not userInput.isdigit(): # don't allow only digits
            if userInput not in SYMBOLS: # don't allow symbols
                Palindrome(userInput)
                again = False   # break out of while loop
            else:   # continue asking user for correct input
                print('No special symbols')
                userInput = input('Enter a string: ')
        else:    # continue asking user for correct input
            print('Please enter only characters:')
            userInput = input('Enter a string: ')
main()
