from App.Lib.Bot.chat import BotChat
from App.Lib.Log.logger import Logger
from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest


class GradeHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return ''

    def get_steps(self) -> list:
        return [
            self.answer_grade_options
        ]

    def answer_grade_options(self):
        answer = BotChat.instance().extract_callback_data()
        Logger.instance().info(f'Callback: {answer}')
