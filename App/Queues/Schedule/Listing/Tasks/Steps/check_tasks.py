from App.Data.Helpers.message_helper import down_face
from App.Queues.Schedule.Listing.Tasks.list_tasks import ListTasks


class CheckTasks(ListTasks):

    def handle(self):
        force_stop = self.force_stop()
        return super().handle(force_stop)
    
    def force_stop(self):
        if not self.get_tasks():
            self.send_message(f'{down_face()} Nenhuma tarefa foi encontrada.')
            return True
        return False
