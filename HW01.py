from datetime import datetime

def get_days_from_today(date: str):
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = target_date - today
        return delta.days


print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2026-12-24"))
