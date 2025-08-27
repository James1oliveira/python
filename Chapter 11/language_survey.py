from survey import AnonymousSurvey  # Import the AnonymousSurvey class from the survey module

# Define the survey question
question = "What language did you first learn to speak?"

# Create an instance of AnonymousSurvey using the question
language_survey = AnonymousSurvey(question)

# Display the question to the user
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")  # Instructions for quitting the survey

# Loop to collect responses from users
while True:
    response = input("Language: ")  # Ask the user for a language
    if response == 'q':  # If user enters 'q', exit the loop
        break
    language_survey.store_response(response)  # Store the user's response

# Display the survey results
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()  # Show all stored responses
