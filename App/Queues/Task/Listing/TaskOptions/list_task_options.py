from App.Queues.Standard.abstract_handler import AbstractHandler


class ListTaskOptions(AbstractHandler):
    _task = None
    
    @classmethod
    def get_task(cls):
        return cls._task
    
    @classmethod
    def set_task(cls, task: str):
        cls._task = task
        
    def get_steps(self) -> list:
        return [
            'set_task',
            'list_categories'
        ]
    
    def get_namespace(self) -> str:
        return 'Task.Listing.TaskOptions'
