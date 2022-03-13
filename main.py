import os
import time

def start():
    inp = input("Suchen, Schreiben oder aktualisieren? \n >>> ")
    
    if inp == 'r':
       search()
            
            
    if inp == 'w':
        write()
    
    if inp == 'a':
        apend()



def search():
    os.system("cls")
    inp = input("Name eingeben! \n >>> ")
        
    try:
        f = open(f'Data\{inp}.txt', 'r')
        os.system('cls')
        print(f.read())
        f.close()
        
    except:
        print("Error: Datei existiert nicht!")
        time.sleep(3)
        os.system('cls')
        search()
        

def write():
    os.system("cls")
    inp = input("Name? \n >>> ")
    
    try:
        f = open(f'Data\{inp}.txt', 'r')
        print("Error: Kontakt existiert bereits!")
        time.sleep(3)
        os.system('cls')
        write()
        
    except:
        f = open(f'Data\{inp}.txt', 'a+')
    
        inp = input("Theleponnummer? \n >>>")
        f.write(f"Tel. {inp} \n")
    
        inp = input("Addresse? \n >>>")
        f.write(f"Addr. {inp} \n")
    
        inp = input("Email? \n >>>")
        f.write(f"Mail. {inp} \n")
        
        f.close()
    

def apend():
    os.system("cls")
    inp_f = input("Name? \n >>>")
    
    try:
        f = open(f'Data\{inp_f}.txt', 'r')
        tel = f.readline()
        addr = f.readline()
        mail = f.readline()
        f.close()
        
        f = open(f'Data\{inp_f}.txt', 'w')
        
        
        inp = input(f"Ist {tel} richtig? \n >>>")
        if inp == "j":
            f.write(f"{tel}")
            f.close()
            f = open(f'Data\{inp_f}.txt', 'a')
        
        if inp == "n":
            inp = input("Zu was editen? \n >>>")
            f.write(f"Tel. {inp} \n")
            f.close()
            f = open(f'Data\{inp_f}', "a")
        
        
        inp = input(f"Ist {addr} richtig? \n >>>")
        if inp == "j":
            f.write(f"{addr} \n")
        
        if inp == "n":
            inp = input("Zu was editen?")
            f.write(f"Addr. {inp} \n")
        
        
        inp = input(f"Ist {mail} richtig? \n >>>")
        if inp == "j":
            f.write(f"{mail} \n")
            f.close()
        
        if inp == "n":
            inp = input("Zu was editen? \n >>>")
            f.write(f"Mail. {inp} \n")
            f.close()
        
        
    except:
        print("Error: dieser kontakt existiert nicht!")
        time.sleep(3)
        os.system('cls')
        apend()








if __name__ == "__main__":
    start()