from App.Queues.Standard.abstract_handler import AbstractHandler


class Create(AbstractHandler):
    
    def get_steps(self) -> list:
        return [
            'save_task'
        ]
    
    def get_namespace(self) -> str:
        return 'Task.Create'
