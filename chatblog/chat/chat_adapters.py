from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement

class Login_User(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        if not isinstance(statement, Statement):
            statement = Statement(text=statement)

        keywords = ['i want', 'goodbye', 'hello', 'good']  # Palavras-chave fornecidas

        return any(keyword in statement.text.lower() for keyword in keywords)

    def process(self, statement, additional_response_selection_parameters=None):
        responses = {
            'i want': "To get started, please log in or create an account.",
            'goodbye': "Goodbye! Come back soon.",
            'hello': "Hello! How can I assist you today?",
            'good': "I'm glad you're feeling good!"
        }

        for keyword, response in responses.items():
            if keyword in statement.text.lower():
                return Statement(response)

        return None