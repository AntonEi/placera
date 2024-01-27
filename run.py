import gspread
from google.oauth2.service_account import Credentials 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('placera')

def explore_tech_options():
    """
    Explore additional options in the Tech category.
    Display a menu for Tech option, asking the user to choose an option
    """
    print("Choose a keyword to explore Tech options:")
    print("[1] Partnerships")
    print("[2] Market Expansion")
    print("[3] Product Launch")
    print("[4] Stock Buyback Program")
    print("[5] Supply Chain  Updates")
    print("[6] Industry Awards\n")
    print("[0] Exit program")

    ## Option field
    option = int(input("Enter your option: "))

    while option != 0:
        if option == 1:
            print('Partnerships')
        elif option == 2:
            print('Market Expansion')
        elif option == 3:
            print('Product Launch')
        elif option == 4:
            print('Stock Buyback Program')
        elif option == 5:
            print('Supply Chain  Updates')
        elif option == 6:
            print('Industry Awards')
        else:
            print("Invalid option.")
            explore_tech_options()
        
        print("thanks")
        explore_tech_options()
        option = int(input("Enter your option: "))

def explore_medical_options():
    """
    Explore additional options in the Medical category.
    Display a menu for Tech option, asking the user to choose an option
    """
    print("Choose a keyword to explore Medical options:")
    print("[1] FDA approval")
    print("[2] Fas 1")
    print("[3] Fas 2")
    print("[4] Fas 3")
    print("[5] EMA approval")
    print("[6] Product Launches\n")
    print("[0] Exit program")

    ## Option field
    option = int(input("Enter your option: "))

    while option != 0:
        if option == 1:
            print('FDA approval')
        elif option == 2:
            print('Fas 1')
        elif option == 3:
            print('Fas 2')
        elif option == 4:
            print('Fas 3')
        elif option == 5:
            print('EMA approval')
        elif option == 6:
            print('Product Launches')
        else:
            print("Invalid option.")
            explore_tech_options()
        
        print("thanks")
        explore_tech_options()
        option = int(input("Enter your option: "))
        
def get_stock_preference():
    """
    Welcome message and user instructions.
    Get information to assist in finding your next stock.
    """
    # Welcome message
    print("Greetings! You've just stepped into the world of StockTrigger,")
    print("your gateway to discovering your next promising stock.\n")
    
    # Enter name
    while True:
        user_name = input("Please enter your name: ")

        if user_name.isalpha():
            print(f"Welcome, {user_name}! Let's get you started in finding your next stock.\n")
            break
        else:
            print("Invalid name. Please enter a name containing only letters. Please try again.\n")
    
    # Choose what category you want.
    while True:
        data_str = input("Please enter your preference (Tech, Medical, or Takeover): ")
        if data_str.lower() in ['tech', 'medical', 'takeover']:
            print(f"Thank you for providing your preference: {data_str.capitalize()}\n")

            # Navigate to the proper preferens thats been called
            if data_str.lower() == 'tech':
                explore_tech_options()
            elif data_str.lower() == 'medical':
                explore_medical_options()
            elif data_str.lower() == 'takeover':
                explore_takeover_options()

            break
        else:
            print("Invalid preference. Please enter Tech, Medical, or Takeover. Please try again.\n")



get_stock_preference()

