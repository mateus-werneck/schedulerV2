from App.Data.Helpers.message_helper import edit_icon
from App.Data.Helpers.task_helper import treat_task_to_message
from App.Lib.Client.marina_api import MarinaAPI
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
        return [self.answer_task_options, self.edit_task]

    def answer_task_options(self):
        self.delete_message()
        
        if self.is_edit_task_mode():
            self.ask_edit_task()
        elif self.is_delete_task_mode():
            return self.delete_task()

    def is_edit_task_mode(self):
        return self.is_mode('main_task_edit_task')

    def ask_edit_task(self):
        task = MarinaAPI.instance().find_task(self.get_task())
        message = f'{edit_icon()} Informe a tarefa que deseja editar seguindo'\
            + ' o modelo abaixo.'
        self.send_message(message)
        self.send_message(treat_task_to_message(task))

    def is_delete_task_mode(self):
        return self.is_mode('main_task_delete_task')

    def delete_task(self):
        queue_name = 'Task.Delete.delete'
        queue = FactoryQueue.create(queue_name)
        queue.set_task(self.get_task())
        queue.init()
        return False

    def edit_task(self):
        queue_name = 'Task.Edit.edit'
        queue = FactoryQueue.create(queue_name)
        queue.set_task_id(self.get_task())
        queue.init()
