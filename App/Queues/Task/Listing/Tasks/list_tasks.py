from App.Queues.Standard.abstract_handler import AbstractHandler


class ListTasks(AbstractHandler):
    _task = None
    
    def __init__(self):
        if self.__class__ is ListTasks:
            ListTasks._task = None
    
    def get_steps(self):
        return [
            'list_all'
        ]
        
    def get_namespace(self) -> str:
        return 'Task.Listing.Tasks'
    
    