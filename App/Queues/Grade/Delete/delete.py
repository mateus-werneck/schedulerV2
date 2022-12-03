from App.Queues.Standard.abstract_handler import AbstractHandler


class Delete(AbstractHandler):
    
    def get_steps(self) -> list:
        return [
            'delete_grade'
        ]
    
    def get_namespace(self) -> str:
        return 'Grade.Delete'

    def set_grade(self, grade: str):
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    