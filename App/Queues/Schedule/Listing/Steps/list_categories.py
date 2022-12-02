from App.Data.Helpers.inline_keyboard_helper import (append_back_button,
                                                     treat_menu)
from App.Data.Helpers.message_helper import (calendar_icon, category_icon,
                                             group_icon, pin_icon)
from App.Handlers.schedule_handler import ScheduleHandler
from App.Lib.Bot.chat import BotChat
from App.Lib.Bot.client import BotClient
from App.Queues.Schedule.Listing.list_schedule_options import \
    ListScheduleOptions


class ListCategories(ListScheduleOptions):

    def handle(self) -> bool:
        self.set_callback()
        return super().handle()

    def set_callback(self):
        menu = self.send_menu()
        callback_function = ScheduleHandler.instance().execute
        BotClient.instance().add_callback_handler(menu, callback_function)

    def send_menu(self):
        title = self.get_title()
        schedule_menu = self.get_menu()
        BotChat.instance().send_callback_query(title, schedule_menu)
        return schedule_menu

    def get_title(self):
        return f'Escolha uma categoria {category_icon()}'

    def get_menu(self):
        options = self.get_options()
        append_back_button(options)
        return treat_menu(options, 'main_agenda')

    def get_options(self):
        return [
            {
                'id': 'list_grades',
                'name': f'{group_icon()} Turmas'
            },
            {
                'id': 'list_schedule',
                'name': f'{calendar_icon()} Cronograma'
            },
            {
                'id': 'list_tasks',
                'name': f' {pin_icon()} Tarefas'
            }
        ]
