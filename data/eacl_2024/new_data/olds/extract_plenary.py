import pandas as pd
import json
from util import str_to_date

df = pd.read_excel('input.xlsx', sheet_name='Event Sessions')
data = []

for index, row in df.iterrows():
    if row['Track name'].lower() != "plenary sessions":
        continue
    # start_time = row['Date'].strftime('%Y-%m-%dT') + row['Start Time'].strftime('%H:%M:%S')
    # end_time = row['Date'].strftime('%Y-%m-%dT') + row['End Time'].strftime('%H:%M:%S')
    start_time = str_to_date(row['Starts at'])
    end_time = str_to_date(row['Ends at'])

    plenary_name = row['Name']
    plenary_id = plenary_name

    plenary_data = {
        'id': plenary_id,
        'title': plenary_name,
        'desc': "",
        'location': row['Room'],
        'start_time': start_time,
        'end_time': end_time,
        'bio': "",
        'speaker_name': "",
        "institution": "",
        "image": 'null'
    }

    data.append(plenary_data)

final_data = {
    "plenaries": data
}

with open('../json_data/plenary.json', 'w') as file:
    json.dump(final_data, file, indent=4)
