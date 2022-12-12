from App.Handlers.Standard.factory_handler import FactoryHandler
from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Standard.factory_queue import FactoryQueue


class CurrentTasksHandler(AbstractHandlerRequest):
    def get_command(self) -> str:
        return 'tarefas'

    def get_steps(self) -> list:
        return [self.list_tasks]

    def list_tasks(self):
       FactoryQueue.create('Schedule.Listing.All.list_all_tasks').init()
       self.reset_handler('schedules_handler')
       schedules_handler = FactoryHandler.create('schedules_handler')
       schedules_handler.next()
       schedules_handler.next()
       
