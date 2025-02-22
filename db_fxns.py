import sqlite3
conn = sqlite3.connect('data.db', check_same_thread=False)  # Path E:/Lean Streamlit in Python/exercise_files/exercise_files/1. Introduction __ 2.1 course_materials_learnstreamlit/course_materials_learnstreamlit/LearnStreamlit/Module01/Fundamentals_of_Streamlit/Mehran/todo_app/
c = conn.cursor()


# Database
# Table
# Field/Coloumns
# DataType

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT,task_status TEXT, task_due_date DATE)')

def add_data(task,task_status,task_due_date):
    c.execute('INSERT INTO taskstable(task,task_status,task_due_date) VALUES (?,?,?)',(task,task_status,task_due_date))
    conn.commit()


def view_all_data():
    c.execute('SELECT * FROM taskstable')
    data = c.fetchall()
    return data

def view_unique_tasks():
    c.execute('SELECT DISTINCT task FROM taskstable')
    data = c.fetchall()
    return data

def get_task(task):
    c.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
    # c.execute('SELECT * FROM taskstable WHERE task=?',(task))
    data = c.fetchall()
    return data
                   
def edit_task_data(new_task,new_task_status,new_task_date,task,task_status,task_due_date):
    c.execute("UPDATE taskstable SET task =?,task_status=?,task_due_date=? WHERE task=? and task_status=? and task_due_date=? ",(new_task,new_task_status,new_task_date,task,task_status,task_due_date))
    conn.commit()
    data = c.fetchall()
    return data


def delete_data(task):
    c.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))
    conn.commit()
    
