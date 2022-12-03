from App.Lib.Bot.context import BotContext
from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Grade.Delete.delete import Delete
from App.Queues.Grade.Listing.GradeOptions.list_grades_options import \
    ListGradesOptions


class GradeHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return ''

    def get_steps(self) -> list:
        return [self.list_options, self.answer_callback]

    def list_options(self):
        data = self.get_callback_data()
        self.grade = data.replace('grade_', '')
        ListGradesOptions().init()

    def answer_callback(self):
        if self.is_edit_mode:
            return
        elif self.is_delete_mode():
            self.delete_grade()
        elif self.is_list_tasks_mode():
            return
    
    def is_edit_mode(self):
        return self.is_mode('main_grade_edit_grade')
    
    def is_delete_mode(self):
        return self.is_mode('main_grade_delete_grade')
    
    def is_list_tasks_mode(self):
        return self.is_mode('main_grade_list_tasks')

    def delete_grade(self):
        queue = Delete()
        queue.set_grade(self.grade)
        queue.init()
        self.grade = None
