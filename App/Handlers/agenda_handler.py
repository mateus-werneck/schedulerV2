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
            self.grade_mode()
        elif self.is_task_mode():
            self.task_mode()
        elif self.is_schedule_mode():
            self.schedule_mode()

    def is_grade_mode(self):
        return self.is_mode('main_agenda_list_grades')

    def grade_mode(self):
        queue = 'Schedule.Listing.Grade.list_grade_options'
        FactoryQueue.create(queue).init()

    def is_task_mode(self):
        return self.is_mode('main_agenda_list_tasks')

    def task_mode(self):
        current_tasks = FactoryHandler.create('current_task_handler')
        current_tasks.execute()

    def is_schedule_mode(self):
        return self.is_mode('main_agenda_list_schedule')

    def schedule_mode(self):
        schedule_handler = FactoryHandler.create('schedule_handler')
        schedule_handler.list_options()
