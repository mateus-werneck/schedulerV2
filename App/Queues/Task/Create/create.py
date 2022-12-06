from App.Queues.Standard.abstract_handler import AbstractHandler
from App.Lib.Log.logger import Logger

class Create(AbstractHandler):
    _grade = None
    _task = None
    
    @staticmethod
    def set_grade(grade: str):
        Create._grade = grade
     
    def get_grade(self):
        return self._grade
    
    @staticmethod
    def set_task(task: dict):
        Create._task = task
     
    def get_task(self):
        return self._task
    
    def get_steps(self) -> list:
        return [
            'set_task',
            'check_schedule',
            'save_task'
        ]
    
    def get_namespace(self) -> str:
        return 'Task.Create'
