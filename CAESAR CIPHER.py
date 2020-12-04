#Brandon Robbins
#Senior Project Portfolio
#
#A python program to illustrate Caesar Cipher Technique 
key = 'abcdefghijklmnopqrstuvwxyz'# this is where the ceasar cipher gets  all the letters to shift

def encrypt(n, plaintext):#This is the encrypt definition that will mask the characters depending on the key (N)
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26 #increments the letters in the original phrase by n in the key index
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def decrypt(n, ciphertext):#This is the decrypt fucntion which shifts all the letters back by n revealing the original message
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26 #does the reverse of encrypt and subtracts n from key index
            result += key[i]
        except ValueError:
            result += l

    return result

def end(answer):#This function closes the application when the user is done
        
        print("Thank you for using this program")
        exit()
        
  
    


def validation(answer):#This function validates that the user is inputing character values only
    if answer == "end":
            end(answer)
    elif  answer.isdigit():#Checks if input us digit
        print(" Please enter character values only.")
        print("Enter the phrase you would like to be encrytpted. Type end to exit the program")
        newanswer = input()
        return validation(newanswer)
        
        
    else:
        
       compute(answer)            

   

def compute(answer):#This is the function that contains the loop that will keep calculating as many ciphers as the user wishes until "end" is entered as an input

    while True:
        if answer != "end":
                print("Enter the shiftkey you would like")# ask user for the number of positions they would like each letter shifted
                                            
                offset = int(input()) #sets key to user input

                encrypted = encrypt(offset, answer)#calls encrypt function and prints
                print('Encrypted:', encrypted)

                decrypted = decrypt(offset, encrypted)#calls encrypt function and prints
                print('Decrypted:', decrypted)

                print("Enter the phrase you would like to be encrytpted. Type end to exit the program")
                answer = input()
                if answer == "end":
                    end(answer)
                else:
                    validation(answer)# Validates ansnwer each time a new on is put input by the user
        else:
            break
                
        
print("Enter the phrase you would like to be encrytpted. Type end to exit the program")
answer = input()

validation(answer)

print("Thanks for choosing this cryptography program")



