
from App.Data.Helpers.message_helper import down_face, floppy_disk
from App.Data.Helpers.task_helper import treat_string_to_task
from App.Lib.Client.marina_api import MarinaAPI
from App.Queues.Task.Create.create import Create


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
    
    def notify(self, new_task: dict):
        task = self.get_task()
       
        if new_task.get('id'):
            message = f'{floppy_disk()} Tarefa <b>{task.get("name")}</b>'\
                + ' criada com sucesso.'
        else:
            message = f'{down_face()} Não consegui criar a tarefa'\
            + f' <b>{task.get("name")}</b> para você.'
        
        self.send_message(message)
