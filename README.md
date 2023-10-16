# Encryption and Decryption Tool

Welcome to the "My Awesome Encryption and Decryption Tool" repository! This tool allows you to encrypt files, set decryption dates, and decrypt them at a later time.

## Features

- Secure file encryption using Fernet cryptography.
- Set decryption dates for encrypted files.
- Delete the original files after encryption for added security.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/gingik/encrypt.git

Install the required Python packages using pip:
pip install -r requirements.txt

Usage
Encryption
Ensure you have a text file (msut be called text.txt) that you want to encrypt.

Run the encryption script:

python encrypt.py

This will encrypt the file and set a decryption date.
The original file (text.txt) will be deleted after encryption.
The encrypted file will be saved as encrypted_file.enc.

Decryption
Wait until the decryption date is reached.

Run the decryption script:

python decrypt.py

This script will check if the file can be decrypted based on the decryption date.
If the date is reached, it will decrypt the file.
The decrypted file will be saved as decrypted_file.txt.

Configuration
You can customize the decryption date in the encrypt.py script.
The encryption key is stored in an encrypted file, and the password is used for decryption in the decrypt.py script.
Contributing
If you would like to contribute to this project or report issues, please follow these steps:

Fork the repository.
Create a new branch for your changes.
Make your changes and test them.
Submit a pull request with a clear description of your changes.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have any questions or feedback, feel free to reach out to info@opensolutions.tech.

Thank you for using "A simple Encryption and Decryption Tool!" We hope it meets your encryption needs.

