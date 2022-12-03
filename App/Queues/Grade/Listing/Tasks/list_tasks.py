from App.Queues.Standard.abstract_handler import AbstractHandler


class ListTasks(AbstractHandler):
    _grade = None
    
    def get_steps(self) -> list:
        return [
            'list_all'
        ]
    
    def get_namespace(self) -> str:
        return 'Grade.Listing.Tasks'

    @classmethod
    def set_grade(cls, grade: str):
        cls._grade = grade
     
    @classmethod   
    def get_grade(cls):
        return cls._grade