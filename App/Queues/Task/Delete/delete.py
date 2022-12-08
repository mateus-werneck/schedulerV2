from App.Lib.Log.logger import Logger
from App.Queues.Standard.abstract_handler import AbstractHandler


class Delete(AbstractHandler):
    _task = None
    
    def get_steps(self) -> list:
        return [
            'delete_task'
        ]
    
    def get_namespace(self) -> str:
        return 'Task.Delete'

    @staticmethod
    def set_task(task: dict):
        Create._task = task
     
    @staticmethod
    def get_task():
        return Create._task