def read_text_from_file(file_name):
    text = ''
    with open(file_name, 'r') as file:
        for line in file.readlines():
            text += line
    return text

def write_text_into_file(file_name, list):
    with open(file_name, 'w') as file:
        count = 0
        for line in list:
            count += 1
            file.write(line)
            if (count < len(list)):
                 file.write('&')

def compress_text(text):
    result = []
    for i in range(len(text)):
        if i == 0:
            result.append(text[i] + "=1")
        elif i == 1:
            if text[i] == text[i-1]:
                result[0] = text[i] + "=2"
        else:
            if text[i] == text[i-1]:
                result[len(result) - 1] = text[i] + "=" + str(int(result[len(result) - 1].split('=')[1]) + 1)
            else:
                result.append(text[i] + "=1")
    return result

def uncompress_text(text):
    result = ''
    for pair in text.split('&'):
        length = pair.split('=')[1]
        char = pair.split('=')[0]
        for i in range(int(length)):
            result += char
    return result

text_from_file = read_text_from_file("/Users/volodia/Desktop/Python/DZ/DZ 4/task_5_input.txt")
list_compressed_text = compress_text(text_from_file) 
write_text_into_file("/Users/volodia/Desktop/Python/DZ/DZ 4/task_5_output.txt", list_compressed_text)
compressed_text = read_text_from_file('/Users/volodia/Desktop/Python/DZ/DZ 4/task_5_output.txt')
uncompressed_text = uncompress_text(compressed_text)

print("\n" + text_from_file, end="\n\n")
print(compressed_text, end="\n\n")
print(uncompressed_text, end="\n\n")