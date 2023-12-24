"""To make the program for Typing tutor"""

import os

import sub_menu

from color import color

def mainscreen():
    """To select the module for initiation"""
    print(">>>Select the option \n\
          1\t:\tSelect existing profile\n\
          2\t:\tCreate new profile\n\
          3\t:\tEdit Tests\n\
          4\t:\tExit\n")
    choice = input("...")

    #to check if the profile file already exists or not1
    try:
        file = open("profile", 'r')

    except:
        file = open("profile", 'a+')
    profile_list = []
    file.close

    #to make a list of the names of the profiles logged into the file
    while True:
        profile_list = file.readlines()
        if not profile_name:
            break
        profile_name = profile_name.rstrip('\n')
        profile_list.append(profile_name)
        if not profile_name:
            break
    #print(profile_list)
    flag = 1
    while flag == 1:

        #for opening an existing profile
        if choice == '1':
            flag = 0
            count = 0
            print(">>>Please select the profile")
            for i in profile_list:
                count+=1
                print(f">>>{count}\t:\t{color['cyan']}{i}{color['reset']}")
            number = input("...")
            flag1 = 1
            while flag1 == 1:
                try:
                    number = int(number)
                    flag1 =0

                except:
                    print(f">>>You have entered incorrect choice\n\
                          please enter a value between 1 and {len(profile_list)}")
                    
                    number = input("...")

            if number == 0:
                pass
            else:
                number -= 1
            name = profile_list[number]
            print(f">>>You have chosen {color['bright_cyan']}{color['bold']}{name}{color['reset']}")
            sub_menu.Chap_list(name)

        #for  creating a new profile
        elif choice == '2':
            flag = 0
            name = input(">>>Enter the name of the new user\n...")

            flag = 1
            while flag == 1:
                #taking the name of the new profile again if the name is too long
                if(len(name) > 32):
                    print("The name is too long\n\
                        Enter a name with less than 32 characters")
                    name = input("\n...")
                
                #to check if a profile with a same name exists or not
                elif name in profile_list:
                    print(">>>Profile with same name already exists\n\
                          Enter a new name")
                    name = input("\n...")

                else:
                    flag = 0
            
            file = open("profile", 'a+')
            file.write(f"\n{name}")
            print(f">>>You have created a new profile '{name}'")
            file.close
            sub_menu.StatusScreen(name)

        #to edit the tests
        elif choice == '3':
            
            flag = 0
        
        elif choice == '4':
            flag = 0
            file = exit()
        
        else:
            print(">>>Please enter a correct choice")
            choice =input("...")
        

        #choice = '0'


mainscreen()