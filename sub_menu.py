"""
it takes the name from the main file and selects the exercise to open in the tutorial
"""

import os

from color import color
from getch import getch
from check_word import check_word


def Chap_list(name):
    """Window to select the details of the chapter to take and returns the number"""

    # open and read the file containg the course level or if not found create it
    try:
        level = open(f'{name}/course_level', 'r')

    except:
        print(">>>Folder not found\n\
    >>>Creating new file\n\
    >>>All previous data has been reset ")
        os.mkdir(name)
        level = open(f'{name}/course_level', 'a+')
        level.write('0\n1')

    level.seek(0)
    chapter = int(level.readline())
    exercise = int(level.readline())
    level.close()

    print(f">>>You are currently at {color['red']}CHAPTER {chapter}{color['blue']} EXERCISE {exercise}{color['reset']}")

    print(">>>Enter to continue to the test\n\
          >>>Enter to continue without any change\n\
          >>>1\t:\tManually select the chapter\n\
          >>>2\t:\tView performance")
    choice = 0
    flag = 1


    while flag != 0:
        choice = input("...")

        if choice == '1':
            """
            To get from the user the manually inputted chapter and exercise
            """
            chapter = input('>>>Enter the number of the chapter\n\
                            >>>1\t:\tasdf jkl;\n\
                            >>>2\t:\tgtrewq hyuiop\n\
                            >>>3\t:\tgcvb hnm,\n\
                            >>>4\t:\tzxcv b nm,.\n\
                            >>>5\t:\t<>?: }{][|-=+-\n\
                            >>>6\t:\tCapital Letters\n\
                            >>>7\t:\tNumbers\n\
                            >>>8\t:\tSymbols\n\
                            >>>9\t:\tPractice\n\
...')
            while True:

                list = [0,1,2,3,4,5,6,7,8,]
                try:
                    chapter = int(chapter)
                    if chapter == 0:
                        pass
                    else:
                        chapter -= 1
                    if chapter in list:
                        break
                except:
                     chapter = input("Please Enter the correct choice\n...")

            file = open(f'courses/course_{chapter+1}', 'r')
            count = len(file.readlines())
            file.close()
            exercise = input(f">>>Choose exercises between 1 to {count+1}\n...")
            while True:
                try:
                    exercise = int(exercise)
                    if exercise <= count:
                        break
                    break
                except:
                    exercise = input("Please Enter the correct number for the EXERCISE\n...")
            flag = 0



            chapter = int(chapter)
            exercise = int(exercise)

            text = get_text(chapter, exercise)     # To get the text from course file

            # make a while loop to check and rerun or quit program also modify the log and data file
            result = check_word(text, name)         #Run the typimg tut 
            
            while True:
                if result == 0:
                    
                    print(">>>Press Enter to continue\n\
                        >>>Press anyother key to exit")
                    k = getch()
                    if k == '\n':
                        result = check_word(text, name)         #Run the typimg tut
                    else:
                        exit()
                    
                elif result == 1:
                    print(">>>Enter to continue to next lesson\n\
                                >>>Any other key to quit")
                    k = getch()

                    if k == '\n':
                        try:
                            exercise += 1
                            file = open(f'{name}/course_level', 'w')
                            file.write(f'{chapter}\n{exercise}')
                            text = get_text(chapter, exercise)
                            result = check_word(text, name)
                        except:
                            chapter += 1
                            exercise = 0
                            file = open(f'{name}/course_level', 'w')
                            file.write(f'{chapter}\n{exercise}')
                            text = get_text(chapter, exercise)
                            result = check_word(text, name)
                        

                    else:
                        try:
                            exercise += 1
                            file = open(f'{name}/course_level', 'w')
                            file.write(f'{chapter}\n{exercise}')
                            text = get_text(chapter, exercise)
                        except:
                            chapter += 1
                            exercise = 0
                            file = open(f'{name}/course_level', 'w')
                            file.write(f'{chapter}\n{exercise}')
                            text = get_text(chapter, exercise)
                        else:
                            print(">>>You are now ready to dive into real world practice\n>>>GOOD BYE")
                        finally:
                            print("GOOD BYE")
                            exit()

        # To view the performance of the profile
        elif choice == '2':
            performance(name)
            print(">>>Press Enter to continue to the test\n\
                >>>Anything else to exit")
            
            input_perf = getch()
            
            if input_perf == '\n':
                Chap_list(name)

            else:
                exit()            

            flag = 0


        elif choice == '' or choice =='\n':
            print(">>>You have chosen to continue with prevous session")
            flag = 0

        else:
            print(">>>Please, Enter the correct choice")




# To create a function to display performance for the said profile
def performance(name):
    file = open(f'{name}/data', 'r')

    list_data = file.readlines()

    print(list_data)
    
    print(" no performance till now buddy")


# To create a function to get text from course_read file

def get_text(chapter, exercise):
    '''to read the course files in the course folder
    enter the chapter no and exercise number to get string'''

    count = 0
    list = os.listdir('courses')
    list.sort()

    file = open(f'courses/{list[chapter]}', 'r')
    for i in range(exercise):
        text = file.readline()
    file.close()
    text = text.strip('\n')
    return text
