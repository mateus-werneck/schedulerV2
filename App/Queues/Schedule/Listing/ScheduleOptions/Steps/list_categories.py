from App.Data.Helpers.inline_keyboard_helper import (append_back_button,
                                                     append_exit_button,
                                                     treat_keyboard,
                                                     treat_menu)
from App.Data.Helpers.message_helper import (add_icon, category_icon,
                                             cross_mark_icon, edit_icon,
                                             open_book_icon)
from App.Handlers.current_tasks_handler import CurrentTasksHandler
from App.Lib.Bot.chat import BotChat
from App.Lib.Bot.client import BotClient
from App.Queues.Schedule.Listing.ScheduleOptions.list_schedule_options import \
    ListScheduleOptions


class ListCategories(ListScheduleOptions):

    def handle(self) -> bool:
        self.set_callback()
        return super().handle()

    def set_callback(self):
        menu = self.send_menu()
        callback_function = CurrentTasksHandler.instance().execute
        BotClient.instance().add_callback_handler(menu, callback_function)

    def send_menu(self):
        title = self.get_title()
        menu = self.get_menu()
        BotChat.instance().send_callback_query(title, menu)
        return menu

    def get_title(self):
        return f'Escolha uma opção {category_icon()}'

    def get_menu(self):
        menu_name = 'tasks_only'
        options = treat_keyboard(self.get_options(), menu_name)
        append_back_button(options, menu_name)
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
            }
        ]
