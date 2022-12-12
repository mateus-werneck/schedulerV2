from App.Lib.Log.logger import Logger
from App.Queues.Standard.abstract_handler import AbstractHandler


class Create(AbstractHandler):
    _grade = None
    _task = None
    
    def __init__(self):
        if self.__class__ is Create:
            Create._grade = None
            Create._task = None
        
    def get_steps(self) -> list:
        return [
            'set_task',
            'set_schedule',
            'save_task',
            'alert_task'
        ]
    
    def get_namespace(self) -> str:
        return 'Task.Create'
    
    @staticmethod
    def set_grade(grade: str):
        Create._grade = grade
    
    @staticmethod 
    def get_grade():
        return Create._grade
    
    @staticmethod
    def set_task(task: dict):
        Create._task = task
     
    @staticmethod
    def get_task():
        return Create._task
