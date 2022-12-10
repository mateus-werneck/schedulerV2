from App.Queues.Schedule.Listing.Weekly.list_weekly import ListWeekly
from App.Queues.Standard.factory_queue import FactoryQueue


class ListAll(ListWeekly):

    def handle(self):
        queue = FactoryQueue.create('Schedule.Listing.Tasks')
        queue.set_tasks(self.get_tasks())
        queue.init()
        return super().handle()
