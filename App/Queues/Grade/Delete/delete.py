from App.Queues.Standard.abstract_handler import AbstractHandler


class Delete(AbstractHandler):
    _grade = None
    
    def get_steps(self) -> list:
        return [
            'delete_grade'
        ]
    
    def get_namespace(self) -> str:
        return 'Grade.Delete'

    @classmethod
    def set_grade(cls, grade: str):
        cls._grade = grade
     
    @classmethod   
    def get_grade(cls):
        return cls._grade
