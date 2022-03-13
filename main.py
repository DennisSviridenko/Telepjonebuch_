import os

def start():
    inp = input("Suchen oder Schreiben? \n >>> ")
    
    if inp == 'r':
       search()
            
            
    if inp == 'w':
        write()
    
    if inp == 'u':
        pass



def search():
    inp = input("Name eingeben! \n >>> ")
        
    try:
        f = open(f'Data\{inp}.txt', 'r')
        os.system('cls')
        print(f.read())
        
    except:
        print("Error: Datei existiert nicht!")
        os.system('cls')
        search()
        

def write():
    inp = input("Name? \n >>> ")
    
    try:
        f = open(f'Data\{inp}.txt', 'r')
        print("Error: Kontakt existiert bereits!")
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
    












if __name__ == "__main__":
    start()