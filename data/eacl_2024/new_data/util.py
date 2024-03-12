import os
import json
from datetime import datetime

def str_to_date(s):
    items = s.split()
    print(items)
    month = "03"
    day = items[1].strip().strip(",")
    year = items[2].strip()
    hour = items[3].split(":")[0].strip()
    minute = items[3].split(":")[1].strip()
    datestring = "{}-{}-{} {}:{}:00".format(
        year,
        month,
        day,
        hour,
        minute
    )

    return datestring

