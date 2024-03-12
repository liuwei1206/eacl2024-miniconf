import pandas as pd
import json
from util import str_to_date

df = pd.read_excel('input.xlsx', sheet_name='Event Sessions')
data = []

for index, row in df.iterrows():
    if row['Track name'].lower() != "workshops":
        continue
    # start_time = row['Date'].strftime('%Y-%m-%dT') + row['Start Time'].strftime('%H:%M:%S')
    # end_time = row['Date'].strftime('%Y-%m-%dT') + row['End Time'].strftime('%H:%M:%S')
    start_time = str_to_date(row['Starts at'])
    end_time = str_to_date(row['Ends at'])

    workshop_name = row['Name']
    workshop_id = workshop_name.split(":")[0]

    workshop_data = {
        'id': workshop_id,
        'title': workshop_name,
        'desc': "",
        'location': row['Room'],
        'start_time': start_time,
        'end_time': end_time,
        'url': "",
        'chair': "",
    }
    data.append(workshop_data)

final_data = {
    "workshops": data
}

with open('workshop.json', 'w') as file:
    json.dump(final_data, file, indent=4)
