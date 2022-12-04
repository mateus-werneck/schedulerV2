from App.Queues.Standard.abstract_handler import AbstractHandler


class Create(AbstractHandler):
    _grade = None
    _task = None
    
    @classmethod
    def set_grade(cls, grade: str):
        cls._grade = grade
     
    @classmethod   
    def get_grade(cls):
        return cls._grade
    
    @classmethod
    def set_task(cls, task: dict):
        cls._task = task
     
    @classmethod   
    def get_task(cls):
        return cls._task
    
    def get_steps(self) -> list:
        return [
            'set_task',
            'check_schedule'
            'save_task'
        ]
    
    def get_namespace(self) -> str:
        return 'Task.Create'
