def menu():
    print("1. Prime Number Sum Calculator")
    print("2. Length Unit Converter")
    print("3. Consonant Counter")        
    print("4. Main-Max Number Finder")
    print("5. Palindrome Checker")
    print("6. Word Counter")
    print("7. Exit")
    choice = int(input("Enter your choice:"))
    return choice                                  # the function returns the choice made by the user
        
choice = menu()                                    # the choice is stored in the variable choice

def Prime_Number_Sum_Calculator():
    x = int(input("Enter starting range:"))
    y = int(input("Enter ending range:"))
    if (x <= 1):                                        # the starting range cannot be less than or equal to 1 since 1 is not a prime number
        print ("error")

    else:
        prime_sum = 0
        for i in range(x,y+1):                          # y+1 instead of y because the range function is exclusive of the ending range
            if (i > 1):
                is_prime = True
                for p in range(2,int(i**0.5) + 1):      # to identify prime numbers the range of p should be from 2 to the square root of i 
                    if (i % p == 0):                    # if the number is divisible by any number other than 1 and itself then it is not a prime number
                        is_prime = False
                        break
                if is_prime:
                    prime_sum += i                       # prime_sum is the sum of all prime numbers in the range
        print("Sum of prime numbers in range:", prime_sum)

def Length_Unit_Converter():
    length = float(input("Enter the length:"))                       
    x = input("Enter the length (m for meters, f for feet):")
    if x == 'm' or 'M':                                          # if the input is m or M then the length is converted to feet 
        y = length * 3.281                                       # since 1 meter is equal to 3.281 feet
        z = round(y, 2)                                          # round off the result to second decimal places
        print("Length in feet:", z)                              
    elif x == 'f' or 'F':                                        
        y = length / 3.281                                       # since 1 feet is equal to 1/3.281 meters
        z = round(y, 2)
        print("Length in meters:", z)

def Consonant_Counter():
    x = input("Enter a string:")
    count = 0                                                     # keep track of number of consonants
    for i in x:                                                   # for loop goes through the string and consonants
        if i in "bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ":     # the string contains all the consonants
            count += 1                                            # count increases by 1 if the consonant is found
    print("Number of consonants:", count)

def Main_Max_Number_Finder():
    series = input("Enter a serie of numbers:").split()    # split allows the string to be split into a list of numbers allowing multiple words to be input
    minimum = min(series)                                  # min function to find minimum number
    print("Minimum No:", minimum)                         
    maximum = max(series)                                   # max function to find maximum number
    print("Maximum No:", maximum)

def Palindrome_Checker():
    x = input("Enter a string:")
    y = x[::-1]                          # :: reverses the word entered
    if x == y:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")




import requests                                  # type: ignore # import the requests module in phython
from bs4 import BeautifulSoup                    # type: ignore # import the BeautifulSoup module from the bs4 library
import string

def Word_Counter():
    url = 'https://gist.github.com/konrados/a1289ade329ac6f4598ebf5ee3dbcb3c'    # the url is the link to the text file

    response = requests.get(url)                                          # ther request module is to get the content from the url
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()   
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    
    x = text.split()                    # split allows the string to be split into a list of words (allow multiple words to be input x)
    
    word_count = {}                      # Initialize an empty dictionary to store word counts
    for word in x:                         
        word = word.lower()               # Convert word to lowercase
        if word not in word_count:
            word_count[word] = 1           # If the word does not exist in the word_count, add it with a count of 1
        else:
            word_count[word] += 1          # If the word exists in the word_count, increment the count by 1
    for x, count in word_count.items():        
        if x == "the" or x == "and" or x == "was":
            print(f'{x}: {count}')                  # the f-string allows the word and the count to be printed in the same line 

def Exit():
    print("Thank You")

while True:                               # a while loop to keep the program running until the user decides to exit
    if choice == 1:
        Prime_Number_Sum_Calculator()        
    elif choice == 2:
        Length_Unit_Converter()
    elif choice == 3:
        Consonant_Counter()
    elif choice == 4:
        Main_Max_Number_Finder()
    elif choice == 5:
        Palindrome_Checker()
    elif choice == 6:
        Word_Counter()
    elif choice == 7:
        Exit

    x = input("Do you want to try another function (yes or no):")
    if x.lower() == "yes":
       choice = menu()
    else:
        Exit()
        break 
    



    
    
          
    


        
            

