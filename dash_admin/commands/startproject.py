import os
from .base import Base
from distutils.dir_util import copy_tree
import sqlite3

MODULE_FOLDER = os.path.dirname(os.path.abspath(__file__))

db_init_sql = """
DROP TABLE IF EXISTS USERS;

CREATE TABLE USERS (
  USERNAME TEXT PRIMARY KEY,
  PASSWORD TEXT
);

INSERT INTO USERS (USERNAME, PASSWORD)

VALUES ('admin', 'admin');
"""


class StartProject(Base):
    """Start a Dash project!"""

    def run(self):
        self.project_name = self.options['<projectname>']
        self.project_root_directory = os.path.join(os.getcwd(), self.project_name)

        # Make sure the project_root_directory doesn't already exist
        if not os.path.exists(self.project_root_directory):
            os.makedirs(self.project_root_directory)

        else:
            raise OSError(\
        '\n\n\nYou must run "startproject" in a directory that does not contain a sub-directory with the project name.'\
        '  You attempted to create a project named "%s" when the path "%s" already exists.'  \
        '  Delete the directory "%s" or change to a different directory and run "startproject" again.\n' % (self.project_name,
                                                                                                  self.project_root_directory,
                                                                                                  self.project_root_directory)
                        )

        copy_tree(os.path.join(MODULE_FOLDER, 'boilerplate'), self.project_root_directory)

        # Initiate the database
        conn = sqlite3.connect(os.path.join(self.project_root_directory, 'data', 'app_data.db'))
        conn.executescript(db_init_sql)
        conn.commit()
        conn.close()
