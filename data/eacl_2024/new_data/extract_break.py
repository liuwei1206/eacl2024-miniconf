import pandas as pd
import json
from util import str_to_date

df = pd.read_excel('input.xlsx', sheet_name='Event Sessions')
data = {}
display_data = {}

count = 0
for index, row in df.iterrows():
    if row['Track name'].lower() != "breaks & social":
        continue
    # start_time = row['Date'].strftime('%Y-%m-%dT') + row['Start Time'].strftime('%H:%M:%S')
    # end_time = row['Date'].strftime('%Y-%m-%dT') + row['End Time'].strftime('%H:%M:%S')
    start_time = str_to_date(row['Starts at'])
    end_time = str_to_date(row['Ends at'])

    break_name = row['Name']
    break_id = break_name
    count += 1

    break_data = {
        'chairs': [],
        'end_time': end_time,
        'id': break_id,
        'link': None,
        'paper_ids': [],
        'room': None,
        'session': "Break {}".format(count),
        'start_time': start_time,
        'track': "Break",
        'type': "Breaks"
    }
    data[break_id] = break_data

    display_break_data = {
        'display_name': "Break {}".format(count),
        'end_time': end_time,
        'events': {
            break_id: {
                'chairs': [],
                'end_time': end_time,
                'id': break_id,
                'link': None,
                'paper_ids': [],
                'room': None,
                'session': "Break {}".format(count),
                'start_time': start_time,
                'track': "Break",
                'type': "Break"
            }
        },
        'id': break_id,
        'name': "Break {}".format(count),
        'plenary_events': {},
        'start_time': start_time,
        'tutorial_events': {},
        'type': "break",
        'workshop_events': {}
    }
    display_data["Break {}".format(count)] = display_break_data

with open('json_data/break.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('json_data/display_break.json', 'w') as file:
    json.dump(display_data, file, indent=4)
