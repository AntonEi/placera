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


def validate_stock_preference(valid_choices):
    option_is_valid = False
    while option_is_valid is False:
        option = input("Enter your option: ")
        option_is_valid = option in valid_choices
        if option_is_valid is False:
            print('Please enter a valid option')
    return int(option)

def explore_tech_options():
    """
    Explore additional options in the Tech category.
    Display a menu for Tech option, asking the user to choose an option
    """
    keyword_list = ["Partnerships", "Market Expansion", "Product Launch", "Stock Buyback Program",
                    "Supply Chain  Updates", "Industry Awards"]
    print("Choose a keyword to explore Tech options:")
    print("[1] Partnerships")
    print("[2] Market Expansion")
    print("[3] Product Launch")
    print("[4] Stock Buyback Program")
    print("[5] Supply Chain  Updates")
    print("[6] Industry Awards\n")
    print("[10] Back to Category")
    print("[0] Exit program")

    ## Option field
    option = validate_stock_preference(['1', '2', '3', '4', '5', '6',
                                        '10', '0'])
    while option != 0:
        if option < 10:
            keyword_index = option - 1
            selected_keyword = keyword_list[keyword_index]
            print(f'\nkey word: "{selected_keyword}"')
            find_stories_by_keyword(selected_keyword, datatech)
        else:
            print('Back to Category...\n')
            get_stock_preference()
            break
        option = int(input("Enter another option: "))

def explore_medical_options():
    """
    Explore additional options in the Medical category.
    Display a menu for Tech option, asking the user to choose an option
    """
    keyword_list = ["FDA approval", "Fas 1", "Fas 2", "Fas 3",
                "EMA approval", "Product Launches"]
    print("Choose a keyword to explore Medical options:")
    print("[1] FDA approval")
    print("[2] Fas 1")
    print("[3] Fas 2")
    print("[4] Fas 3")
    print("[5] EMA approval")
    print("[6] Product Launches\n")
    print("[10] Back to Category")
    print("[0] Exit program")

    ## Option field
    option = validate_stock_preference(['1', '2', '3', '4', '5', '6',
                                        '10', '0'])
    while option != 0:
        if option < 10:
            keyword_index = option - 1
            selected_keyword = keyword_list[keyword_index]
            print(f'\nkey word: "{selected_keyword}"')
            find_stories_by_keyword(selected_keyword, datamedical)
        else:
            print('Back to Category...\n')
            get_stock_preference()
            break
        option = int(input("Enter another option: "))

def explore_takeover_options():
    """
    Explore additional options in the Takeover category.
    Display a menu for Tech option, asking the user to choose an option
    """
    keyword_list = ["Merger", "Takeover", "Acquisition", "Letter of Intent",
            "Buyout", "Hostile Takeover"]
    print("Choose a keyword to explore Takeover options:")
    print("[1] Merger")
    print("[2] Takeover")
    print("[3] Acquisition")
    print("[4] Letter of Intent")
    print("[5] Buyout")
    print("[6] Hostile Takeover\n")
    print("[10] Back to Category")
    print("[0] Exit program")

    ## Option field
   option = validate_stock_preference(['1', '2', '3', '4', '5', '6',
                                        '10', '0'])
    while option != 0:
        if option < 10:
            keyword_index = option - 1
            selected_keyword = keyword_list[keyword_index]
            print(f'\nkey word: "{selected_keyword}"')
            find_stories_by_keyword(selected_keyword, datamedical)
        else:
            print('Back to Category...\n')
            get_stock_preference()
            break
        option = int(input("Enter another option: "))

def enter_name():
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
    
def get_stock_preference():
    """
    Welcome message and user instructions.
    Get information to assist in finding your next stock.
    """
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

def find_stories_by_keyword(keyword, data_sheet):
    found_list = []
    for story in data_sheet:
        if keyword.lower() in story[1] or keyword.upper() in story[1] or keyword in story[1]:
            found_list.append(story)
    print(f'We found {len(found_list)} stories matching your keyword: ')
    for story in found_list:
        print(story)


tech = SHEET.worksheet('tech')
datatech = tech.get_all_values()
medical = SHEET.worksheet('medical')
datamedical = medical.get_all_values()
takeover = SHEET.worksheet('takeover')
datatakeover = takeover.get_all_values()


def main():
    enter_name()
    get_stock_preference()
    
main()