from os import system

def start_user_enviroment():
    print("This is Going to be user Enviroment")

def compare_strings(compare):
    """Compares with user_input

    Args:
        compare (string): compares two string

    Returns:
        bool : True if user_input is the same as (compare) 
    """
    if(get_user_input(compare)):
        return True
    return False

def get_user_input(prompt):
    """Gets users input

    Args:
        input (string): prompt

    Returns:
        string: The users input
    """
    return input(f"{prompt} \n > ")

def main_menu(first_run):
    RUNNING = True
    c_Running = True 
    first_run = True
    
    while(c_Running):
        if(not first_run):
            user_input = ""


        print("MAIN MENU")
        print()
        print("    1:  ")
        print("    2: [COMING SOON]")
        print("    3: [COMING SOON]")
        print("    4: [COMING SOON]")
        print("    5: [Exit]")
    
        user_input = get_user_input("Please select option")
        if(user_input == "1"):
            start_user_enviroment()
        if(user_input == "5"):
            print("See you soon!")
            RUNNING = False 
            c_Running = False
        else: print("Still In Developement")
        
    
        first_run = False
        system("clear")
        
    return 0


if __name__=="__main__":
    running = True 
    
    while(running):
        running = main_menu(running)   # --> Works // running = returns error_code and debug info


#TODO Login System
#TODO Documentation
