import os
import sqlite3

PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(PROJECT_ROOT_DIR, 'data', 'app_data.db')
PROJECT_NAME = os.path.basename(PROJECT_ROOT_DIR)

os.environ['%s_PROJECT_ROOT_DIR' % PROJECT_NAME] = PROJECT_ROOT_DIR
os.environ['%s_DATABASE_PATH' % PROJECT_NAME] = DATABASE_PATH
os.environ['DASH_PROJECT_NAME'] = PROJECT_NAME
