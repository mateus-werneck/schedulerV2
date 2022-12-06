def list_split(value: list, parts: int):
    if not parts:
        return value
    return [value[i:i+parts] for i in range(0, len(value), parts)]
