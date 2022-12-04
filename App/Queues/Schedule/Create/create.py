from App.Queues.Standard.abstract_handler import AbstractHandler


class Create(AbstractHandler):
    _grade = None
    _deadline = None
    _schedule = None
    
    @classmethod
    def set_grade(cls, grade: str):
        cls._grade = grade
     
    @classmethod   
    def get_grade(cls):
        return cls._grade
    
    @classmethod
    def set_schedule(cls, schedule: dict):
        cls._schedule = schedule
     
    @classmethod   
    def get_schedule(cls):
        return cls._schedule
    
    @classmethod
    def set_deadline(cls, deadline: str):
        cls._deadline = deadline
     
    @classmethod   
    def get_deadline(cls):
        return cls._deadline
    
    def get_steps(self) -> list:
        return [
            'save_schedule'
        ]
    
    def get_namespace(self) -> str:
        return 'Schedule.Create'
