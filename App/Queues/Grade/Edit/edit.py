from App.Queues.Standard.abstract_handler import AbstractHandler


class Edit(AbstractHandler):
    _grade = None
    
    def get_steps(self) -> list:
        return [
            'edit_grade'
        ]
    
    def get_namespace(self) -> str:
        return 'Grade.Edit'

    @classmethod
    def set_grade(cls, grade: str):
        cls._grade = grade
     
    @classmethod   
    def get_grade(cls):
        return cls._grade
