# StockTrigger

Welcome to StockTrigger, the Python-powered tool designed to make stock exploration an accessible and enjoyable experience. Whether you're a seasoned investor or just starting, StockTrigger provides a user-friendly platform to discover promising stocks through relevant news in Tech, Medical, and Takeover sectors.

The live link can be found here - [StockTrigger](https://stocktrigger-aad21b3ce292.herokuapp.com/)

## How to use StockTrigger:

- Start by entering your name
- Choose from three different preferences: Tech, Medical, or Takeover
    - This selection will guide StockTrigger to focus on relevant press releases within the chosen preference.
- Select a keyword of your choice that you want to use to find stocks within the specified preference.
    - This keyword will be used to search for related stories within press releases.
- StockTrigger will efficiently scan its curated collection for press releases containing the specified keyword within the chosen preference.
    - The tool will display the number of stories found based on your search criteria
- Receive a summary of the found heading.
    - Explore the context of each story to make informed decisions.
- Choose whether to save the used keyword in the document for future reference.
    - This option helps in keeping track of previously used keywords and the associated search results.
- After reviewing the search results, StockTrigger presents options for the next action:
    - Use a new keyword for a different search.
    - Choose another preference and initiate a new search 
    - End the program if your search requirements are met. 

## Site Owner Goals

- To provide users with an efficient and user-friendly tool for searching key information within press releases.
- The tool is designed to assist users in staying one step ahead when identifying the next big stock.
- The tool is aimed at aiding users in effortlessly identifying stocks.

## User Stories

- ### As a user I want to:
    - Select a preference (Tech, Medical, or Takeover) to tailor my stock search.
    - Easily navigate through a menu of keywords associated with my preference.
    - Receive information on the number of news stories found related to my chosen keyword.
    - Read the stories in a clear and straightforward text format.
    - Decide whether to save the keyword and associated stories in a document for future reference.
    - Have the option to use a new keyword, select another preference, or end the program.

## Logic Flow 

To help plan and understand how the tool works, I created a flow chart using Lucid Chart. 

This chart visually shows the step-by-step process and the different parts of the tool that interact with each other. It was created at the beginning of the project to guide the development.it does not fully reflect the tool structure.

The goal was to keep things organized and ensure a clear understanding of the tool's structure. Although the flow chart may not cover every detail, it served as a helpful roadmap.

![Flow Chart](docs/readme_images/logic-flow.png)

## Features

### Title and Introduction Section
- Upon entering the tool, the user is greeted with a simple interface that welcomes them and requests their name.

![Welcome Screen](docs/readme_images/first-page.png)

- Robust data validation is implemented for the name input. The user is required to enter a name consisting only letters, and not just a blank space.In case of invalid data, a error message saying "Invalid name. Please enter a name containing only letters. Please try again." will show

![Username Validation](docs/readme_images/invalid-name.png)

### Preference menu
- The computer will welcome them to the game and repeat their name back to them. 
- Next, you'll be asked to choose a preference between Tech, Medical, or Takeover. Select the category that aligns with your interest or focus.

![User Menu](docs/readme_images/preference.png)

- It doesn't matter if their input is lower or upper case. The computer can handle both inputs by using the inbuilt function, lower().
- If the user does not input Tech, Medical, or Takeover they will get an error message saying "Invalid preference. Please enter Tech, Medical, or Takeover. Please try again." 

![User validator](docs/readme_images/invalid-preference.png)

### Key word option
- The program will present you with a menu of keywords related to your chosen preference.
- You can select a keyword from the list to explore relevant information.

![Key word option](docs/readme_images/keyword-section.png)

If you don't input a valid number, you will receive an error message asking you to input a valid option. 

![Key word option](docs/readme_images/invalid-keyword.png)

### Keyword Result
- After selecting the keyword, the program will display relevant PR matching your preference.
- You can decide whether to save this keyword for regular searches or not. Inputting either "1" for Yes or "2" for No will prompt the next step in the process.

![Keyword Result](docs/readme_images/save.png)

If you don't input a valid number, you will receive an error message asking you to input a valid option. 

![Saving invaid](docs/readme_images/save-invalid.png)
### Saving keyword
- If the user chooses to save the keyword for regular searches, they can enter [1] for "Yes." The program then updates the document and confirms the action by displaying "Document updated."
- Following this, the user is prompted to enter another option, and they are reminded that they can press [10] to see the options. This allows users to continue using the program for additional searches or explore other features.

![Saving keyword](docs/readme_images/save.png)

### Exit program 
- The user has the option to exit the program at any time by pressing [0]. This provides a convenient and straightforward way for users to conclude their session when they no longer wish to use the tool.

![Exit program](docs/readme_images/exit.png)


## Data Model

I utilized a modular design and a combination of functions and data structures in this project. The StockTrigger program comprises several functions, each serving a specific purpose:
- validate_stock_preference: This function ensures the user's selected option is valid, taking input and validating it against a list of choices.
- explore_tech_options, explore_medical_options, explore_takeover_options: These functions present additional options within different categories, allowing users to explore various keywords related to Tech, Medical, and Takeover.
- find_stories_by_keyword: Searches for stories in a data sheet that match a given keyword, providing the user with relevant information.
- The data model involves the use of lists to store keywords, data retrieved from Google Sheets, and Google Sheets integration using the gspread library.

![Google sheet](docs/readme_images/sheet.png) 
## Testing 

### PEP8 Testing
The python files have all been passed through [pep8](https://pep8ci.herokuapp.com/#) All python files were checked with no errors reported. See screen show below: 

![pep8](docs/readme_images/Pep8.png)

### Input Testing

The name input underwent thorough testing to ensure a robust validation process. Specifically:

- Verified that the user cannot input an empty space and only letters as their name.
- Preference menu accepts only three valid preferences: Tech, Medical, or Takeover.
- If an invalid number or letters is input during the Keyword Option or Saving keyword option, the system will generate a clear error message.


### Other Program Testing
The program was tested thoroughly to ensure the following features worked as intended:
- A user selects their preference between Tech, Medical, or Takeover each time they use the app.
- The program guides the user through available options within their selected preference.
- The app validates and handles user input to ensure it matches available choices, providing clear error messages otherwise.
- The user can explore various keyword options within their chosen preference.
- The app retrieves and displays relevant stories from a Google Sheet based on the selected keyword.
- The user has the option to save a keyword to regular searches for future reference.
- The program ensures that the entered name is valid, consisting only of letters.
- The app gives appropriate feedback to the user based on their interactions, ensuring clear communication.
- The terminal provides a smooth and clear experience, with options to exit the program or explore more preferences. 
- The app integrates with Google Sheets to update information accurately and reflect the user's preferences.

All of the above tests were completed in my local terminal and also in the Heroku terminal.

## Libraries and Technologies Used

### Python Libraries:
[Gspread](https://pypi.org/project/gspread/): to allow communication with Google Sheets
[google.oauth2.service_account](https://google-auth.readthedocs.io/en/stable/index.html):  used to get infomation for the text

### Programs Used
- [GitHub](https://github.com/) - used for version control.
- [Heroku](https://dashboard.heroku.com/apps) -  used to deploy the live project.
- [Lucidchart](https://lucid.app/documents#/dashboard) -  used to create the game flowchart
- [PEP8 Online](http://pep8online.com/) - used to validate all the Python code

## Known Bugs

The text from the Google Sheet doesn't fit within the program's square. 

Attempting to copy the text causes the program to shut down.

## Fixed bugs 

Add validator to the takeover option function

- Issue: Pressing keys 7-9 at the start of the program led to an unexpected shutdown.
- Description: Users experienced an issue where pressing any key from 7 to 9 during the program's startup caused an abrupt shutdown.
- Resolution: The problem was traced to the absence of input validation in the takeover option function. This resulted in the program encountering unexpected input, leading to a shutdown. The addition of a validator to the takeover option function now ensures that only valid inputs are accepted, preventing the program from shutting down unexpectedly when keys 7-9 are pressed.


Resolve Loop Exit Issue

- Issue: Delayed Exit on Pressing [0] in Program Loop
- Description: Users reported an inconvenience during program execution where pressing [0] to exit required multiple attempts. The program was caught in a loop, necessitating users to press [0] more than once to successfully exit.
- Resolution: Upon further inspection, it was identified that the loop exit condition needed improvement. To address this issue, a 'break' statement was strategically introduced, ensuring a more efficient exit process. With this modification, users can now exit the program promptly with a single press of [0], enhancing the overall usability and responsiveness of the application. The 'break' statement optimizes the loop control, resolving the reported problem and providing a smoother user experience

## Deployment

The site was deployed via [Heroku](https://dashboard.heroku.com/apps), and the live link can be found here: [Stocktrigger](https://stocktrigger-aad21b3ce292.herokuapp.com/)

Before deploying to Heroku pip3 freeze > requirements.txt was used to add all the dependencies required to the requirements.txt file. This is required for the game to run on Heroku.

The following steps were then taken:
1. Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
3. Enter a unique and meaningful app name.
4. Next select your region.
5. Click on the Create App button.
6. Click on the Settings Tab and scroll down to Config Vars.
7. Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button.
8. Input CREDS and the content of your Google Sheet API creds file as another config var and click add.
9. In the next Key box enter OXFORD_API_APP_ID and add your unique ID to the value box. 
10. In the next Key box enter OXFORD_API_APP_KEY and add your unique key to the value box. 
11. Next, scroll down to the Buildpack section click Add Buildpack select Python and click Save Changes
12. Repeat step 11 to add node.js. Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order.
13. Scroll to the top of the page and choose the Deploy tab.
14. Select Github as the deployment method.
15. Confirm you want to connect to GitHub.
16. Search for the repository name and click the connect button.
17. Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
18. Click View to view the deployed site.

The site is now live and operational.

## Credits 
### Resources Used
- [W3Schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [Placera](https://www.placera.se/placera/pressmeddelanden.html)


## Acknowledgments

A big thank you to my mentor Antonio Rodriguez

My fellow student Elin Dalenbäck.