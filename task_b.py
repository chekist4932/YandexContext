from datetime import datetime, timedelta, date
import calendar


def str_to_date(date_string_: str):
    return datetime.strptime(date_string_, "%Y-%m-%d").date()


def detail_by_month(start_: date, end_: date):
    start_date = start_
    details = []

    while True:

        month_ = start_date.month
        year_ = start_date.year
        day = calendar.monthrange(year_, month_)[1]
        end_date = date(year_, month_, day)
        if end_date > end_ or end_date == end_:
            end_date = end_
            details.append((start_date, end_date))
            return details

        details.append((start_date, end_date))
        start_date = end_date + timedelta(days=1)


def detail_by_year(start_: date, end_: date):
    start_date = start_
    details = []
    while True:

        month_ = start_date.month
        year_ = start_date.year
        diff = 12 - month_
        month_ += diff

        day = calendar.monthrange(year_, month_)[1]
        end_date = date(year_, month_, day)
        if end_date > end_ or end_date == end_:
            end_date = end_
            details.append((start_date, end_date))
            return details

        details.append((start_date, end_date))
        start_date = end_date + timedelta(days=1)


def detail_by_quarter(start_: date, end_: date):
    start_date = start_
    details = []

    while True:

        month_ = start_date.month
        year_ = start_date.year

        if month_ % 3 == 0:
            diff = 0
        else:
            diff = 3 - (month_ % 3)
        month_ += diff

        if month_ > 12:
            year_ += 1
            month_ -= 12

        day = calendar.monthrange(year_, month_)[1]
        end_date = date(year_, month_, day)
        if end_date > end_ or end_date == end_:
            end_date = end_
            details.append((start_date, end_date))
            return details

        details.append((start_date, end_date))
        start_date = end_date + timedelta(days=1)


def get_diff(month):
    if month in [1, 2, 3]:
        diff = 3 - month
    elif month in [10, 11, 12]:
        diff = 15 - month
    elif month in [4, 5, 6, 7, 8, 9]:
        diff = 9 - month
    return diff


def detail_by_review(start_: date, end_: date):
    start_date = start_
    details = []

    while True:

        month_ = start_date.month
        year_ = start_date.year
        diff = get_diff(month_)

        month_ += + diff
        if month_ > 12:
            year_ += 1
            month_ -= 12

        day = calendar.monthrange(year_, month_)[1]
        end_date = date(year_, month_, day)
        if end_date > end_ or end_date == end_:
            end_date = end_
            details.append((start_date, end_date))
            return details

        details.append((start_date, end_date))
        start_date = end_date + timedelta(days=1)


def detail_by_week(start_: date, end_: date):
    start_date = start_
    details = []

    while True:

        end_date = start_date + timedelta(days=6 - start_date.weekday())
        if end_date > end_ or end_date == end_:
            end_date = end_
            details.append((start_date, end_date))
            return details
        details.append((start_date, end_date))
        start_date = end_date + timedelta(days=1)


with open('input.txt', 'r') as file:
    parameters = file.readlines()
    mode = parameters[0].strip()
    date_start, date_end = [str_to_date(date_string.strip()) for date_string in parameters[1].split()]

res = []
if mode == "WEEK":
    res = detail_by_week(date_start, date_end)
elif mode == "MONTH":
    res = detail_by_month(date_start, date_end)
elif mode == "QUARTER":
    res = detail_by_quarter(date_start, date_end)
elif mode == "YEAR":
    res = detail_by_year(date_start, date_end)
elif mode == "REVIEW":
    res = detail_by_review(date_start, date_end)

with open('output.txt', 'w') as file:
    file.write(str(len(res)))
    for i in res:
        file.write(f"\n{str(i[0])} {str(i[1])}")


# M, W, R, Q, Y