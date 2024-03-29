
from App.Data.Helpers.message_helper import cross_mark_icon, down_face
from App.Data.Helpers.task_helper import treat_string_to_task
from App.Lib.Client.marina_api import MarinaAPI
from App.Queues.Task.Delete.delete import Delete


class DeleteTask(Delete):

    def handle(self) -> bool:
        self.delete()
        return super().handle()

    def delete(self):    
        deleted = self.delete_task()
        self.notify(deleted)

    def delete_task(self):
        task = self.get_task()
        return MarinaAPI.instance().delete_task(task)
    
    def notify(self, deleted: dict):
        if deleted.get('id'):
            message = f'{cross_mark_icon()} Tarefa removida com sucesso.'
        else:
            message = f'{down_face()} Não consegui remover a tarefa para você.'
        
        self.send_message(message)
