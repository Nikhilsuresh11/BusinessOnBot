# BusinessOnBot

1) Backend Rest service with Flask 
2) Chatbot using Rasa and JS

## 1) Backend

  This is a Flask REST service that fetches bank details from a SQLite database using the data given in the API’s query parameters.

  To run the application, follow these steps:

  Install the required dependencies using pip.

  Run the following command in your terminal:

  pip install -r requirements.txt

  Make sure you have the bank details in CSV format.

  You can use the data available in this repository.
  Convert the CSV file to a SQLite database.

  You can use the following command in your terminal:
  sqlite3 bank_details.db < csv_to_sqlite.sql
  Run the Flask app.



![case1 code](https://user-images.githubusercontent.com/109418285/221884766-edca2ffc-f04e-4d9c-a68e-a88b6119a9a7.png)
![case2 code](https://user-images.githubusercontent.com/109418285/221884837-799efcb5-2654-40cc-8126-117ba3259b65.png)

![case1 OP](https://user-images.githubusercontent.com/109418285/221884907-9a1774a4-64b1-47c9-a257-3a46ed0f3b61.jpeg)
![case2 OP](https://user-images.githubusercontent.com/109418285/221885005-e36222c8-e128-4ac1-be9b-0f35bf44cf7a.jpeg)


## 2) Chatbot


Install Rasa: Use pip to install the Rasa framework on your system by running the command pip install rasa.

Create a Rasa project: Run the command rasa init to create a new Rasa project. 

Define the domain: The domain.yml file defines the domain of your chatbot, including entities, intents, actions, slots, and responses.

Define NLU data: NLU data is used to train the chatbot to understand user inputs. You can define NLU data in the data/nlu.md file.

Define stories: Stories are used to define the conversation flow of the chatbot. You can define stories in the data/stories.md file.

Define actions: Actions are used to perform certain actions based on the user's inputs. You can define actions in the actions.py file.

Train the chatbot: Run the command rasa train to train your chatbot.

Define Flask app: Create a Flask application by defining a Flask app object and defining routes for the chatbot endpoints add some html and css to make it more appealing

Run the Flask app: Start the Flask app by running the command python app.py (assuming that the name of your Flask app file is app.py).



![bot1](https://user-images.githubusercontent.com/109418285/221884447-32c38f3e-bd4e-4291-a2a6-cb592f162242.png)
![bot2](https://user-images.githubusercontent.com/109418285/221884678-90498961-4e6e-4b3a-b336-b68fe184d19b.png)


