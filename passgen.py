import hashlib
import getpass

def load_criteria(criteria_file):
    with open(criteria_file, 'r') as file:
        criteria = file.read().strip()
    return criteria

def hash_password(password):
    # Hash the password using SHA-256
    hasher = hashlib.sha256()
    hasher.update(password.encode())
    return hasher.digest()  # This returns the binary hash of the password

def conform_to_criteria(hashed_password, criteria):
    # Convert hashed bytes to characters in the criteria
    return ''.join(criteria[b % len(criteria)] for b in hashed_password)

def main():
    criteria_file = 'pass.crit'
    password = getpass.getpass("Enter your password: ")
    
    criteria = load_criteria(criteria_file)
    
    hashed_password = hash_password(password)
    final_password = conform_to_criteria(hashed_password, criteria)
    
    print(f"Your consistent password is:\r\n{final_password}")

if __name__ == "__main__":
    main()
