from App.Data.Helpers.task_helper import get_base_task_message
from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Standard.factory_queue import FactoryQueue


class TasksHandler(AbstractHandlerRequest):
    _grade = None

    @staticmethod
    def get_grade(cls):
        return TasksHandler._grade

    @staticmethod
    def set_grade(grade: str):
        TasksHandler._grade = grade

    def get_command(self) -> str:
        return ''

    def get_steps(self) -> list:
        return [self.answer_tasks_options, self.create_task]

    def answer_tasks_options(self):
        self.delete_message()

        if self.is_create_task_mode():
            return self.ask_task_data()

        return self.start_task_mode()

    def is_create_task_mode(self):
        return self.is_mode('main_tasks_create_task')

    def ask_task_data(self):
        message = self.get_ask_message()
        self.send_message('Informe a tarefa que deseja cadastrar seguindo'
                          + ' o exemplo abaixo.')
        self.send_message(self.get_ask_message())
        return True

    def get_ask_message(self):
        return get_base_task_message()\
            .format(
                name='Preparar Lição 1',
                description='Finalizar a preparação da Lição 1',
                due_date='22/12/2022',
                delivery_date='19:30'
        )

    def start_task_mode(self):
        queue = 'Task.Listing.TaskOptions.list_task_options'
        FactoryQueue.create(queue).init()
        return False

    def create_task(self):
        if not self.has_valid_text_data():
            self.send_message('Por favor informe uma tarefa válida.')
            return False

        queue = FactoryQueue.create('Task.Create.create')
        queue.set_grade(self.get_grade())
        queue.init()
