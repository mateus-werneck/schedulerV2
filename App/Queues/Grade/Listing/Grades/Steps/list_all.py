from App.Data.Helpers.inline_keyboard_helper import (append_exit_button,
                                                     treat_keyboard,
                                                     treat_menu)
from App.Data.Helpers.message_helper import category_icon, down_face
from App.Handlers.grade_handler import GradeHandler
from App.Lib.Bot.chat import BotChat
from App.Lib.Bot.client import BotClient
from App.Lib.Client.marina_api import MarinaAPI
from App.Queues.Grade.Listing.Grades.list_grades import ListGrades


class ListAll(ListGrades):

    def handle(self) -> bool:
        self.set_callback()
        return super().handle()

    def set_callback(self):
        menu = self.send_menu()

        if menu is None:
            self.send_message(f'{down_face()} Nenhuma turma foi encontrada.')
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
        return f'Escolha uma turma {category_icon()}'

    def get_menu(self):
        menu_name = 'grade'
        options = self.get_options()
        
        if not options:
            return None
        
        options = treat_keyboard(options, menu_name, 2)
        append_exit_button(options, menu_name)
        return treat_menu(options)

    def get_options(self):
        return MarinaAPI.instance().list_grades()
