#  A STEGACRYPT APPROACH TO TRIPLE LEVEL DATA SECURITY

                                                 


The project addresses the imperative need for secure information exchange in the modern era dominated by rapid technological advancements. It combines the strengths of cryptography and steganography to enhance data security during transmission.

Key Features:

Dual Encryption Layers:
1.Utilizes Blowfish and Advanced Encryption Standard (AES) algorithms for two-tier encryption.
2.Blowfish ensures efficiency with minimal execution time and memory usage.
3.AES offers robust security with key sizes of 128, 192, and 256 bits, making it highly resistant to hacking attempts.

Steganographic Concealment:
1.Implements Least Significant Bit (LSB) Encoding for embedding encrypted text within an image.
2.LSB Encoding provides perceptual transparency, simplicity of implementation, and reduced suspicion to human observers.
Challenges Addressed:

Cryptography Concerns:
Overcomes the vulnerability of traditional cryptography, where adversaries may monitor transmissions or attempt to obtain decryption keys.

Steganography Drawbacks:
Addresses the risk of exposure when hidden information is suspected, as typical steganographic methods do not involve encryption.

Advantages:
Triple Level Security:
1.Offers a robust security framework by integrating dual encryption layers with steganographic concealment.
2.Outperforms conventional two-level and one-level security systems.

Technical Details:
Blowfish Algorithm:
Chosen for its efficiency, requiring minimal execution time and memory.

AES Algorithm:
Implemented with key sizes of 128, 192, and 256 bits for enhanced resistance against hacking attempts.

LSB Encoding:
Selected for its human-eye-friendly transparency, simplicity, and high perceptual transparency.




To run the project, execute the following steps:
1. Download and install 3.8.0 - 3.8.5 versions of python.
2. Download and install mysql.
3. Create database fcsproject, and a table users in it. The users table has three fields uid, username and password.
4. Download and install visual studio code.
5. Open the project in vscode and install the packages that might be missing such as pycrytodome, tensorflow, Image etc.
6. Run 'app.py' and open the server link that is shown.
