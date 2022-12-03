from App.Queues.Standard.abstract_handler import AbstractHandler


class ListGrades(AbstractHandler):
    
    def get_steps(self) -> list:
        return [
            'list_all'
        ]
    
    def get_namespace(self) -> str:
        return 'Grade.Listing.Grades'
