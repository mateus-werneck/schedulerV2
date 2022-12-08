from App.Lib.Log.logger import Logger
from App.Queues.Standard.abstract_handler import AbstractHandler


class Delete(AbstractHandler):
    _task = None
    
    def __init__(self):
        if self.__class__ is Delete:
            Delete._task = None
    
    def get_steps(self) -> list:
        return [
            'delete_task'
        ]
    
    def get_namespace(self) -> str:
        return 'Task.Delete'

    @staticmethod
    def set_task(task: str):
        Delete._task = task
     
    @staticmethod
    def get_task():
        return Delete._task
