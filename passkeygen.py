from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open('pass.key', 'wb') as key_file:
        key_file.write(key)
    print("Key generated and saved to 'pass.key'")

if __name__ == "__main__":
    generate_key()
