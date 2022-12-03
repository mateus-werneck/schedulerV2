from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Grade.Create.create import Create
from App.Queues.Grade.Listing.Grades.list_grades import ListGrades


class TasksHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return ''

    def get_steps(self) -> list:
        return [self.answer_tasks_options]

    def answer_tasks_options(self):
        self.delete_message()
