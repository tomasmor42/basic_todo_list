import unittest
import datetime

import service
import app

TASK_ID = 1
TASK_TEXT = "text text"
TASKS = {TASK_ID: TASK_TEXT}

class TestGetTask(unittest.TestCase):
    def test_id_exists(self):
        service.TASKS = TASKS
        task_id = TASK_ID
        result_task = service.get_task(task_id)
        self.assertEqual(result_task, TASK_TEXT)
    
    def test_id_doesnt_exist(self):
        service.TASKS = TASKS
        task_id = 2
        result_task = service.get_task(task_id)
        self.assertFalse(result_task)

class GetAllTasks(unittest.TestCase):
    def test_get_all_tasks_empty(self):
        service.TASKS = {}
        all_tasks = service.get_all_tasks()
        self.assertEqual(all_tasks, {})
    
    def test_get_all_tasks(self):
        service.TASKS = TASKS
        all_tasks = service.get_all_tasks()
        self.assertEqual(all_tasks, TASKS)

class CreateTask(unittest.TestCase):
    def test_create_task_success(self):
        date = (
            datetime.datetime.now() + 
            datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
        text = TASK_TEXT
        task = service.create_task(date, text)
        self.assertTrue(task)
    
    def test_create_task_in_past(self):
        date = (
            datetime.datetime.now() - 
            datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
        text = TASK_TEXT
        task = service.create_task(date, text)
        self.assertIsNone(task)
import sys

if __name__ == '__main__':
    unittest.main()