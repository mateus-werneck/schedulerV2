
from App.Data.Helpers.message_helper import down_face, floppy_disk
from App.Data.Helpers.task_helper import treat_string_to_task
from App.Lib.Client.marina_api import MarinaAPI
from App.Queues.Task.Edit.edit import Edit


class EditTask(Edit):

    def handle(self) -> bool:
        self.save()
        return super().handle()

    def save(self):
        updated = self.edit_task()
        self.notify(updated)

    def edit_task(self):
        task = self.get_task()
        return MarinaAPI.instance().edit_task(self.get_task_id(), task)

    def notify(self, updated: dict):
        task = self.get_task()
        
        if updated.get('id'):
            message = f'{floppy_disk()} Tarefa <b>{task.get("name")}</b>'\
                + ' alterada com sucesso.'
        else:
            message = f'{down_face()} Não consegui alterar a tarefa'\
                + f' <b>{task.get("name")}</b> para você.'

        self.send_message(message)
