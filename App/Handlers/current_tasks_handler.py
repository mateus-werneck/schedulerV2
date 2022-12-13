from App.Handlers.Standard.factory_handler import FactoryHandler
from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Standard.factory_queue import FactoryQueue


class CurrentTasksHandler(AbstractHandlerRequest):
    
    def get_command(self) -> str:
        return 'tarefas'

    def get_steps(self) -> list:
        return [self.answer_task_options]

    def get_parent_handler_name(self) -> str:
        return 'agenda_handler'
    
    def answer_task_options(self):
        handler = FactoryHandler.create('schedules_handler')
        handler.start_task_mode()
