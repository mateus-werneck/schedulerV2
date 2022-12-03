from App.Data.Helpers.inline_keyboard_helper import (append_exit_button,
                                                     treat_menu)
from App.Data.Helpers.message_helper import category_icon, down_face
from App.Handlers.grade_handler import GradeHandler
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

        callback_function = GradeHandler.instance().execute
        BotClient.instance().add_callback_handler(menu, callback_function)

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
        return treat_menu(options, 'grade_tasks')

    def get_options(self):
        grade = self.get_grade()
        return MarinaAPI.instance().list_grade_tasks(grade)
