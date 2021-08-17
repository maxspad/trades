from icalendar import Calendar, Event

ical_file = 'schedule.ics'
with open(ical_file) as f:
    ical_text = f.read()
cal = Calendar.from_ical(ical_text)
w = cal.walk()
print(len(w))
print(type(w[0]))
print(type(w[1]))
print(type(w[-1]))
print(w[1])
print(w[1].decoded('DTSTAMP'))
print(type(w[1].decoded('DTSTAMP')))
print(w[1].decoded('eggs', default='cheese'))
print(w[1].property_items())

def event_to_dict(e):
    event_keys = []