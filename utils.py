from datetime import timedelta


def date_range(start_date, end_date):
    num_days = (end_date - start_date).days
    date_list = sorted([end_date - timedelta(days=x) for x in range(num_days + 1)])
    return date_list
