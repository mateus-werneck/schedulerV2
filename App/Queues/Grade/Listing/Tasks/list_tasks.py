from App.Queues.Standard.abstract_handler import AbstractHandler


class ListTasks(AbstractHandler):
    _grade = None
    
    def get_steps(self) -> list:
        return [
            'list_all'
        ]
    
    def get_namespace(self) -> str:
        return 'Grade.Listing.Tasks'

    @staticmethod
    def set_grade(grade: str):
        ListTasks._grade = grade
     
    @staticmethod   
    def get_grade():
        return ListTasks._grade
