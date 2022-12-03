from App.Lib.Bot.chat import BotChat
from App.Queues.Task.Listing.TaskOptions.list_task_options \
    import ListTaskOptions


class SetTask(ListTaskOptions):

    def handle(self) -> bool:
        task = BotChat.instance().extract_callback_data()
        task = task.replace('main_tasks', '')
        self.set_task(task)
        return super().handle()
