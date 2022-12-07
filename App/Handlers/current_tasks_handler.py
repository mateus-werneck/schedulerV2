from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Standard.factory_queue import FactoryQueue

class CurrentTasksHandler(AbstractHandlerRequest):
    def get_command(self) -> str:
        return 'tarefas'

    def get_steps(self) -> list:
        return [self.list_tasks, self.show_task_options]

    def list_tasks(self):
       FactoryQueue.create('Task.Listing.Tasks.list_tasks').init()
