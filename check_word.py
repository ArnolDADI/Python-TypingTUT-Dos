"""
Module to take the text from the parrent file and run typing tutorial and return if the user passed it or not
"""
import os
from getch import getch
from time import time

from color import color

# Lambda function to clear screen
cls = lambda: os.system('cls' if os.name=='nt' else 'clear')

def check_word(text, name):
    """ To check correctness of the typing tutorial while using """
    #variables
    count = 0
    count_letter = 0
    count_word = 0
    print(text)
    list_word = list(text.split())      # Create a list of the words in the text
    count_right = 0
    count_wrong = 0
    typed_letter = ''
    typed_word = ''
    input_letter = ''
    str = ''
    start = time()
    input_letter_unformatted = ''
    
    #loop to take input and check it
    while count_word < len(list_word):
        
        counter = 0
        flag = 0

        # To add space after the word except the last one
        if count_word != len(list_word) -1:
            typed_word = list_word[count_word] + ' '
        else:
            typed_word = list_word[count_word]

        count_letter = len(typed_word)

        # To check if the typed word is same as the inputted word
        while counter < count_letter:
            
            key = getch()
            input_letter_unformatted += key

            # To make a string for the typed words
            if key == typed_word[counter]:
                typed_letter += f"{color['green']}{typed_word[counter]}"
                input_letter += f"{color['green']}{key}"
            else:
                flag = 1
                typed_letter += f"{color['bright_red']}{typed_word[counter]}{color['green']}"
                input_letter += f"{color['bright_red']}{key}{color['green']}"

            cls()       # Clear screen

            # To print the string 
            try:
                print(f"{typed_letter}{color['bright_blue']}{color['bold']}{color['bg_white']}\
{text[count+1]}{color['reset']}{color['bright_yellow']}{text[count+2:]}{color['reset']}")
            except:
                print(f"{typed_letter}")
            
            counter += 1
            count += 1

        try:
            str += typed_letter
        except:
            str += typed_letter 

        if flag == 1:
            count_wrong += 1
        else:
            count_right += 1

        count_word += 1

    end  = time()

    print(f"{input_letter}{color['reset']}")

    time_taken = end - start
    accuracy = (count_right/count_word)*100
    wpm = count_word/(time_taken/60)
    cpm = count/(time_taken/60)

    # To print the results and parameters of the test
    print(f">>>Total words = {count_word}\n>>>Correct words = {count_right}\n>>>Wrong words = {count_wrong}")
    print(f">>>Accuracy = {accuracy}%")
    print(f">>>Time taken = {time_taken}")
    print(f">>>Total keys pressed = {count}")
    print(f">>>cpm = {cpm}")
    print(f">>>wpm = {wpm}")

    list_details = [text, input_letter_unformatted, count, count_word, count_right, count_wrong, int(accuracy), int(time_taken), int(cpm), int(wpm)]

    details(list_details, name)

    # To return different values from the result of the test to the parent file
    if accuracy >= 80 and wpm >= 33:
        print("PASSED")
        
        return 1
    
    else:
        print("FAIL")

        return 0


def details(result, name):
    """To store the details and log the tuts
    manages log_10 file, data_all file and data_typed_text"""

    raw_text = result[0]
    input_text = result[1]

#_________________________________________________________________________________________________________________________________
    # Making and rreading a file to read and store details of last ten attempts
    try:
        log_10 = open(f'{name}/log_10', 'r')
    except FileNotFoundError:
        log_10 = open(f'{name}/log_10', 'a+')
        log_10.write(f"0 0 0 0 0 0 0 0 0 0")
        
    log_10.seek(0)
    log_10_list = log_10.readlines()
    log_10.close()
    log_10 = open(f'{name}/log_10', 'w')
    try:
        log_10_list.pop(10)
    except IndexError:
        print(">>>size less than 10")
    
    for i in range (len(log_10_list)):
        
        text_list = list(log_10_list[i].split())
        text_list[0] = int(text_list[0])
        text_list[0] += 1
        log_10_list[i] = f"{text_list[0]} {text_list[1]} {text_list[2]} {text_list[3]} {text_list[4]} {text_list[5]}\
 {text_list[6]} {text_list[7]} {text_list[8]}\n"
    log_10_list.insert(0, f"1 {result[2]} {result[3]} {result[4]} {result[5]} {result[6]} {result[7]} {result[8]} {result[9]}\n")
                
    log_10.writelines(log_10_list)

    #_____________________________________________________________________________________________________________________________
    try:
        data_all = open(f'{name}/data', 'r')
        
    except FileNotFoundError:
        data_all = open(f'{name}/data', 'a+')
        data_all.write(f"CTY 0\nCTW 0\nCTR 0\nCTI 0\nACC 0\nTTN 0\nCPM 0\nWPM 0")

    data_all.seek(0)
    data_all_list = data_all.readlines()
    data_all.close()

    for i in range (len(data_all_list)):
        read = data_all_list[i]
        read_list = list(read.split())
        if i < 4:
            read_list[1] = int(read_list[1]) +result[i+2]
            data_all_list[i] = f"{read_list[0]} {read_list[1]}\n"
        else:
            res = 0
            for line in log_10_list:
                read_list = list(line.split())
                res += float(read_list[i+1])
            res /= len(log_10_list)
            read_list[1] = res
            data_all_list[i] = f"{read_list[0]} {read_list[1]}\n"

    data_all = open(f'{name}/data', 'w')
    data_all.writelines(data_all_list)

    #______________________________________________________________________________
    # detals pf the typed characters
    try:
        data_typed_text = open(f'{name}/data_text.txt', 'r+')

    except FileNotFoundError:
        data_typed_text = open(f'{name}/data_text.txt', 'a+')

        for i in range(33,127):
            data_typed_text.write(f"{chr(i)} 0 0\n")

        data_typed_text.close()
        data_typed_text = open(f'{name}/data_text.txt', 'r+')

    data_typed_text.seek(0)
    count_list = data_typed_text.readlines()


    # add total no. of typed characters to the file data_typed_text
    for i in input_text:
        for j in range (len(count_list)):
            read = count_list[j]
            if i == read[0]:
                read_list = list(read.split(' '))
                read_list[1] = int(read_list[1])+1
                count_list[j] = f"{read_list[0]} {read_list[1]} {read_list[2]}"
    

    # add total no. wrong characters to the file data_typed_text
    for i in  range (len(raw_text)):
        if raw_text[i] != input_text[i]:
            for j in range (len(count_list)):
                read = count_list[j]
                if raw_text[i] == read[0]:
                    read_list = list(read.split(' '))
                    read_list[2] = int(read_list[2])+1
                    count_list[j] = f"{read_list[0]} {read_list[1]} {read_list[2]}"

    for i in range(len(count_list)):
        if count_list[i][-1] != '\n':
            count_list[i] += '\n'

    
    data_typed_text.close()
    data_typed_text = open(f'{name}/data_text.txt', 'w')
    data_typed_text.seek(0)
    data_typed_text.writelines(count_list)
            
    
