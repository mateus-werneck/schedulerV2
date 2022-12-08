from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Standard.factory_queue import FactoryQueue
from App.Lib.Client.marina_api import MarinaAPI

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
        return [self.list_task_options, self.answer_task_options]

    def list_task_options(self):
        task = self.get_callback_data()
        self.set_task(task)
        queue_name = 'Task.Listing.TaskOptions.list_task_options'
        FactoryQueue.create(queue_name).init()

    def answer_task_options(self):
        if self.is_edit_task_mode():
            self.edit_task()
        elif self.is_delete_task_mode():
            return self.delete_task()

    def is_edit_task_mode(self):
        return self.is_mode('main_task_edit_task')

    def edit_task(self):
        task = MarinaAPI.instance().find_task(self.get_task())
        

    def is_delete_task_mode(self):
        return self.is_mode('main_task_delete_task')

    def delete_task(self):
        queue_name = 'Task.Delete.delete'
        queue = FactoryQueue.create(queue_name)
        queue.set_task(self.get_task())
        queue.init()
        return False
