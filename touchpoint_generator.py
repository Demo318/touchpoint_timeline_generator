"""
This script is design to automatically generate
a touch-point timeline for sales reps reaching
out to prospective clients.
"""

from datetime import date
from datetime import timedelta as delta

# PSUEDO CODE
# Collect today's time & date ✔
# Timeline saved as array inside Timeline class.✔
#   Each week is an array, [Touchpoint Action,
#                           Day range to complete,
#                           How many days until next touch]

# Identify first day as today ✔
#   Offset from weekends ✔
# Iterate over to make pretty looking list
# Offer week or day shifting
# GUI date picker?


prospecting_actions = [
    ["Call/Voicemail/Email", 4, 7],
    ["Call/Voicemail/Email", 4, 7],
    ["Send Value-Add w/out Ask", 4, 7],
    ["Optional: Mug/Gift Drop", 4, 7],
    ["Call/Voicemail/Email", 4, 7],
    ["LinkedIn Connection/Message", 4, 14],
    ["Call/Voicemail/Email", 4, 21],
    ["Assess Account Strategy", 4, 0]
]


def validate_to_next_weekday(today_var):
    if today_var.weekday == 0:
        today_var = today_var + delta(days=1)
    elif today_var.weekday == 7:
        today_var = today_var + delta(days=2)
    else:
        today_var


today = date.today()
