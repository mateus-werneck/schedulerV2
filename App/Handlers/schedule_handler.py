from App.Lib.Bot.chat import BotChat
from App.Lib.Bot.context import BotContext
from App.Lib.Log.logger import Logger
from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Grade.Listing.list_grade_options import ListGradeOptions
from App.Queues.Schedule.Listing.list_schedule_options import \
    ListScheduleOptions


class ScheduleHandler(AbstractHandlerRequest):
    
    def get_command(self) -> str:
        return 'agenda'

    def get_steps(self) -> list:
        return [self.list_options, self.answer_list_options]

    def list_options(self):
        ListScheduleOptions().init()

    def answer_list_options(self):
        answer = BotChat.instance().extract_callback_data()
        Logger.instance().info(f'Callback: {answer}')
        self.__handle_modes(answer)

    def __handle_modes(self, answer: str):
        if self.is_grade_mode(answer):
            ListGradeOptions().init()
        elif self.is_task_mode(answer):
            return

    def is_grade_mode(self, answer: str):
        return answer == 'main_agenda_list_grades'
    
    def is_task_mode(self, answer: str):
        return answer == 'main_agenda_list_tasks'
