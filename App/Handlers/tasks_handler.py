from App.Lib.Standard.abstract_handler_request import AbstractHandlerRequest
from App.Queues.Standard.factory_queue import FactoryQueue


class TasksHandler(AbstractHandlerRequest):
    _grade = None

    @classmethod
    def get_grade(cls):
        return cls._grade

    @classmethod
    def set_grade(cls, grade: str):
        cls._grade = grade

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
        self.send_message(message)
        return True

    def get_ask_message(self):
        return 'Informe a tarefa que deseja cadastrar' \
            + '(nome, descrição, dia e hora).\n<b>Exemplos</b>\n\n'\
            + '1 - Preparar Aula 05, Começar a preparação da aula 05,\
            <b>quarta</b>, <b>19:30</b>\n'\
            + '2 - Corrigir provas, corrigir as provas escritas,\
            <b>22/10/2022</b>, <b>15:22</b>'

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
