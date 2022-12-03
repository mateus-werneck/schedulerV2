from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Schedule.Listing.Grade.list_grade_options import \
    ListGradeOptions
from App.Queues.Schedule.Listing.Schedule.list_schedule_options import \
    ListScheduleOptions


class ScheduleHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return 'agenda'

    def get_steps(self) -> list:
        return [self.list_options, self.answer_list_options]

    def list_options(self):
        ListScheduleOptions().init()

    def answer_list_options(self):
        if self.is_grade_mode():
            ListGradeOptions().init()
        elif self.is_task_mode():
            return

    def is_grade_mode(self):
        return self.is_mode('main_agenda_list_grades')

    def is_task_mode(self):
        return self.is_mode('main_agenda_list_tasks')
