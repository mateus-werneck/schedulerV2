from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest


class TaskHandler(AbstractHandlerRequest):
    _task = None
    
    @classmethod
    def get_task(cls):
        return cls._task
    
    @classmethod
    def set_task(cls, task: str):
        cls._task = task
        
    def get_command(self) -> str:
        return ''

    def get_steps(self) -> list:
        return [self.answer_task_options]

    def answer_task_options(self):
        pass