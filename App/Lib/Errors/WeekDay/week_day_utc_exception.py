class WeekDayUtcNotFoundException(Exception):
    def __init__(self):
        self.message = '[WeekDay] Dia da semana UTC não foi encontrado.'
        super().__init__(self.message)