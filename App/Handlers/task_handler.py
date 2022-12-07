from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Standard.factory_queue import FactoryQueue


class TaskHandler(AbstractHandlerRequest):
    _task = None

    @staticmethod
    def get_task():
        return TaskHandler._task

    @staticmethod
    def set_task(task: str):
        TaskHandler._task = task

    def get_command(self) -> str:
        return ''

    def get_steps(self) -> list:
        return [self.list_task_options]

    def list_task_options(self):
        task = self.get_callback_data()
        self.set_task(task)
        queue_name = 'Task.Listing.TaskOptions.list_task_options'
        FactoryQueue.create(queue_name).init()
