#Ex2:
from colorama import Fore

def count_words(text):
    words = text.split()
    return len(words)

def replace_words(text, order, words_replace):
    words = text.split()
    words[order-1] = words_replace
    return ' '.join(words)

text = input(Fore.YELLOW + "Nhập ký tự: ")

word_count_original = count_words(text)

order = int(input(Fore.BLUE + "Hãy chọn số thứ tự của từ mà bạn muốn thay thế: "))

words_replace = input(Fore.GREEN + "Nhập vào ký tự bạn muốn thay thế: ")

text_modified = replace_words(text, order, words_replace) 

word_count_modified = count_words(text_modified)

def change_word():
    print("--------------------------------------------------")
    print("==================================================")
    print("--------------------------------------------------")

    print(Fore.RESET + f"SỐ TỪ TRƯỚC KHI SỬA ĐỔI    : {word_count_original}")

    print(f"CÂU SAU KHI ĐƯỢC SỬA ĐỔI   : {text_modified}")

    print(f"SỐ TỪ SAU KHI ĐƯỢC SỬA ĐỔI : {word_count_modified}")

    print(Fore.GREEN + "--------------------------------------------------")
    print("==================================================")
    print("--------------------------------------------------")
    print(Fore.RESET)

change_word()

