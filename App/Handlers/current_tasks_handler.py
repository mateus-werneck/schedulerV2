from App.Data.Helpers.task_helper import get_base_task_message
from App.Handlers.Standard.factory_handler import FactoryHandler
from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Standard.factory_queue import FactoryQueue


class CurrentTasksHandler(AbstractHandlerRequest):

    def get_command(self) -> str:
        return 'tarefas'

    def get_steps(self) -> list:
        return [self.answer_tasks_options, self.handle_actions]

    def get_parent_handler_name(self) -> str:
        return 'agenda_handler'

    def answer_tasks_options(self):
        self.delete_message()

        if self.is_create_task_mode():
            return self.ask_task_data()
        elif self.is_list_task_mode():
            return self.list_tasks()

    def is_create_task_mode(self):
        return self.is_mode('tasks_only_create_task')

    def is_list_task_mode(self):
        return self.is_mode('tasks_only_list_tasks')

    def ask_task_data(self):
        message = self.get_ask_message()
        self.send_message('Informe a tarefa que deseja cadastrar seguindo'
                          + ' o exemplo abaixo.')
        self.send_message(self.get_ask_message())
        return True

    def get_ask_message(self):
        return get_base_task_message()\
            .format(
                name='Tirar fotos para o Brechó',
                description='Finalizar ensaio do Brechó',
                due_date='31/12/2022',
                delivery_date='15:30'
        )

    def list_tasks(self):
        FactoryQueue.create('Schedule.Listing.All.list_all_tasks')\
            .init()
        return True

    def handle_actions(self):
        if self.has_callback_data():
            return self.start_task_mode()
        return self.create_task()

    def start_task_mode(self):
        handler = FactoryHandler.create('schedules_handler')
        handler.start_task_mode()
        return True

    def create_task(self):
        if not self.has_valid_text_data():
            self.send_message('Por favor informe uma tarefa válida.')
            return False

        queue = FactoryQueue.create('Task.Create.create')
        queue.init()
        return True
