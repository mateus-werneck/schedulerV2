from App.Data.Helpers.inline_keyboard_helper import (append_exit_button,
                                                     treat_keyboard,
                                                     treat_menu)
from App.Data.Helpers.message_helper import (calendar_icon, category_icon,
                                             group_icon, pin_icon)
from App.Handlers.agenda_handler import AgendaHandler
from App.Lib.Bot.chat import BotChat
from App.Lib.Bot.client import BotClient
from App.Queues.Schedule.Listing.Schedule.list_schedule_options import \
    ListScheduleOptions


class ListCategories(ListScheduleOptions):

    def handle(self) -> bool:
        self.set_callback()
        return super().handle()

    def set_callback(self):
        menu = self.send_menu()
        callback_function = AgendaHandler.instance().execute
        BotClient.instance().add_callback_handler(menu, callback_function)

    def send_menu(self):
        title = self.get_title()
        menu = self.get_menu()
        BotChat.instance().send_callback_query(title, menu)
        return menu

    def get_title(self):
        return f'Escolha uma categoria {category_icon()}'

    def get_menu(self):
        menu_name = 'main_agenda'
        options = treat_keyboard(self.get_options(), menu_name, 2)
        append_exit_button(options, menu_name)
        return treat_menu(options)

    def get_options(self):
        return [
            {
                'id': 'list_schedule',
                'name': f'{calendar_icon()} Cronograma'
            },
            {
                'id': 'list_tasks',
                'name': f' {pin_icon()} Tarefas'
            },
               {
                'id': 'list_grades',
                'name': f'{group_icon()} Turmas'
            }
        ]
