import math
import os
import json
from datetime import datetime
from datetime import datetime

import pandas as pd
import openpyxl
import json

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

def s2d(str):
    return datetime.strptime(str, '%Y-%m-%d').date()

def s2dt(str):
    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S')

def s2t(str):
    return datetime.strptime(str, '%H:%M').time()

def poster_session_time(str):
    if str is None or type(str) == float:
        return ""
    def update(time):
        items = time.split(":")
        if len(items) == 1:
            # only number
            assert (items[0].strip() in ["2", "9"]), (items[0])
            if items[0].strip() == "2":
                return "14:00"
            elif items[0].strip() == "9":
                return "09:00"
        else:
            assert items[0].strip() in ["5", "12"]
            if items[0].strip() == "5":
                return "17:30"
            elif items[0].strip() == "12":
                return "12:30"

    def opt_item(item):
        start = item.split("-")[0].strip()
        end = item.split("-")[1].strip()
        start = update(start)
        end = update(end)
        return "{} - {}".format(start, end)

    items = str.split("\n")
    items = [opt_item(item) for item in items if item.strip() != ""]
    return "; ".join(items)

def prepare_tutorial_data(data_file):
    data = [
        [
            s2d("2024-03-21"), s2t("14:00"), s2t("17:30"), "Radisson", "T1", "Transformer-specific Interpretability",
            "Hosein Mohebbi, Jaap Jumelet, Michael Hanna, Afra Alishahi and Willem Zuidema",
            "tutorial-1", "Transformers have emerged as dominant players in various scientific fields, especially NLP. However, their inner workings, like many other neural networks, remain opaque. In spite of the widespread use of model-agnostic interpretability techniques, including gradient-based and occlusion-based, their shortcomings are becoming increasingly apparent for Transformer interpretation, making the field of interpretability more demanding today. In this tutorial, we will present Transformer-specific interpretability methods, a new trending approach, that make use of specific features of the Transformer architecture and are deemed more promising for understanding Transformer-based models. We start by discussing the potential pitfalls and misleading results model-agnostic approaches may produce when interpreting Transformers. Next, we discuss Transformer-specific methods, including those designed to quantify context-mixing interactions among all input pairs (as the fundamental property of the Transformer architecture) and those that combine causal methods with low-level Transformer analysis to identify particular subnetworks within a model that are responsible for specific tasks. By the end of the tutorial, we hope participants will understand the advantages (as well as current limitations) of Transformer-specific interpretability methods and how they can be applied to their own research work."
        ],
        [
            s2d("2024-03-21"), s2t("14:00"), s2t("17:30"), "Fortress 2", "T2", "LLMs for Low Resource Languages in Multilingual, Multimodal and Dialectal Settings",
            "Firoj Alam, Shammur Absar Chowdhury, Sabri Boughorbel and Maram Hasanain",
            "tutorial-2", "The recent breakthroughs in Artificial Intelligence (AI) can be attributed to the remarkable performance of Large Language Models (LLMs) across a spectrum of research areas (e.g., machine translation, question-answering, automatic speech recognition, text-to-speech generation) and application domains (e.g., business, law, healthcare, education, and psychology). The success of these LLMs largely depends on specific training techniques, most notably instruction tuning, RLHF, and subsequent prompting to achieve the desired output. As the development of such LLMs continues to increase in both closed and open settings, evaluation has become crucial for understanding their generalization capabilities across different tasks, modalities, languages, and dialects. This evaluation process is tightly coupled with prompting, which plays a key role in obtaining better outputs. There has been attempts to evaluate such models focusing on diverse tasks, languages, and dialects, which suggests that the capabilities of LLMs are still limited for medium-to-low-resource languages due to the lack of representative datasets. The tutorial offers an overview of this emerging research area. We explore the capabilities of LLMs in terms of their performance, zero- and few-shot settings, fine-tuning, instructions tuning, and close vs. open models with a special emphasis on low-resource settings. In addition to LLMs for standard NLP tasks, we will focus on speech and multimodality."
        ],
        [
            s2d("2024-03-21"), s2t("9:00"), s2t("17:30"), "Fortress 1", "T3", "Computational modeling of semantic change",
            "Pierluigi Cassotti, Francesco Periti, Stefano De Pascale, Haim Dubossarsky and Nina Tahmasebi",
            "tutorial-3", "This tutorial provides an overview of current approaches, problems and challenges in the detection of lexical semantic change. At its core, computational modelling of semantic change consists of the following: (1) Modelling word meaning, typically using unsupervised methods applied to diachronic corpora; (2) modelling meaning change, based on the results of the above; (3) evaluation. The tutorial will provide an introduction to lexical semantic change and an overview of the resources available (corpora, pre-trained diachronic models and data sets). We will highlight issues related to the creation and use of diachronic corpora and different procedures for annotating data. We will then present the current state of the art in automatic detection of LSC, provide a hands-on section on available systems and tools, and open the floor for discussion on possible applications."
        ],
        [
            s2d("2024-03-21"), s2t("9:00"), s2t("12:30"), "Fortress 2", "T4", "Item Response Theory for Natural Language Processing",
            "João Sedoc, John P. Lalor, Pedro Rodriguez and Jose Hernandez-Orallo",
            "tutorial-4", "This tutorial will introduce the NLP community to Item Response Theory (IRT). IRT is a method from the field of psychometrics for model and dataset assessment. IRT has been used for decades to build test sets for human subjects and estimate latent characteristics of dataset examples. Recently, there has been an uptick in work applying IRT to tasks in NLP. It is our goal to introduce the wider NLP community to IRT and show its benefits for a number of NLP tasks. From this tutorial, we hope to encourage wider adoption of IRT among NLP researchers.",
        ],
        [
            s2d("2024-03-21"), s2t("9:00"), s2t("12:30"), "Radisson", "T5", "Language+Molecules",
            "Carl Edwards, Qingyun Wang and Heng Ji",
            "tutorial-5", "Climate change, access to food and water, pandemics— these words, when uttered, immediately summon to mind global challenges with possible disastrous outcomes. Molecular solutions will be critical to addressing these global problems on scales of complexity never-before-seen. However, they exist in extremely large search spaces, which makes AI tools a necessity. Excitingly, the chemistry field is posed to be substantially accelerated via multimodal models combining language with molecules and drug structures."
        ]
    ]
    column_names = ['Date', 'Start Time', 'End Time', 'Room', 'Id', 'Title',
                    'Authors', 'Rocketchat', 'Desc']

    sheet_name = "Tutorials Schedule"
    # df = pd.DataFrame(
    #     data,
    #     columns=column_names
    # )
    # df.to_excel("input.xlsx", index=False, sheet_name="Tutorials Schedule")

    return data, column_names, sheet_name

def prepare_workshop_data(data_file):
    def _get_link_if_exists(cell):
        try:
            return cell.hyperlink.target
        except AttributeError:
            return None

    df = pd.read_excel('EACL24-Events.xlsx', sheet_name='EACL 2024 Workshops')
    ws = openpyxl.load_workbook(filename=data_file)['EACL 2024 Workshops']
    data = []
    for index, row in df.iterrows():
        if index == 0 or index > 20:
            continue

        day = row[2] # row['Day
        start_time = row[10] # row['Start time']
        end_time = row[15] # row['End time']
        room = "{}, {}".format(row[3], row[4]) # row['Hotel'] + ", " + row['Ballroom']
        shortname = row[8] # row['Acronym & Direct Link to Interested attendees']
        workshop_id = "Workshop-{}".format(row[7]) # + row['Wkshp #']
        title = row[9] # title
        organizers = row[38] # row['Organizer(s): First name, Last name']
        sponsors = row[29] # row['Sponsor Name(s)']
        poster_session = row[26]
        poster_session = poster_session_time(poster_session)
        desc = ""
        url = _get_link_if_exists(ws.cell(row=index+2, column=10))

        data.append(
            [day.date(), start_time, end_time, room, shortname, workshop_id, title,
             organizers, poster_session, sponsors, desc, url]
        )

    column_names = ['Date', 'Start Time', 'End Time', 'Room',
                    'Shortname', 'Id', 'Title', 'organizers',
                    'Poster Session', 'Sponsors', 'Desc', 'url']

    sheet_name = "Workshops Schedule"
    df1 = pd.DataFrame(
        data,
        columns=column_names
    )
    df1.to_excel("input.xlsx", index=False, sheet_name="Workshops Schedule")

    return data, column_names, sheet_name


def prepare_plenary_data(data_file):
    data = [
        ["EACL 2024 General Chair", "opening-session", "Opening Session and Presidential Address", "",
         "In-Person", "March 18 - Time: 08:00 - 08:30", "TBD", "EACL 2024"],
        ["Hongning Wang", "keynote-01", "Human vs. Generative AI in Content Creation Competition: Symbiosis or Conflict?", "",
         "In-Person", "March 18 - Time: 08:30 - 09:30", "Dr. Hongning Wang is now an associate professor at the Department of Computer Science and Technology at Tsinghua University. Prior to that, he was the Copenhaver Associate Professor in the Department of Computer Science at the University of Virginia. He received his PhD degree in computer science at the University of Illinois at Champaign-Urbana in 2014. His research generally lies in the intersection among machine learning and information retrieval, with a special focus on sequential decision optimization and computational user modeling. His work has generated over 100 research papers in top venues in data mining and information retrieval areas. He is a recipient of 2016 National Science Foundation CAREER Award, 2020 Google Faculty Research Award, and SIGIR’2019 Best Paper Award.",
         "Tsinghua University"],
        ["Hinrich Schütze", "keynote-02", "Quality Data for LLMs: Challenges and Opportunities for NLP", "",
         "In-Person", "March 19 - Time: 08:00 - 09:00", "Hinrich Schuetze is Professor at the Center for Information and Language Processing at LMU Munich. His lab is engaged in research on multilinguality, representation learning and linguistic analysis of NLP models. His research has been funded by NSF, the German National Science Foundation and the European Research Council (ERC Advanced Grant), inter alia. Hinrich is coauthor of two well-known textbooks (Foundations of Statistical Natural Language Processing and Introduction to Information Retrieval), a fellow of HessianAI, ELLIS (the European Laboratory for Learning and Intelligent Systems) and ACL (Association for Computational Linguistics) and (co-)awardee of several best paper awards and the ACL 2023 25-year test of time award.",
         "Ludwig Maximilian University of Munich"],
        ["EACL 2024 Board", "business-meeting", "Business Meeting", "",
         "In-Person", "March 19 - Time: 12:00 - 12:45", "TBD", "EACL 2024"],
        ["Mirella Lapata", "keynote-03", "Prompting is not all you need! Or why Structure and Representations still matter in NLP", "",
         "In-Person", "March 20 - Time: 13:45 - 14:45", "Mirella Lapata is professor of natural language processing in the School of Informatics at the University of Edinburgh. Her research focuses on getting computers to understand, reason with, and generate natural language. She is the first recipient (2009) of the British Computer Society and Information Retrieval Specialist Group (BCS/IRSG) Karen Sparck Jones award and a Fellow of the Royal Society of Edinburgh, the ACL, and Academia Europaea. Mirella has also received best paper awards in leading NLP conferences and has served on the editorial boards of the Journal of Artificial Intelligence Research, the Transactions of the ACL, and Computational Linguistics. She was president of SIGDAT (the group that organizes EMNLP) in 2018. She has been awarded an ERC consolidator grant, a Royal Society Wolfson Research Merit Award, and a UKRI Turing AI World-Leading Researcher Fellowship.",
         "University of Edinburgh"],
        ["EACL 2024 General Chair", "best-paper", "Best Paper Awards", "",
         "In-Person", "March 20 - Time: 15:00 - 15:45", "TBD", "EACL 2024"],
        ["EACL 2024 General Chair", "closing-session", "Closing Remarks & Upcoming Conference Announcements", "",
         "In-Person", "March 20 - Time: 15:45 - 16:30", "TBD", "EACL 2024"],
    ]
    column_names = ['Presenter', 'id', 'Title', 'Session Name', 'Presentation Mode', 'Desc', 'bio', 'ins']

    sheet_name = "Plenary Schedule"
    df1 = pd.DataFrame(
        data,
        columns=column_names
    )
    df1.to_excel("input.xlsx", index=False, sheet_name="Plenary Schedule")

    return data, column_names, sheet_name

def prepare_break_data(data_file):
    data = [
        ["coffee-break-1", s2d("2024-03-18"), s2t("10:30"), s2t("11:00"), "Coffee Break", "Breaks", "Coffee Break 1"],
        ["lunch-break-1", s2d("2024-03-18"), s2t("12:30"), s2t("14:00"), "Lunch Break", "Breaks", "Lunch Break 1"],
        ["coffee-break-2", s2d("2024-03-18"), s2t("15:30"), s2t("16:00"), "Coffee Break", "Breaks", "Coffee Break 2"],
        ["coffee-break-3", s2d("2024-03-19"), s2t("10:00"), s2t("10:30"), "Coffee Break", "Breaks", "Coffee Break 3"],
        ["lunch-break-2", s2d("2024-03-19"), s2t("12:00"), s2t("13:00"), "Lunch Break", "Breaks", "Lunch Break 2"],
        ["coffee-break-4", s2d("2024-03-19"), s2t("15:30"), s2t("16:00"), "Coffee Break", "Breaks", "Coffee Break 4"],
        ["coffee-break-5", s2d("2024-03-20"), s2t("10:30"), s2t("11:00"), "Coffee Break", "Breaks", "Coffee Break 5"],
        ["lunch-break-3", s2d("2024-03-20"), s2t("12:30"), s2t("14:00"), "Lunch Break", "Breaks", "Lunch Break 3"],
        ["coffee-break-6", s2d("2024-03-20"), s2t("15:45"), s2t("16:15"), "Coffee Break", "Breaks", "Coffee Break 6"],
        ["coffee-break-7", s2d("2024-03-21"), s2t("10:30"), s2t("11:00"), "Coffee Break", "Breaks", "Coffee Break 7"],
        ["lunch-break-4", s2d("2024-03-21"), s2t("12:30"), s2t("14:00"), "Lunch Break", "Breaks", "Lunch Break 4"],
        ["coffee-break-8", s2d("2024-03-21"), s2t("15:30"), s2t("16:00"), "Coffee Break", "Breaks", "Coffee Break 8"],
        ["coffee-break-9", s2d("2024-03-22"), s2t("10:30"), s2t("11:00"), "Coffee Break", "Breaks", "Coffee Break 9"],
        ["lunch-break-5", s2d("2024-03-22"), s2t("12:30"), s2t("14:00"), "Lunch Break", "Breaks", "Lunch Break 5"],
        ["coffee-break-10", s2d("2024-03-22"), s2t("15:30"), s2t("16:00"), "Coffee Break", "Breaks", "Coffee Break 10"],
    ]
    column_names = ['id', 'Date', 'Start Time', 'End Time', 'Track', 'Type', 'Session']

    sheet_name = "Breaks Schedule"
    df1 = pd.DataFrame(
        data,
        columns=column_names
    )
    df1.to_excel("input.xlsx", index=False, sheet_name="Breaks Schedule")

    return data, column_names, sheet_name

def write_to_excel(data_file):
    # prepare_tutorial_data(data_file=data_file)
    # prepare_workshop_data(data_file)
    # prepare_plenary_data(data_file)
    prepare_break_data(data_file)
if __name__ == "__main__":
    data_file = "EACL24-Events.xlsx"
    write_to_excel(data_file)


