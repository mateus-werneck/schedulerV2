from App.Data.Helpers.inline_keyboard_helper import (append_exit_button,
                                                     treat_keyboard,
                                                     treat_menu)
from App.Data.Helpers.message_helper import (category_icon, cross_mark_icon,
                                             edit_icon, open_book_icon, add_icon)
from App.Handlers.grade_handler import GradeHandler
from App.Lib.Bot.chat import BotChat
from App.Lib.Bot.client import BotClient
from App.Queues.Grade.Listing.GradeOptions.list_grades_options import \
    ListGradesOptions


class ListCategories(ListGradesOptions):

    def handle(self) -> bool:
        self.set_callback()
        return super().handle()

    def set_callback(self):
        menu = self.send_menu()
        callback_function = GradeHandler.instance().execute
        BotClient.instance().add_callback_handler(menu, callback_function)

    def send_menu(self):
        title = self.get_title()
        menu = self.get_menu()
        BotChat.instance().send_callback_query(title, menu)
        return menu

    def get_title(self):
        return f'Escolha uma opção {category_icon()}'

    def get_menu(self):
        menu_name = 'main_grade'
        options = treat_keyboard(self.get_options(), menu_name)
        append_exit_button(options, menu_name)
        return treat_menu(options)

    def get_options(self):
        return [
            {
                'id': 'list_tasks',
                'name': f'{open_book_icon()} Listar Tarefas'
            },
            {
                'id': 'create_task',
                'name': f'{add_icon()} Cadastrar Tarefa'
            },
            {
                'id': 'edit_grade',
                'name': f'{edit_icon()} Editar Turma'
            },
            {
                'id': 'delete_grade',
                'name': f'{cross_mark_icon()} Deletar Turma'
            }
        ]
