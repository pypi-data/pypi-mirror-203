import os

class Actions(object):

    def execute_directory_actions(self, dir_path):
        for action in list(filter(lambda x: x.endswith('_directory'), dir(self))):
            getattr(self, action)(dir_path)

    def execute_file_actions(self, dir_path, file_name):
        for action in list(filter(lambda x: x.endswith('_file'), dir(self))):
            getattr(self, action)(dir_path, file_name)

    def execute_final_actions(self):
        for action in list(filter(lambda x: x.endswith('_final'), dir(self))):
            getattr(self, action)()

class Walker(object):

    def __init__(self, visit_hidden_directories=False):
        self.visit_hidden_directories = visit_hidden_directories

    def accept(self, directory, action_engine):
        for dirName, subdirList, fileList in os.walk(directory):
            action_engine.execute_directory_actions(dirName)
            for fname in fileList:
                action_engine.execute_file_actions(dirName, fname)
            if not self.visit_hidden_directories:
                for subdir in subdirList:
                    if subdir.startswith('.'):
                        subdirList.remove(subdir)
        action_engine.execute_final_actions()
