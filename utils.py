# setup
import ipywidgets as widgets
from ipywidgets import HBox, Layout
from IPython.display import Markdown
from ipywidgets import Checkbox, Button, HBox, VBox, Label
from os import path
import sqlite3

setup_sql = """create table survey (
                  qid text not null,
                  question text not null, 
                  choice text not null, 
                  comment text, 
                  pid text not null,
                  unique(qid, pid) 
               )"""
# all Likert Scales
# AGREE_OPTIONS = ['Strongly Agree', 'Agree', 'Undecided', 'Disagree', 'Strongly Disagree']
BINARY_OPTIONS = ['Yes', 'No']
TIME_OPTIONS = ['Always', 'Often', 'Sometimes', 'Rarely', 'Never']

def get_options(adjective):
    return [f'Very {adjective}', f'{adjective}', f'Moderately {adjective}', f'Slightly {adjective}', f'Not {adjective}',]


    
def get_comment(description):
    a = widgets.Textarea(description="Comments:")
    display(Markdown(f"### {description}"))
    display(a)
    return a


def get_radio(description, option, sub=None):
    value_idx = 2 if len(option) > 2 else 1
    r = widgets.RadioButtons(
        options=option,
        value=option[value_idx],
        description="",
    )
    a = widgets.Textarea(description="Comments:")
    md = f"#### <font color='blue'>{description}</font>"
    if sub:
        md += "\n" + "<font color='gray'>" + sub + "</font>"
    display(Markdown(md))
    display(HBox([r, a]))
    return r, a


def clean_str(s):
    return s.replace("'", '')

class MidasSurvey():
    def __init__(self, pid):
        self.pid = pid
        f_path = f"survey_{pid}.sqlite"
        run = True
        if path.exists(f_path):
            # if this alredy exists, don't run setup
            run = False
        
        self.con = sqlite3.connect(f_path)
        self.cur = self.con.cursor()
        
        if run:
            self.cur.execute(setup_sql)

    
    # if it already exists, then replace it
    def save_answer(self, q, r, a, qid):
        insert = f"INSERT OR REPLACE INTO survey VALUES ('{qid}', '{clean_str(q)}', '{r}', '{clean_str(a)}', '{self.pid}')"
        self.cur.execute(insert)
        self.con.commit()


