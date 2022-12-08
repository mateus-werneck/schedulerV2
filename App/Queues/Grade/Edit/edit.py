from App.Queues.Standard.abstract_handler import AbstractHandler


class Edit(AbstractHandler):
    _grade = None
    
    def get_steps(self) -> list:
        return [
            'edit_grade'
        ]
    
    def get_namespace(self) -> str:
        return 'Grade.Edit'

    @staticmethod
    def set_grade(grade: str):
        Edit._grade = grade
     
    @staticmethod   
    def get_grade():
        return Edit._grade
