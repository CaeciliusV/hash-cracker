import hashlib
import time

def crack_hash(target_hash, wordlist_path, hash_type):

    if hash_type not in ["md5", "sha1"]:
        print("Unsupported hash type. Please use md5 or sha1")
        return

    start_time = time.time()
    attempts = 0
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:

        for line in f:
            word = line.strip()
            attempts += 1
            
            if hash_type == "md5":
                attempt = hashlib.md5(word.encode()).hexdigest()

            elif hash_type == "sha1":
                attempt = hashlib.sha1(word.encode()).hexdigest()
                
            if attempts % 100000 == 0:
                print(f"Tried {attempts} passwords...")

            if attempt == target_hash:
                end_time = time.time()
                elapsed = round(end_time - start_time, 2)
                print(f"\nPassword found: {word}")
                print(f"Cracked in {attempts} attempts and {elapsed} seconds")
                return

    end_time = time.time()
    elapsed = round(end_time - start_time, 2)
    print(f"Password not found in wordlist after {attempts} attempts in {elapsed} seconds")


target = input("Enter the hash to crack: ")
path = input("Enter the wordlist path: ")
hash_type = input("Enter hash type (md5 or sha1): ").lower()

crack_hash(target, path, hash_type)
