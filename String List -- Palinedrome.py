# Palinedrome 
# Ask the user for a string and print out whether this string 
# is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

def Palinedrome(string):
    revString = ''
    for i in string:
        revString = i + revString # concatenate char to the begin of revString 
    if revString.lower() == string.lower():
        print(string, "is a palinedrome")
    else:
        print(string, "is not a palinedrome")
        
def main():
    userInput = input("Enter a string: ")
    Palinedrome(userInput)
    
main()