def alphabet():
    alphabets_in_capital = []
    for i in range(ord('А'),ord('ѐ')):
        alphabets_in_capital.append(chr(i))
    return alphabets_in_capital

def encrypted_text(text, alphabet, encrypt_number):
    result = ''
    for char in text:
        if char in alphabet:
            for i in range(len(alphabet)):
                if(alphabet[i] == char):   
                    result += alphabet[i - encrypt_number]  
        else: result += char
    return result

def write_text_into_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)

def read_text_from_file(file_name):
    text = ''
    with open(file_name, 'r') as file:
        for line in file.readlines():
            text += line
    return text

def unencrypt_text(text, alphabet, encrypt_number):
    result = ''
    for char in text:
        if char in alphabet:
            for i in range(len(alphabet)):
                if(alphabet[i] == char):   
                    result += alphabet[i + encrypt_number]  
        else: result += char
    return result



alphabet = alphabet()
normal_text = read_text_from_file('/Users/volodia/Desktop/Python/DZ/DZ 4/task_4_normal.txt')
encrypted_text = encrypted_text(normal_text, alphabet, 2)
write_text_into_file('/Users/volodia/Desktop/Python/DZ/DZ 4/task_4_shifr.txt', encrypted_text)
encrypted_text_from_file = read_text_from_file('/Users/volodia/Desktop/Python/DZ/DZ 4/task_4_shifr.txt')
unencrypted_text = unencrypt_text(encrypted_text_from_file, alphabet, 2)