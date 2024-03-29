from App.Data.Helpers.message_helper import get_startup_message
from App.Lib.Bot.chat import BotChat
from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest


class StartHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return 'start'

    def get_steps(self) -> list:
        return [self.start]

    def start(self):
        message = 'Bem-vindo a sua agenda.'
        BotChat.instance().send_text(message)
        BotChat.instance().send_text(get_startup_message())
