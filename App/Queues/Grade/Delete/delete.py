from App.Queues.Standard.abstract_handler import AbstractHandler


class Delete(AbstractHandler):
    _grade = None
    
    def get_steps(self) -> list:
        return [
            'delete_grade'
        ]
    
    def get_namespace(self) -> str:
        return 'Grade.Delete'

    @staticmethod
    def set_grade(grade: str):
        Delete._grade = grade
     
    @staticmethod   
    def get_grade():
        return Delete._grade
