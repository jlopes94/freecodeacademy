
def add_time(start, duration, start_day=None):
    # for later use
    tod_swap = 0
    days = 0
    f_day = ''
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

#  starting values
    s_tod = start.split(' ')[1]
    s_hour = int(start.split(':')[0])
    s_min = int(start.split(':')[1].split(' ')[0])

# modifier time values
    m_hour = int(duration.split(':')[0])
    m_min = int(duration.split(':')[1])

# new time values
    n_min = s_min + m_min
    n_hour = s_hour + m_hour

#  check for 12-hour cycle flip
    while n_min > 60:
        n_min -= 60
        n_hour += 1
    while n_hour >= 12:
        tod_swap += 1
        n_hour -= 12
    if n_hour == 0:
        n_hour = 12

#  check if days passed
    while tod_swap >= 1:
        if s_tod == 'AM':
            s_tod = 'PM'
            tod_swap -= 1
        else:
            s_tod = 'AM'
            tod_swap -= 1
            days += 1

#  if day of the week included, find the day we land on
    if start_day:
        start_day = start_day.lower()
        s_weekday = week.index(start_day)
        f_day = days % 7
        f_day = f_day + s_weekday
        if f_day > 6:
            f_day -= 7
        f_day = ', ' + week[f_day].capitalize()

# converting to string for output since no calculation is required
    n_hour = str(n_hour)
    n_min = str(n_min)

#  decide the formatting of output
    if days == 1:
        return n_hour + ':' + n_min.rjust(2, '0') + ' ' + s_tod + f_day + ' (next day)'
    elif days >= 2:
        return n_hour + ':' + n_min.rjust(2, '0') + ' ' + s_tod + f_day + ' (' + str(days) + ' days later)'
    else:
        return n_hour + ':' + n_min.rjust(2, '0') + ' ' + s_tod + f_day
