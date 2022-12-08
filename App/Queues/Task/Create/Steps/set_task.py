
from App.Data.Helpers.task_helper import treat_string_to_task
from App.Queues.Task.Create.create import Create


class SetTask(Create):

    def handle(self) -> bool:
        result = self.set_task_data()
        return super().handle(not result)

    def set_task_data(self):
        if not self.has_valid_text_data():
            self.send_message('Por favor informe uma tarefa válida.')
            return False
        
        task = self.get_task_data()
        
        if not task:
            self.send_message('Por favor informe uma tarefa válida.')
            return False
        
        self.set_task(task)
        return True

    def get_task_data(self):
        task_data = self.get_text_data()
        return treat_string_to_task(task_data)
    
   