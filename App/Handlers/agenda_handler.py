from App.Handlers.Standard.factory_handler import FactoryHandler
from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Standard.factory_queue import FactoryQueue


class AgendaHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return 'agenda'

    def get_steps(self) -> list:
        return [self.list_options, self.answer_list_options]

    def list_options(self):
        queue = 'Schedule.Listing.Schedule.list_schedule_options'
        FactoryQueue.create(queue).init()

    def answer_list_options(self):
        self.delete_message()

        if self.is_grade_mode():
            queue = 'Schedule.Listing.Grade.list_grade_options'
            FactoryQueue.create(queue).init()
        elif self.is_task_mode():
            current_tasks = FactoryHandler.create('current_tasks_handler')
            current_tasks.execute()
        elif self.is_schedule_mode():
            schedules_handler = FactoryHandler.create('schedules_handler')
            schedules_handler.execute()

    def is_grade_mode(self):
        return self.is_mode('main_agenda_list_grades')

    def is_task_mode(self):
        return self.is_mode('main_agenda_list_tasks')

    def is_schedule_mode(self):
        return self.is_mode('main_agenda_list_schedule')
