import pandas as pd
import json
from util import str_to_date

df = pd.read_excel('input.xlsx', sheet_name='Event Sessions')
data = []

for index, row in df.iterrows():
    if row['Track name'].lower() != "tutorials":
        continue
    # start_time = row['Date'].strftime('%Y-%m-%dT') + row['Start Time'].strftime('%H:%M:%S')
    # end_time = row['Date'].strftime('%Y-%m-%dT') + row['End Time'].strftime('%H:%M:%S')
    start_time = str_to_date(row['Starts at'])
    end_time = str_to_date(row['Ends at'])

    tutorial_name = row['Name']
    tutorial_id = tutorial_name.split(":")[0]

    tutorial_data = {
        'id': tutorial_id,
        'title': tutorial_name,
        'desc': "",
        'location': row['Room'],
        'start_time': start_time,
        'end_time': end_time,
        'hosts': "",
        'rocketchat': ""
    }

    data.append(tutorial_data)

final_data = {
    "tutorials": data
}

with open('json_data/tutorial.json', 'w') as file:
    json.dump(final_data, file, indent=4)
