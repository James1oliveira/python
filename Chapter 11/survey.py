class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """
        Initialize the survey with a question.
        Also prepare an empty list to store user responses.
        
        Args:
        question -- a string containing the survey question
        """
        self.question = question  # Store the survey question
        self.responses = []       # Create an empty list for storing responses

    def show_question(self):
        """Display the survey question to the user."""
        print(self.question)

    def store_response(self, new_response):
        """
        Add a single response to the list of responses.
        
        Args:
        new_response -- a string containing the user's answer
        """
        self.responses.append(new_response)

    def show_results(self):
        """Display all the responses that have been collected so far."""
        print("Survey results:")
        for response in self.responses:  # Loop through each stored response
            print(f"- {response}")
