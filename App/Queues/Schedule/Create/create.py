from App.Queues.Standard.abstract_handler import AbstractHandler


class Create(AbstractHandler):
    _grade = None
    _deadline = None
    _schedule = None
    
    def get_steps(self) -> list:
        return [
            'save_schedule'
        ]
    
    def get_namespace(self) -> str:
        return 'Schedule.Create'
    
    @staticmethod
    def set_grade(grade: str):
        Create._grade = grade
     
    @staticmethod
    def get_grade():
        return Create._grade
    
    @staticmethod
    def set_schedule(schedule: dict):
        Create._schedule = schedule
    
    @staticmethod
    def get_schedule():
        return Create._schedule
    
    @staticmethod
    def set_deadline(deadline: str):
        Create._deadline = deadline
    
    @staticmethod
    def get_deadline():
        return Create._deadline
