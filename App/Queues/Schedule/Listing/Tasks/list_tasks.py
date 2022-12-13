from App.Handlers.schedules_handler import SchedulesHandler
from App.Queues.Standard.abstract_handler import AbstractHandler


class ListTasks(AbstractHandler):
    _tasks = None
    _handler = None
    
    def __init__(self):
        if self.__class__ is ListTasks:
            ListTasks._tasks = None
            ListTasks._handler = SchedulesHandler.instance()

    def get_steps(self) -> list:
        return [
            'check_tasks',
            'list_all'
        ]

    def get_namespace(self) -> str:
        return 'Schedule.Listing.Tasks'

    @staticmethod
    def set_tasks(tasks: list):
        ListTasks._tasks = tasks

    @staticmethod
    def get_tasks():
        return ListTasks._tasks
    
    @staticmethod
    def set_callback_handler(handler: AbstractHandler):
        ListTasks._handler = handler
        
    @staticmethod
    def get_callback_handler() -> AbstractHandler:
        return ListTasks._handler
