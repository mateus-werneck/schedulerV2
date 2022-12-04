class WeekDayExceededException(Exception):
    def __init__(self):
        self.message = '[WeekDay] Limite de busca de dia da semana foi excedido.'
        super().__init__(self.message)