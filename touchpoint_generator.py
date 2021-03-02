"""
This script is design to automatically generate
a touch-point timeline for sales reps reaching
out to prospective clients.
"""
import datetime
import calendar

# PSUEDO CODE
# Collect today's time & date ✔
# Timeline saved as array inside Timeline class.
#   Each week is an array, [Touchpoint Action,
#                           Day range to complete,
#                           How many days until next touch]

# Identify first day
#   Offset from weekends
# Iterate over to make pretty looking list


today = datetime.date.today()

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
