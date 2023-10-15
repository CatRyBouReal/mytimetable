# Import libraries used
from guizero import App, ListBox, Text, PushButton, Box
from classes import Subject, Day

# Set timetable subjects in 2D list. Each list inside is a day.
# Each item in a day is a period
while True:
    try:
        TIMETABLE = eval(open("timetable.conf").read())
        if type(TIMETABLE) != list:
            raise ValueError("There is an error in your config file")
        break
    except(Exception):
        error_app = App("Error", height = 80, width = 250)
        text = Text(error_app, "There is an error in your config file")
        box = Box(error_app, align="bottom", width="fill")
        button = PushButton(box, error_app.destroy, text = "Ok", align="right")
        error_app.display()
        exit()


# Initialise functions
def get_day_names():
    days = []
    for day in TIMETABLE:
        days.append(day.name)
    return days


def fetch_subject(day: str, period: int) -> Subject:
    for table_day in TIMETABLE:
        if table_day.name == day:
            func_day = table_day
            break
    return func_day.subjects[period - 1]


def change_text_to_sub(text: Text):
    text.value = "You have {} with {} on {} during period {} at {}".format(
        fetch_subject(day_list.value, period_list.value).name,
        fetch_subject(day_list.value, period_list.value).teacher,
        day_list.value,
        period_list.value,
        fetch_subject(day_list.value, period_list.value).room
    )


main_app = App("MyTimetable", width=910)

title_box = Box(main_app, width="fill", align="top")
title_text = Text(title_box, "MyTimetable", 50)

content_box = Box(main_app, width="fill")
period_list = ListBox(content_box, [], align="right")
day_list = ListBox(content_box, get_day_names(), align="left")

def change_period_list(day: str):
    period_list.clear()
    for table_day in TIMETABLE:
        if table_day.name == day:
            for i in range(1, len(table_day.subjects) + 1):
                period_list.append(i)
            break
    period_list.children[0].tk.select_set(0)

day_list.update_command(change_period_list)

day_list.children[0].tk.select_set(0)

change_period_list(day_list.value)

subject_text = Text(content_box, "Please select 2 options")
button = PushButton(content_box, change_text_to_sub, [subject_text],
                    "Show subject")

main_app.display()