from App.Queues.Schedule.Listing.Daily.list_daily import ListDaily
from App.Lib.Client.marina_api import MarinaAPI
from App.Data.Helpers.task_helper import get_tasks_from_schedules
from App.Lib.Treat.time_treat import treat_datetime_to_string_hour
from App.Lib.Bot.chat import BotChat
from App.Lib.Bot.client import BotClient
from App.Data.Helpers.inline_keyboard_helper import (append_exit_button,
                                                     treat_keyboard,
                                                     treat_menu)
from App.Data.Helpers.message_helper import category_icon


class ListAll(ListDaily):

    def handle(self):
        self.set_callback()
        return super().handle()

    def set_callback(self):
        menu = self.send_menu()
        callback_function = TaskHandler.instance().execute
        BotClient.instance().add_callback_handler(menu, callback_function)

    def send_menu(self):
        title = self.get_title()
        menu = self.get_menu()
        BotChat.instance().send_callback_query(title, menu)
        return menu

    def get_title(self):
        return f'Escolha uma tarefa {category_icon()}'

    def get_menu(self):
        menu_name = 'daily_tasks'
        options = treat_keyboard(self.get_tasks(), menu_name, 2)
        append_exit_button(options, menu_name)
        return treat_menu(options)