from App.Lib.Bot.chat import BotChat
from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Schedule.Listing.list_schedule_options import \
    ListScheduleOptions


class ScheduleHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return 'agenda'

    def get_steps(self) -> list:
        return [
            self.list_options,
            self.answer_list_options
            ]

    def list_options(self):
        ListScheduleOptions().init()
    
    def answer_list_options(self):
        answer = BotChat.instance().extract_callback_data()
