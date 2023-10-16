from cryptography.fernet import Fernet
from datetime import datetime, timedelta
import ntplib
import os

def generate_key():
    return Fernet.generate_key()

def encrypt_file(key, input_file, output_file):
    cipher_suite = Fernet(key)
    with open(input_file, 'rb') as file:
        data = file.read()
    encrypted_data = cipher_suite.encrypt(data)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)
    os.remove(input_file)  # Delete the original text file after encryption
    print(key)

def encrypt_and_save_decryption_date(key):
    trusted_time = get_trusted_time()
    decryption_date = trusted_time + timedelta(seconds=30)
    cipher_suite = Fernet(key)
    encrypted_date = cipher_suite.encrypt(decryption_date.strftime("%Y-%m-%d %H:%M:%S").encode())
    with open("decryption_date.enc", "wb") as file:
        file.write(encrypted_date)

def save_encrypted_key(key2, key_file):
    cipher_suite = Fernet(key2)
    # Generate a new key to encrypt
    new_key = generate_key()
    encrypted_key = cipher_suite.encrypt(new_key)
    with open(key_file, "wb") as file:
        file.write(encrypted_key)

def get_trusted_time(server="time.windows.com"):
    c = ntplib.NTPClient()
    response = c.request(server)
    return datetime.fromtimestamp(response.tx_time)

if __name__ == "__main__":
    key = generate_key()
    #key2 = generate_key()
    # Encrypt the file
    input_file = "text.txt"
    encrypted_file = "encrypted_file.enc"
    encrypt_file(key, input_file, encrypted_file)
    print("File encrypted and original file deleted.")

    # Encrypt and save the decryption date
    encrypt_and_save_decryption_date(key)
    
    # Save the encrypted key to a file
    #key_file = "encryption_key.enc"
    #save_encrypted_key(key2, key_file)
    #print("Encryption Key : ", key2)
    #print("Encryption key saved to", key_file)

