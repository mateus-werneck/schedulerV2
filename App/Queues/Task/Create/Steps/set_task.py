
from App.Queues.Task.Create.create import Create
from App.Data.Helpers.task_helper import treat_string_to_task


class SetTask(Create):

    def handle(self) -> bool:
        result = self.save()
        return super().handle(not result)

    def save(self):
        if not self.has_valid_text_data():
            self.send_message('Por favor informe uma tarefa válida.')
            return False
        
        task = self.get_task_data()
        self.set_task(task)
        return True

    def get_task_data(self):
        task_data = self.get_text_data()
        return treat_string_to_task(task_data)
    
   