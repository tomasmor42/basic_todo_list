import datetime

import pytest

import service

TASK_ID = 1
TASK_TEXT = "text text"
TASKS = {TASK_ID: TASK_TEXT}

def test_get_task_id_exists(tasks):
    result_task = service.get_task(TASK_ID)
    assert result_task == TASK_TEXT

def test_get_task_doesnt_exist(tasks):
    result_task = service.get_task(2)
    assert result_task is None

def test_get_all_tasks_empty(tasks_empty):
    service.TASKS = {}
    all_tasks = service.get_all_tasks()
    assert all_tasks == {}
    service.TASKS = TASKS

def test_get_all_tasks_not_empty(tasks):
    all_tasks = service.get_all_tasks()
    assert all_tasks == TASKS

def test_create_task_success():
    date = (
            datetime.datetime.now() + 
            datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
    task = service.create_task(date, TASK_TEXT)
    assert task 

def test_create_task_in_the_past():
    date = (
            datetime.datetime.now() - 
            datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
    
    task = service.create_task(date, TASK_TEXT)
    assert task is None
