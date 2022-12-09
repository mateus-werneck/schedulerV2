from App.Data.Helpers.inline_keyboard_helper import (append_back_button,
                                                     treat_keyboard,
                                                     treat_menu)
from App.Data.Helpers.message_helper import (category_icon, calendar_icon)
from App.Handlers.schedules_handler import SchedulesHandler
from App.Lib.Bot.chat import BotChat
from App.Lib.Bot.client import BotClient
from App.Queues.Schedule.Listing.Schedules.list_schedules_options import \
    ListSchedulesOptions


class ListCategories(ListSchedulesOptions):

    def handle(self) -> bool:
        self.set_callback()
        return super().handle()

    def set_callback(self):
        menu = self.send_menu()
        callback_function = SchedulesHandler.instance().execute
        BotClient.instance().add_callback_handler(menu, callback_function)

    def send_menu(self):
        title = self.get_title()
        menu = self.get_menu()
        BotChat.instance().send_callback_query(title, menu)
        return menu

    def get_title(self):
        return f'Escolha um opção de cronograma {category_icon()}'

    def get_menu(self):
        menu_name = 'schedule'
        options = treat_keyboard(self.get_options(), menu_name, 3)
        append_back_button(options, menu_name)
        return treat_menu(options)

    def get_options(self):
        return [
            {
                'id': 'list_daily',
                'name': f'{calendar_icon()} Diário'
            },
            {
                'id': 'list_weekly',
                'name': f' {calendar_icon()} Semanal'
            },
               {
                'id': 'list_monthly',
                'name': f'{calendar_icon()} Mensal'
            }
        ]
