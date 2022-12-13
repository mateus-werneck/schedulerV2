from App.Handlers.Standard.factory_handler import FactoryHandler
from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Standard.factory_queue import FactoryQueue


class CurrentTaskHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return 'tarefas'

    def get_steps(self) -> list:
        return [self.list_tasks]

    def list_tasks(self):
        FactoryQueue.create('Schedule.Listing.All.list_all_tasks')\
            .init()
