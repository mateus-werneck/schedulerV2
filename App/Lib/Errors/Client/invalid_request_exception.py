class InvalidRequestException(Exception):
    def __init__(self, message='Nenhuma requisição válida foi informada', api='BaseAPI'):
        self.message = f'[{api}] {message}'
        super().__init__(self.message)
