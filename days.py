from datetime import datetime, timedelta
def days():
    presentday = datetime.now()  # or presentday = datetime.today()
    tomorrow = presentday + timedelta(1)
    aftertomorrow=presentday + timedelta(2)

    DAYS = [presentday.strftime('%Y-%m-%d'), tomorrow.strftime('%Y-%m-%d'), aftertomorrow.strftime('%Y-%m-%d')]
    return DAYS