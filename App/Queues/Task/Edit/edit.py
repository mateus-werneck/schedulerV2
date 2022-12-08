from App.Lib.Log.logger import Logger
from App.Queues.Standard.abstract_handler import AbstractHandler


class Edit(AbstractHandler):
    _task_id = None
    _task = None
    
    def get_steps(self) -> list:
        return [
            'set_task',
            'check_schedule',
            'edit_task'
        ]
    
    def get_namespace(self) -> str:
        return 'Task.Edit'
    
    @staticmethod
    def set_task(task: dict):
        Edit._task = task
     
    @staticmethod
    def get_task():
        return Edit._task
    
    @staticmethod
    def set_task_id(id: str):
        Edit._task_id = id
     
    @staticmethod
    def get_task_id():
        return Edit._task_id
