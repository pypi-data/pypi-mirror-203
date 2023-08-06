from datetime import datetime

def find(predicate, seq):
    return next(filter(predicate, seq), None)

def standard_file_name(file_prefix: str):
    current_datetime = datetime.now()
    day_str = current_datetime.strftime('%m%d%y')
    time_str = current_datetime.strftime('%H%M')
    file_name = f'{file_prefix}-{day_str}-{time_str}'
    return file_name
