from App.Queues.Standard.abstract_handler import AbstractHandler

class Update(AbstractHandler):
    _jobs = None
    
    def get_steps(self) -> list:
        return [
            'set_jobs',
            'register_jobs'
        ]

    def get_namespace(self) -> str:
        return 'Jobs.Daily'
    
    @staticmethod
    def set_jobs(jobs: list):
        Update._jobs = jobs
        
    @staticmethod
    def get_jobs():
        return Update._jobs 