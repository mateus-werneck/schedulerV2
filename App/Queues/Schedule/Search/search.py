from App.Queues.Standard.abstract_handler import AbstractHandler


class Search(AbstractHandler):
    _grade = None
    _deadline = None
    _schedule = None
    
    def get_steps(self) -> list:
        return [
            'set_grade',
            'check_schedule_exists',
            'create_schedule'
        ]
    
    def get_namespace(self) -> str:
        return 'Schedule.Search'
    
    @staticmethod
    def set_grade(grade):
        Search._grade = grade
     
    @staticmethod
    def get_grade():
        return Search._grade
    
    @staticmethod
    def set_schedule(schedule: dict):
        Search._schedule = schedule
    
    @staticmethod
    def get_schedule():
        return Search._schedule
    
    @staticmethod
    def set_deadline(deadline: str):
        Search._deadline = deadline
    
    @staticmethod
    def get_deadline():
        return Search._deadline
    
    @staticmethod
    def has_active_schedule():
        return Search.get_schedule() is not None
