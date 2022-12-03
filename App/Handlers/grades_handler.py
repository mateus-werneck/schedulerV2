from App.Data.Helpers.message_helper import down_face, floppy_disk
from App.Lib.Client.marina_api import MarinaAPI
from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Grade.Create.create import Create
from App.Queues.Grade.Listing.Grades.list_grades import ListGrades


class GradesHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return ''

    def get_steps(self) -> list:
        return [self.answer_grade_options, self.answer_create_grade]

    def answer_grade_options(self):
        if self.is_create_grade_mode():
            return self.reply_create_grade()
        if self.is_show_grades_mode():
            ListGrades().init()
            return False

    def is_create_grade_mode(self):
        return self.is_mode('agenda_grades_create_grade')

    def reply_create_grade(self):
        message = 'Informe um nome para a nova turma. \
                \nExemplo: <b>Junior 1 - T/Q - 19:30</b>'
        self.send_message(message)
    
    def is_show_grades_mode(self):
        return self.is_mode('agenda_grades_show_grades')

    def answer_create_grade(self):        
        Create().init()
