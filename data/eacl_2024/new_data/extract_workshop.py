import pandas as pd
import json
from util import str_to_date

def write_workshop_old():
    df = pd.read_excel('input.xlsx', sheet_name='Event Sessions')
    data = []

    for index, row in df.iterrows():
        if row['Track name'].lower() != "workshops":
            continue
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

    with open('json_data/workshop.json', 'w') as file:
        json.dump(final_data, file, indent=4)

def write_workshop():
    df = pd.read_excel('EACL24-Events.xlsx', sheet_name='EACL 2024 Workshops')
    data = []

    for index, row in df.iterrows():
        anthology_venue_id = ""
        booklet_id = ""
        chairs = ""
        committee = []
        description = row["Desc"]
        end_time = ""
        id = row["Id"]
        link = ""
        paper_ids = []
        room = row["Room"]
        session = row["Shortname"]
        short_name = row["Shortname"]
        start_time = ""
        track = "Workshop"
        type = "Workshops"
        workshop_site_url = row["url"]

        start_time = row["Date"] + " " + row["Start Time"] + ":00"
        end_time = row["Date"] + " " + row["Enti Time"] + ":00"
        organizers = row["organizers"]


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

    with open('json_data/workshop.json', 'w') as file:
        json.dump(final_data, file, indent=4)
