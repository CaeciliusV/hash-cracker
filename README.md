# Beginner Python Hash Cracker

This is a command-line dictionary attack tool that cracks MD5 and SHA1 password hashes using a wordlist.
I built it to understand how password hashing works and why even when weak passwords are stored as hashes 
they are still vlnerable.

## What it does

- Takes in target hash from user
- Can take both MD5 and SHA1
- Runs a dictionary attacking using a wordlist (tested with rockyou.txt)
- Shows progress every 100K attempts
- Outputs the cracked password, time taken and total attempts

## What I learned

- What a hashing algorithm is
- How hashing algorithms work
- Why dictionary attacks are effective with weak passwords
- What salting passwords are and how they defeat this type of attack
- File handling in Python
- Using the hashlib library
- Using the time library

## How to run it

1. Download or clone this repository
2. Download a wordlist (rockyou.txt is recommended)
3. Generate a test hash to crack:
import hashlib
print(hashlib.md5("yourword".encode()).hexdigest())

4. Run the cracker
5. Enter your hash, wordlist file path, and hash type

## Example output

  Enter the hash to crack: 5f4dcc3b5aa765d61d8327deb882cf99
  Enter the wordlist path: rockyou.txt
  Enter hash type (md5 or sha1): md5

  Password found: password
  Cracked in 1 attempts and 0.0 seconds

## Limitations
- Only supports MD5 and SHA1
- Salted hashes cannot be cracked
- speed is dependent on wordlist size and your hardware
- Attack only works if the password is in the wordlist

## Tools used

- Python 3
- hashlib (built-in)
- time (built-in)
- rockyou.txt wordlist
