from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Standard.factory_queue import FactoryQueue


class GradeHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return ''

    def get_steps(self) -> list:
        return [self.list_options, self.answer_callback, self.edit_grade]

    def list_options(self):
        data = self.get_callback_data()
        self.grade = data.replace('grade_', '')
        queue = 'Grade.Listing.GradeOptions.list_grades_options'
        FactoryQueue.create(queue).init()

    def answer_callback(self):
        self.delete_message()
        
        if self.is_edit_mode():
            self.ask_new_grade_name()
        elif self.is_delete_mode():
            return self.delete_grade()
        elif self.is_list_tasks_mode():
            return self.list_tasks()
    
    def is_edit_mode(self):
        return self.is_mode('main_grade_edit_grade')
    
    def ask_new_grade_name(self):
        self.send_message('Por favor informe um nome novo para a turma. \
                \nExemplo: <b>Advanced - S/Q - 17:00</b>')
        
    def is_delete_mode(self):
        return self.is_mode('main_grade_delete_grade')
    
    def delete_grade(self):
        queue = FactoryQueue.create('Grade.Delete.delete')
        queue.set_grade(self.grade)
        queue.init()
        self.grade = None
        return False
    
    def is_list_tasks_mode(self):
        return self.is_mode('main_grade_list_tasks')
    
    def list_tasks(self):
        queue = FactoryQueue.create('Grade.Listing.Tasks.list_tasks')
        queue.set_grade(self.grade)
        queue.init()
        self.grade = None
        return False

    def edit_grade(self):
        queue = FactoryQueue.create('Grade.Edit.edit')
        queue.set_grade(self.grade)
        queue.init()
        self.grade = None
