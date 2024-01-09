''' 
To make a proogram that runs typing tutorial in Terminal'''

import os
from subprocess import call
from getch import getch
from time import time




class Tutorial:
    def __init__(self) -> None:
        """Initiating the name variable and empty profile list"""
        self.name       = ''
        self.profiles   = []

        # Lambda function to clear screen
        self.cls = lambda: os.system('cls' if os.name=='nt' else 'clear')


    def run(self):
        '''Initiate the function for the first time'''
        try:
            with open('profile.s', 'r') as f:
                # Comment: 
                profile_list = f.readlines()
                profile_list = list(map(lambda i: i.strip('\n'), profile_list))
            # end readline file
                self.profiles = profile_list
                self.choices()
        except FileNotFoundError:
            self.createAndGet()


    def choices(self):
        '''gives the user choice to continiue with the previous profile or '''
        """To select the module for initiation"""
        print(">>>Select the option \n>>>Press 'Return' to continue\n\
        1\t:\tSelect existing profile\n\
        2\t:\tCreate new profile\n\
        3\t:\tEdit Tests\n\
        4\t:\tExit\n")

        
        choice = input("...")
        if choice == '':
            try:
                with open('lastProfile', 'r') as f:
                    # Comment: lastProfile
                    name = f.readline()
                    # end for
                # end readline file
                subMenu().Chap_list(name)
                    
            except FileNotFoundError:
                if self.profiles == []:
                    self.getName()
                else:
                    self.selectProfile()


        else:
            check = self.checkChoice(choice, 1, 5)
            if check == 1:
                print(f'>>>You have chosen {choice}')
                choice = int(choice)
                if choice == 1:
                    self.selectProfile()
                elif choice == 2:
                    self.getName()
                elif choice == 3:
                    self.editTest()
                else:
                    print("Exiting as per your WISH")
                    exit()
            else:
                self.choices()
        

    def createAndGet(self):
        ''' Executes when there is no profile.s file in the dir'''
        print(">>> No Profile found in memory\n")
        self.getName()


    def getName(self):
        '''Gets the name from the user
        saves it in the profile.s file
        then runs the program to start the test
        '''
        print(">>>Enter the New Profile Name\n")

        self.name = input("...")
        for i in self.name:
            if not i.isalpha():
                print(">>>Name should only consist of Alphabets")
                self.getName()
            elif len(self.name) not in range(4,32):
                print(">>>The length of the name should be between 4 to 32 characters")
                self.getName()
            else:
                with open('profile.s', 'a') as f:
                    # Comment: write the profile name in the file
                    f.write(f'{self.name}\n')
                # end append file
                break
        
        subMenu().Chap_list(self.name)

    
    def selectProfile(self):
        '''Gets the name list from the profile.s file
        then prompts the user to select one and then
        takes user to the profile page'''
        print(">>>Please enter the number of the profile to proceed with to profile page")
        for i in self.profiles:
            print(f">>>{self.profiles.index(i) + 1}     :   {i}")
        choice = input("...")
        check = self.checkChoice(choice, 1, len(self.profiles)+1)

        if check == 1:
            choice = int(choice)
            self.name = self.profiles[choice-1]
            
            subMenu().Chap_list(self.name)
        else:
            self.selectProfile()


    def editTest(self):
        '''
        Takes the number of the course file that user wants to edit
        Open Editor for the file
        Note: VIM editor is neccessary for this thing'''
        print(">>>Enter the number of the course file that you want to edit\n\
              >>>Note: VIM editor is neccessary for this thing")
        coursesList = os.listdir("courses")
        coursesList.sort()
        for item in coursesList:  # import os
            # Comment: 
            print(coursesList.index(item)+1, '    :   ', item)
        # end file item
            
        choice = input('...')
        check = self.checkChoice(choice, 1, len(coursesList)+1)
        if check == 1:
                choice = int(choice)-1
                print(f'>>>You have chosen {coursesList[choice]}')
                
                EDITOR = os.environ.get('EDITOR','vim') #that easy!

                initial_message = "" # if you want to set up the file somehow
                # Openig file in append mode and sending it to vim for editing
                with open(f'courses/{coursesList[choice]}','a+',encoding='utf-8') as tf:
                    tf.write(initial_message)
                    tf.flush()
                    #Opening Editor
                    call([EDITOR, tf.name])
                # Opening the Edited file and showing the results of the editing
                with open(f'courses/{coursesList[choice]}','r',encoding='utf-8') as tf:
                    print('>>> The Edited file is shown:\n\n')
                    edited_message = tf.read()
                    print (edited_message)

                # Returning back to main menu
                print(f"{'*'*90}\n>>>Press any key to continue to Main Menu")
                getch()
                self.run()
        else:
            self.editTest()


    def checkChoice(self, choice,  min, max):
        ''' To check if the numerical inputs requested from the user are in the specified type and range or not'''
        try:
            choice = int(choice)
            if choice in range(min, max):
                return 1
            else:
                print(">>>Inpur Out of bounds\n>>>Please, Enter an integer value within specified range")
                return 2
        except ValueError:
            print(">>>Invalid Input Type\n>>>Please, Enter an integer value within specified range")
            return 2
        


class subMenu(Tutorial):
    """
    it takes the name from the main file and selects the exercise to open in the tutorial
    """

    def __init__(self) -> None:
        super().__init__()


    def Chap_list(self, name):
        """Window to select the details of the chapter to take and returns the number"""
        # open and read the file containg the course level or if not found create it
        try:
            with open(f'{name}/course_level', 'r') as level:
                chapter = int(level.readline())
                exercise = int(level.readline())

        except FileNotFoundError:
            print("\
            >>>Profile Folder not found\n\
            >>>Creating new file\n\
            >>>All previous data has been reset ")
            os.mkdir(name)
            try:
                with open(f'{name}/course_level', 'a+') as level:
                    level.write('0\n1')
            except FileExistsError:
                with open(f'{name}/course_level', 'a+') as level:
                    level.write('0\n1')

        print(f">>>You are currently at {color['red']}CHAPTER {chapter}{color['blue']} EXERCISE {exercise}{color['reset']}")
        self.getChapter(name)


    def getChapter(self, name):
        print(">>>Enter to continue to the test\n\
        >>>Enter to continue without any change\n\
        >>>1\t:\tManually select the chapter\n\
        >>>2\t:\tView performance\n\
        >>>3\t:\tReturn to Main Menu")
        
        choice = input("...")
        if choice == '':
            with open(f'{name}/course_level', 'r') as f:
                list = f.readlines()
                chapter = int(list[0])
                exercise = int(list[1])
            print(f"You have chosen to continue with {color['red']}CHAPTER {chapter}{color['blue']} EXERCISE {exercise}{color['reset']}")
            self.getText(chapter, exercise, name)
        else:
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
                >>>9\t:\tPractice\n\n...')
            
                check = self.checkChoice(chapter, 1, 10)
                if check == 1:
                    chapter = int(chapter)
                    self.getExercise(chapter, name)
                else:
                    print('>>>Please Enter the values within the specified range\n')
                    self.getChapter(name)

                    # To view the performance of the profile
            elif choice == '2':
                self.performance(name)


            elif choice == '3':
                Tutorial().run()

        


            else:
                print(">>>Please, Enter the correct choice")
                self.getChapter(name)


    def performance(self, name):
        with open(f'{name}/data', 'r') as file:

            list_data = file.readlines()

        print(list_data)
        
        print(" no performance till now buddy")


    def getExercise(self, chapter, name):
        '''Checks the number of the available exercises in thefile'''
        with open(f'courses/course_{chapter}', 'r') as file:
            count = len(file.readlines())
            exercise = input(f">>>Choose exercises between 1 to {count+1}\n...")
            check = self.checkChoice(exercise, 1, count+1)
            if check == 1:
                exercise = int(exercise)-1

                self.getText(chapter, exercise, name)
            else:
                print('>>>Please Enter the values within the specified range\n')
                self.getExercise(chapter, name)


    def getText(self, chapter, exercise, name):
        '''to read the course files in the course folder
        enter the chapter no and exercise number to get string'''

        list = os.listdir('courses')
        list.sort()

        with open(f'courses/{list[chapter]}', 'r') as file:
            textList = file.readlines()
        text = textList[exercise].strip('\n')
        
        result = checkWord().check_word(text, name)         #Run the typimg tut 
        self.checkResult(result, text, name, chapter, exercise)


    def checkResult(self, result, text, name, chapter, exercise):

        with open('lastProfile', 'w') as f:
            # Comment: save the name to the lastProfile file for use in the Main Menu
            f.write(f'{name}')
        # end overwrite file
        while True:
                if result == 0:
                    
                    print(">>>Press Enter to continue\n\
                    >>>Press anyother key to exit")
                    k = getch()
                    if k == '\n':
                        result = checkWord().check_word(text, name)         #Run the typimg tut
                    else:
                        exit()
                    
                elif result == 1:
                    #Incrementing the exercise
                    try:
                        exercise += 1
                        file = open(f'{name}/course_level', 'w')
                        file.write(f'{chapter}\n{exercise}')
                    #Incremnting the Chapter
                    except IndexError:
                        chapter += 1
                        exercise = 0
                        file = open(f'{name}/course_level', 'w')
                        file.write(f'{chapter}\n{exercise}')

                    print(">>>Enter to continue to next lesson\n\
                    >>>Space to return to Main Menu\
                    >>>Any other key to quit")
                    k = getch()
                    if k == '\n':
                        #    Running the next exercise
                        text = self.getText(chapter, exercise, name)
                    elif k == ' ':
                        #Returnintg to the home
                        Tutorial().run()
                    else:
                        #Obiously Exiting
                        exit()
                else:
                    #End of the stored Chapters
                    print(">>>You are now ready to dive into real world practice\n>>>GOOD BYE")
                    exit()
    


class checkWord(subMenu):

    def __init__(self) -> None:
        super().__init__()

        
    def check_word(self, text, name):
        """ To check correctness of the typing tutorial while using """
        #variables
        lengthText      = len(text)
        lenDisp         = int((os.popen('tput cols')).read())      # To measure the width of the terminal
        lenHeight         = int((os.popen('tput lines')).read())//2      # To measure the width of the terminal
        lenTypedDisp    = lenDisp//2
        listWord        = list(text.split())
        lenListW        = len(listWord)

        count       = 0
        countLetter = 0
        countWord   = 0
        countLRight = 0 
        countWRight = 0 
        countLWrong = 0 
        countWWrong = 0 

        typedL      = ''
        typedW      = ''
        inputL      = ''
        inputLUF    = ''
        string      = ''

        startTime = time()      # Taking the starting time of the test

        print(text)

        while countWord < lenListW:
             
            counter = 0
            flag = 0
            # To add space after the word except the last one
            if countWord != lenListW -1:
                typedW = listWord[countWord] + ' '
            else:
                typedW = listWord[countWord]
            countLetter = len(typedW)
            # To check if the typed word is same as the inputed word
            while counter < countLetter:
                
                key = getch()      # Get the key press from the user
                self.cls()

                print('\n' * lenHeight)
                inputLUF += key
                # To make a string for the typed words
                if key == typedW[counter]:
                    typedL += f"{color['green']}{typedW[counter]}"
                    inputL += f"{color['green']}{key}"
                else:
                    print('\a', end = '\r')
                    flag = 1
                    typedL += f"{color['bright_red']}{typedW[counter]}{color['green']}"
                    inputL += f"{color['bright_red']}{key}{color['green']}"

#                 self.cls()       # Clear screen

#               # To print the string 
                
                if count < lenTypedDisp:
                    print(f"{typedL}{color['bright_blue']}{color['bold']}{color['bg_white']}{text[count+1]}{color['reset']}{color['bright_yellow']}{text[count+2:count+lenTypedDisp]}{color['reset']}")
                elif count >= lenTypedDisp and lengthText - count > lenTypedDisp -1:
                    print(f"{typedL[-lenTypedDisp-2:]}{color['bright_blue']}{color['bold']}{color['bg_white']}{text[count+1]}{color['reset']}{color['bright_yellow']}{text[count+2:count+2+lenTypedDisp-1]}{color['reset']}")
                elif lengthText - count < lengthText - lenTypedDisp -1:
                    try:
                        print(f"{typedL[-lenTypedDisp-2:]}{color['bright_blue']}{color['bold']}{color['bg_white']}{text[count+1]}{color['reset']}{color['bright_yellow']}{text[count+2:]}{color['reset']}")
                    except IndexError:
                        print(f"{typedL}FOURTH")
                    
                counter += 1
                count += 1

            # try:
            #     string += typedL
            # except:
            #     string += typedL 
            string += typedL 

            if flag == 1:
                countWWrong += 1
            else:
                countWRight += 1

            countWord += 1

        endTime  = time()       # Taking the end time of the test

        print(f"{inputL}{color['reset']}")

        timeTaken = endTime - startTime
        accuracy = (countWRight/countWord)*100
        WPM = countWord/(timeTaken/60)
        CPM = count/(timeTaken/60)

        # To print the results and parameters of the test
        print('-'*lenDisp)
        print(f">>>Total words = {countWord}\n>>>Correct words = {countWRight}\n>>>Wrong words = {countWWrong}")
        print(f">>>Accuracy = {accuracy:.2f}%")
        print(f">>>Time taken = {timeTaken:.2f}")
        print(f">>>Total keys pressed = {count}")
        print(f">>>CPM = {CPM:.2f}")
        print(f">>>WPM = {WPM:.2f}")
        print('-'*lenDisp)


        dictDetails = {'text' : text, 'inputLUF' : inputLUF, 'count' : count, 'countWord' : countWord, 'countWRight' : countWRight, 'countWWrong' : countWWrong, 'accuracy' : int(accuracy),'timeTaken' : int(timeTaken), 'CPM' : int(CPM), 'WPM' : int(WPM)}

        self.details(dictDetails, name)
        # To return different values from the result of the test to the parent file
        if accuracy >= 80 and WPM >= 33:
            print("PASSED")
            return 1      
        else:
            print("FAIL")
            return 0



    def details(self, result, name):
        """To store the details and log the tuts
        manages log_10 file, data_all file and data_typed_text"""

        raw_text = result['text']
        input_text = result['inputLUF']

    #_________________________________________________________________________________________________________________________________
        # Making and reading a file to read and store details of last ten attempts
        
        with open(f'{name}/test.log', 'a+') as testLog:
            testLog.seek(0)
            if testLog.read(10) == '':
                testLog.write("0 0 0 0 0 0 0 0 0\n")
            testLog.seek(0)
            logList = testLog.readlines()
            try:
                logList.pop(100)
                print(">>>Popped the last entry")
            except IndexError:
                print(">>>Log size currently less than 100")

            testLog.seek(0)
            testLog.write(f"{result['count']} {result['countWord']} {result['countWRight']} {result['countWWrong']} {result['accuracy']} {result['timeTaken']} {result['CPM']} {result['WPM']}\n")

        #_____________________________________________________________________________________________________________________________
        

    

"""A dictionary to control colour of the text"""

color = {
  'reset': '\x1b[0m',
  'bold': '\x1b[1m',
  'italic': '\x1b[3m',
  'underline': '\x1b[4m',
  'inverse': '\x1b[7m',

  'black': '\x1b[30m',
  'red': '\x1b[31m',
  'green': '\x1b[32m',
  'yellow': '\x1b[33m',
  'blue': '\x1b[34m',
  'magenta': '\x1b[35m',
  'cyan': '\x1b[36m',
  'white': '\x1b[37m',
  'gray': '\x1b[90m',
  'bright_red': '\x1b[91m',
  'bright_green': '\x1b[92m',
  'bright_yellow': '\x1b[93m',
  'bright_blue': '\x1b[94m',
  'bright_magenta': '\x1b[95m',
  'bright_cyan': '\x1b[96m',
  'bright_white': '\x1b[97m',

  'bg_black': '\x1b[40m',
  'bg_red': '\x1b[41m',
  'bg_green': '\x1b[42m',
  'bg_yellow': '\x1b[43m',
  'bg_blue': '\x1b[44m',
  'bg_magenta': '\x1b[45m',
  'bg_cyan': '\x1b[46m',
  'bg_white': '\x1b[47m',
  'bg_gray': '\x1b[100m',
  'bg_bright_red': '\x1b[101m',
  'bg_bright_green': '\x1b[102m',
  'bg_bright_yellow': '\x1b[103m',
  'bg_bright_blue': '\x1b[104m',
  'bg_bright_magenta': '\x1b[105m',
  'bg_bright_cyan': '\x1b[106m',
  'bg_bright_white': '\x1b[107m'
}











run = Tutorial()
run.run()