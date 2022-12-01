from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from App.Data.Helpers.inline_keyboard_helper import treat_menu
from App.Data.Helpers.message_helper import (add_icon, category_icon,
                                             open_book_icon)
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
        list_name = 'main_agenda'
        options = self.get_options()
        return treat_menu(options, list_name)

    def get_options(self):
        return [
            {
                'id': 'create_schedule',
                'name': f'{add_icon()} Cadastrar cronograma'
            },
            {
                'id': 'show_schedule',
                'name': f'{open_book_icon()} Visualizar cronograma da semana'
            }
        ]
