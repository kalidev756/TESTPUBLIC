
from colorama import Fore
import random
import os
import time
import subprocess
#couleure aléatoire

logo=((Fore.MAGENTA) + """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                                                                          
_____                                      _ _          
/ ____|                                    (_) |         
| |     ___  _ __ ___  _ __ ___  _   _ _ __  _| |_ _   _  
| |    / _ \| '_ ` _ \| '_ ` _ \| | | | '_ \| | __| | | | 
| |___| (_) | | | | | | | | | | | |_| | | | | | |_| |_| | 
\_____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|_|\__|\__, | 
_    _            _      ______ _____              __/ | 
| |  | |          | |    |  ____|  __ \            |___/  
| |__| | __ _  ___| | __ | |__  | |__) |                  
|  __  |/ _` |/ __| |/ / |  __| |  _  /                   
| |  | | (_| | (__|   <  | |    | | \ \                   
|_|  |_|\__,_|\___|_|\_\ |_|    |_|  \_\    
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
        ⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀
        ⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
        ⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
        ⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
        ⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
        ⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
        ⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      """)

#time sleep
def sleep2():
    time.sleep(2)
# security 
def sensible_verify():
    for i in range(300):
            print(" ")
            print(logo)
            print(Fore.RED+"____________________________________________________________________________________________________________")
            print(Fore.RED+"fr: NOUS NE SOMMES EN AUCUN CAS RESPONSABLE DE LA MAUVAISE UTILISATION DE CE TOOL, TITRE EDUCATIF UNIQUEMENT")
            print(Fore.RED+"en: we are not responsable if you use this tool for unhetickal action")
            time.sleep(1)
            for i in range(300):
                print("")
            print(logo)
            print(Fore.RED+"AUTHENTIFICATION REQUIRED: CRITICAL FONCTION")
            acces_attacks=input(">>")
            if acces_attacks=="123456":
                print("succes!")
                principal_menu()
                
            else:
                print("unable to verify, back to main meunu")
                time.sleep(2)
                principal_menu()






###################APLICATIVE################
#osint aplicative

#learning aplicative



#attacks aplicative

def zphisher():

    for i in range(400):
        print(" ")
    print(logo)
    print(Fore.MAGENTA+"________")
    print("lancement...")
    time.sleep(2)
    choice_attack="2"
    if choice_attack == "1":
        print("fonction isn't available")
        time.sleep(2)
        principal_menu()
    elif choice_attack=="2":
        confirmation=input("confirm action?(y/n)")
        if confirmation=="y":
            print("start...")
            time.sleep(2)
            for i in range(300):
                print(" ")
            result = subprocess.run(["git", "clone", "--depth=1", "https://github.com/htr-tech/zphisher.git"])

            if result.returncode == 0:
                print("Succès !")
            else:
                print("An error occurred while cloning the repository.")

            os.chdir("zphisher")
            subprocess.call(['bash', 'zphisher.sh'])
        elif confirmation=="n":
            principal_menu()
        else:
            print("error, back to main meunu")
            time.sleep(1)
            principal_menu()
    elif choice_attack == "q":
        principal_menu()
    else:
        print("error when entering the option (q for the main menu)")
        time.sleep(2)
        principal_menu()

#security alicative

#other aplicative


#start meunu

def principal_menu():
    for i in range(400):
        print(" ")
    print(logo)
    print(Fore.GREEN +"____________________________________________________________________________________________________________")
    print(f"\033[91m[\033[97m01\033[91m]\033[33m Course        |  _________________________**version 2.3.5**________________________")
    print(f"\033[91m[\033[97m02\033[91m]\033[33m Tools         |  Original repository: ")
    print(f"\033[91m[\033[97m03\033[91m]\033[33m SandBox       |  Dev: ")
    print(f"\033[91m[\033[97m04\033[91m]\033[33m Training      |  Dev: ")
    print(f"\033[91m[\033[97m05\033[91m]\033[33m other         |")
    meunu()


#meunu_background

def meunu():
   
    meunu_sub_choose=input(">>")
    if meunu_sub_choose=="1":
        space_logo()
        long37()
        print(f"\033[91m[\033[97m01\033[91m]\033[33m courses1       ")
        print(f"\033[91m[\033[97m02\033[91m]\033[33m courses2       ")
        print(f"\033[91m[\033[97m03\033[91m]\033[33m courses3       ")
        print(f"\033[91m[\033[97m04\033[91m]\033[33m courses4       ")
        print(f"\033[91m[\033[97m05\033[91m]\033[33m courses5       ")
        meunu_sub_sub_courses=input(">>")
        if meunu_sub_sub_courses=="1":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m courses x     ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m courses x     ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m courses x     ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m courses x     ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m courses x     ")
            print("unvailidable") 
            back_to_main_meunu()
        elif meunu_sub_sub_courses=="2":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m courses x      ")
            print("unvailidable") 
            back_to_main_meunu()
        elif meunu_sub_sub_courses=="3":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m courses x      ")
            print("unvailidable") 
            back_to_main_meunu()
        elif meunu_sub_sub_courses=="4":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m courses x      ")
            print("unvailidable") 
            back_to_main_meunu()
        elif meunu_sub_sub_courses=="5":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m courses x      ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m courses x      ")
            print("unvailidable") 
            back_to_main_meunu()
        elif meunu_sub_choose=="q":
            principal_menu()
        else:
            print("error")
            principal_menu()
        principal_menu
    elif meunu_sub_choose=="2":
        space_logo()
        long37()
        print(f"\033[91m[\033[97m01\033[91m]\033[33m Physhing")
        print(f"\033[91m[\033[97m02\033[91m]\033[33m tools   ")
        print(f"\033[91m[\033[97m03\033[91m]\033[33m tools   ")
        print(f"\033[91m[\033[97m04\033[91m]\033[33m tools   ")
        print(f"\033[91m[\033[97m05\033[91m]\033[33m tools   ")
        meunu_sub_sub_tools=input(">>")
        if meunu_sub_sub_tools=="1":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m Zphisher     ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m tools x   ")
            last_choose=input(">>")
            if last_choose=="1":
                space_logo()
                zphisher()
            elif last_choose =="q":
                principal_menu()
            else:
                back_to_main_meunu()
        elif meunu_sub_sub_tools=="2":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m tools x   ") 
            back_to_main_meunu()
        elif meunu_sub_sub_tools=="3":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m tools x   ") 
            back_to_main_meunu()
        elif meunu_sub_sub_tools=="4":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m tools x   ")  
            back_to_main_meunu()
        elif meunu_sub_sub_tools=="4":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m tools x   ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m tools x   ")  
            back_to_main_meunu()
        elif meunu_sub_choose=="q":
            principal_menu()
        else:
            print("error")
            principal_menu()
    elif meunu_sub_choose=="3":
        space_logo()
        long37()
        print(f"\033[91m[\033[97m01\033[91m]\033[33m SandBox1   ")
        print(f"\033[91m[\033[97m02\033[91m]\033[33m SandBox2   ")
        print(f"\033[91m[\033[97m03\033[91m]\033[33m SandBox3   ")
        print(f"\033[91m[\033[97m04\033[91m]\033[33m SandBox4   ")
        print(f"\033[91m[\033[97m05\033[91m]\033[33m SandBox5   ")
        meunu_sub_sub_SandBox=input(">>")
        if meunu_sub_sub_SandBox=="1":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m SandBox x   ")
            back_to_main_meunu()
        elif meunu_sub_sub_SandBox=="2":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m SandBox x   ") 
            back_to_main_meunu()
        elif meunu_sub_sub_SandBox=="3":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m SandBox x   ") 
            back_to_main_meunu()
        elif meunu_sub_sub_SandBox=="4":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m SandBox x   ") 
            back_to_main_meunu()
        elif meunu_sub_sub_SandBox=="5":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m SandBox x   ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m SandBox x   ") 
            back_to_main_meunu()
        elif meunu_sub_choose=="q":
            principal_menu()
        else:
            print("error")
            principal_menu()
    elif meunu_sub_choose=="4":
        space_logo()
        long37()
        print(f"\033[91m[\033[97m01\033[91m]\033[33m unvailidable1   ")
        print(f"\033[91m[\033[97m02\033[91m]\033[33m unvailidable2   ")
        print(f"\033[91m[\033[97m03\033[91m]\033[33m unvailidable3   ")
        print(f"\033[91m[\033[97m04\033[91m]\033[33m unvailidable4   ")
        print(f"\033[91m[\033[97m05\033[91m]\033[33m unvailidable5   ")
        meunu_sub_sub_unvailidable=input(">>")
        if meunu_sub_sub_unvailidable=="1":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m unvailidable x  ")
            last_choose=input(">>")
            if last_choose=="1":
                print("error when entering the option (q for the main menu)")
                
            elif last_choose=="q":
                principal_menu()
            else:
                back_to_main_meunu()

            
        elif meunu_sub_sub_unvailidable=="2":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m unvailidable x  ") 
            back_to_main_meunu()
        elif meunu_sub_sub_unvailidable=="3":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m unvailidable x  ") 
            back_to_main_meunu()
        elif meunu_sub_sub_unvailidable=="4":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m unvailidable x  ") 
            back_to_main_meunu()
        elif meunu_sub_sub_unvailidable=="5":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m unvailidable x  ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m unvailidable x  ")
            back_to_main_meunu()
        else:
            principal_menu()
    
    elif meunu_sub_choose=="5":
        space_logo()
        long37()
        print(f"\033[91m[\033[97m01\033[91m]\033[33m other  ")
        print(f"\033[91m[\033[97m02\033[91m]\033[33m other  ")
        print(f"\033[91m[\033[97m03\033[91m]\033[33m other  ")
        print(f"\033[91m[\033[97m04\033[91m]\033[33m other  ")
        print(f"\033[91m[\033[97m05\033[91m]\033[33m other  ")
        meunu_sub_sub_other=input(">>")
        if meunu_sub_sub_other=="1":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m otherex  ")
            back_to_main_meunu()
        elif meunu_sub_sub_other=="2":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m otherex  ")
            print("unvailidable") 
            back_to_main_meunu()
        elif meunu_sub_sub_other=="3":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m otherex  ")
            print("unvailidable") 
            back_to_main_meunu()
        elif meunu_sub_sub_other=="4":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m otherex  ")
            print("unvailidable") 
            back_to_main_meunu()
        elif meunu_sub_sub_other=="5":
            space_logo()
            long37()
            print(f"\033[91m[\033[97m01\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m02\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m03\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m04\033[91m]\033[33m otherex  ")
            print(f"\033[91m[\033[97m05\033[91m]\033[33m otherex  ")
            print("unvailidable") 
            back_to_main_meunu()
        else:
            principal_menu()

#other

def back_to_main_meunu():
    long37()
    print("An error has occured, back ton main mennu")
    print("please verivy any options are availible")
    time.sleep(2)
    principal_menu()

def long37():
    print("____________________________________________________________________________________________________________///")

def space_logo():
    for i in range(400):
        print()
    print(logo)

principal_menu()