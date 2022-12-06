from App.Data.Helpers.inline_keyboard_helper import (append_exit_button,
                                                     treat_menu, append_custom_button)
from App.Data.Helpers.message_helper import category_icon, down_face, add_icon
from App.Handlers.tasks_handler import TasksHandler
from App.Lib.Bot.chat import BotChat
from App.Lib.Bot.client import BotClient
from App.Lib.Client.marina_api import MarinaAPI
from App.Queues.Grade.Listing.Tasks.list_tasks import ListTasks


class ListAll(ListTasks):

    def handle(self) -> bool:
        self.set_callback()
        return super().handle()

    def set_callback(self):
        menu = self.send_menu()

        if menu is None:
            self.send_message(f'{down_face()} Nenhuma tarefa foi encontrada.')
            return

        callback_function = TasksHandler.instance().execute
        BotClient.instance().add_callback_handler(menu, callback_function)
        TasksHandler.instance().set_grade(self.get_grade())

    def send_menu(self):
        title = self.get_title()
        menu = self.get_menu()
        if menu is not None:
            BotChat.instance().send_callback_query(title, menu)
        return menu

    def get_title(self):
        return f'Escolha uma opção {category_icon()}'

    def get_menu(self):
        options = self.get_options()

        if not options:
            return None

        append_exit_button(options)
        return treat_menu(options, 'main_tasks', 2)

    def get_options(self):
        grade = self.get_grade()
        options = MarinaAPI.instance().list_grade_tasks(grade)
        append_custom_button(options, 'create_task',
                             f' {add_icon()} Cadastrar Tarefa')
        return options
