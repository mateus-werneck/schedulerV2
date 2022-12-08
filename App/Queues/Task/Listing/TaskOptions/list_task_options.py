from App.Queues.Standard.abstract_handler import AbstractHandler


class ListTaskOptions(AbstractHandler):
    _task = None
    
    def __init__(self):
        if self.__class__ is ListTaskOptions:
            ListTaskOptions._task = None
    
    @staticmethod
    def get_task():
        return ListTaskOptions._task
    
    @staticmethod
    def set_task(task: str):
        ListTaskOptions._task = task
        
    def get_steps(self) -> list:
        return [
            'set_task',
            'list_categories'
        ]
    
    def get_namespace(self) -> str:
        return 'Task.Listing.TaskOptions'
