# Open the file for reading
with open('Web_A2.0.txt', 'r') as file:
    content = file.read()  # Read the content
    punctuation = [',', '.', '!', '?', ')', '(', '!,', ').', '),', '*', '&', '0', '2', '3', '4', '5', '6', '7', '8', '9', '"']
    for sign in punctuation:
        content = content.replace(sign, '').lower()
    words = content.split()  # Split content into words
    word_count = len(words)  # Count the words
    unique_words = sorted(set(words)) # Sort them alphabetically
     # Get read of signs

with open('web_A2.0_dict.txt', 'w', encoding='UTF8') as new_file:
    for word in unique_words:
        new_file.write(word + '\n')
print(f'Total words in the file: {word_count}')
# Total words in the file: 7194 (Pycharm)

# Pages	31 (google docs)
# Words	7249
# Characters	53613
# Characters excluding spaces	46564

