#Imports the hashlib library
import hashlib

#Imports the time library
import time

#Creating the function that will try and find the word
def crack_hash(target_hash, wordlist_path, hash_type):

    #Checks to see if the user inputs a valid hash type
    if hash_type not in ["md5", "sha1"]:
        print("Unsupported hash type. Please use md5 or sha1")
        return

    #Creates the start of the timer and attempt counter
    start_time = time.time()
    attempts = 0
    
    #Opening the file as a read only and then making sure it doesnt crash(errors=ignore)
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:

        #Goes through each line in the file and then removes the invisible line that happens
        #when you press enter for a new line
        for line in f:
            word = line.strip()

            #attempt counter
            attempts += 1 

            #If the user chose md5 then it will hash through md5
            if hash_type == "md5":
                attempt = hashlib.md5(word.encode()).hexdigest()

            #Or if the user chose sha1 then it will hash through sha1
            elif hash_type == "sha1":
                attempt = hashlib.sha1(word.encode()).hexdigest()

            #every 100k attempts it will print out how many attempts  have been made
            if attempts % 100000 == 0:
                print(f"Tried {attempts} passwords...")

            #Looping till target word is found
            if attempt == target_hash:
                #marks the time when the word was found
                end_time = time.time()

                #Says total time taken and rounds it off to 2dp
                elapsed = round(end_time - start_time, 2)

                #prints results
                print(f"\nPassword found: {word}")
                print(f"Cracked in {attempts} attempts and {elapsed} seconds")
                return

    #If no password is found then it exists the loop and function ends
    end_time = time.time()
    elapsed = round(end_time - start_time, 2)
    print(f"Password not found in wordlist after {attempts} attempts in {elapsed} seconds")

#Asking the user to enter what they would want
target = input("Enter the hash to crack: ")
path = input("Enter the wordlist path: ")
hash_type = input("Enter hash type (md5 or sha1): ").lower()

crack_hash(target, path, hash_type)
