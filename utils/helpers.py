from datetime import datetime

def date_today():
    return datetime.now().strftime("%Y-%m-%d")

def date_validate(date_txt):
    if date_txt:
        try:
            datetime.strptime(date_txt, "%Y-%m-%d")
            return date_txt
        except ValueError:
            raise ValueError("Дата должна быть YYYY-MM-DD")
        
def amount_validate(amount):
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError("Введена отрицательная сумма")
        return amount
    except ValueError:
        raise ValueError("Некорректный тип данных")