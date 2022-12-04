
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
        
        new_task = self.create_task()
        self.notify(new_task)

    def create_task(self):
        task = self.get_task()
        return MarinaAPI.instance().create_task(task)

    def get_task(self):
        task_data = self.get_text_data()
        return treat_string_to_task(task_data)
    
    def notify(self, grade: dict):
        if grade.get('id'):
            message = f'{floppy_disk()} Tarefa criada com sucesso.'
        else:
            message = f'{down_face()} Não consegui criar a tarefa para você.'
        
        self.send_message(message)
