#
# Name luis
# Date 11/23/2024
# File Encryption and Decryption Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

def encrypt_file(input_file,output_file, codes):
    try:
        file = open(input_file, 'r')
        original_text = file.read()
        encryped__text = ""
        for char in original_text:
            encryped__text += codes.get(char, char)
        encrypted_file = open(output_file, 'w')
        encrypted_file.write(encryped__text)
        print("File Encrypted Successfully.")
    except FileNotFoundError:
        print("Input file not found.")

encryption_codes = {
            'A' : '%',
            'a' : '9',
            'B' : '@',
            'b' : '#',
            'C' : '*',
            'c' : '$'
        }
encrypt_file('input.txt', 'encrypted_output.txt',encryption_codes)
def decrypt_file(encrypted_file, decrypted_file, codes):
    file = open(encrypted_file, 'r')
    encrypted_text = file.read()
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += codes.get(char, char)

    decrypted_file = open(decrypted_file, 'W')
    decrypted_file.write(decrypted_text)
    print("File Decrypted Succesfully,")
decryption_codes = {
    '%' : 'A',
    '9' : 'a',
    '@' : 'B',
    '#' : 'b',
    '*' : 'C',
    '$' : 'c'
}
decrypt_file('encrypted_output.txt','decryption_codes')


