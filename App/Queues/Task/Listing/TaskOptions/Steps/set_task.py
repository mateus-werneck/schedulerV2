from App.Lib.Bot.chat import BotChat
from App.Queues.Task.Listing.TaskOptions.list_task_options \
    import ListTaskOptions


class SetTask(ListTaskOptions):

    def handle(self) -> bool:
        task = BotChat.instance().extract_callback_data()
        self.set_task(task)
        return super().handle()
