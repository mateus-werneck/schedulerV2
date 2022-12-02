from App.Data.Helpers.inline_keyboard_helper import (append_exit_button,
                                                     treat_menu)
from App.Data.Helpers.message_helper import (add_icon, group_icon,
                                             open_book_icon)
from App.Handlers.grade_handler import GradeHandler
from App.Lib.Bot.chat import BotChat
from App.Lib.Bot.client import BotClient
from App.Queues.Schedule.Listing.Grade.list_grade_options import \
    ListGradeOptions


class ListCategories(ListGradeOptions):

    def handle(self) -> bool:
        self.set_callback()
        return super().handle()

    def set_callback(self):
        menu = self.send_menu()
        callback_function = GradeHandler.instance().execute
        BotClient.instance().add_callback_handler(menu, callback_function)

    def send_menu(self):
        title = self.get_title()
        schedule_menu = self.get_menu()
        BotChat.instance().send_callback_query(title, schedule_menu)
        return schedule_menu

    def get_title(self):
        return f'Turmas {group_icon()}'

    def get_menu(self):
        options = self.get_options()
        append_exit_button(options)
        return treat_menu(options, 'agenda_grades')

    def get_options(self):
        return [
            {
                'id': 'create_grade',
                'name': f'{add_icon()} Cadastrar Turma'
            },
            {
                'id': 'show_grades',
                'name': f'{open_book_icon()} Visualizar Turmas'
            }
        ]
