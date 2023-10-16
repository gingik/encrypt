from cryptography.fernet import Fernet
from datetime import datetime
import ntplib
import os

def decrypt_file(key, input_file, output_file):
    cipher_suite = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

def decrypt_decryption_date(key2):
    with open("decryption_date.enc", "rb") as file:
        encrypted_date = file.read()
    cipher_suite = Fernet(key2)
    decrypted_date_str = cipher_suite.decrypt(encrypted_date).decode()
    return datetime.strptime(decrypted_date_str, "%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    # Use the password obtained from the encryption to decrypt the date and file
    password = input("Enter the encryption key (password): ").encode('utf-8')

    decryption_date = decrypt_decryption_date(password)

    current_time = datetime.now()

    if current_time >= decryption_date:
            # Decrypt the file
            input_file = "encrypted_file.enc"
            decrypted_file = "decrypted_file.txt"
            decrypt_file(password, input_file, decrypted_file)
            print("File decrypted.")
            directory = "./"
            for filename in os.listdir(directory):
                if filename.endswith(".enc"):
                    file_path = os.path.join(directory, filename)
                    os.remove(file_path)
            print("Deleted Encrypted files")

            
    else:
        print("File cannot be decrypted yet.")

