
from App.Data.Helpers.message_helper import down_face, floppy_disk
from App.Lib.Client.marina_api import MarinaAPI
from App.Queues.Task.Create.create import Create
from App.Data.Helpers.task_helper import treat_string_to_task


class SaveTask(Create):

    def handle(self) -> bool:
        self.save()
        return super().handle()

    def save(self):
        if not self.has_valid_text_data():
            self.send_message('Por favor informe uma tarefa válida.')
            return
        
        task = self.get_task_data()
        self.set_task(task)

    def get_task_data(self):
        task_data = self.get_text_data()
        return treat_string_to_task(task_data)
    
   