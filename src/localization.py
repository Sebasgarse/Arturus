import os
import json
from src.public.singleton import SingletonType

class localization(metaclass=SingletonType):
    DIR = 'local/languages/'
    LANGUAGE_CONFIG_DIR = 'language.ini'
    
    _language_data = None
    _language = ''

    def __init__(self):
        self._create_user_language()
        self._get_user_language()
        self._create_dir()
        self._get_language_data()
        self.__dict__ = self._language_data

    def _create_user_language(self):
        if (not os.path.exists(self.LANGUAGE_CONFIG_DIR)):
            language_config = open(self.LANGUAGE_CONFIG_DIR, 'w')
            language_config.write('spanish')
            language_config.close()

    def _get_user_language(self):
        language_config = open(self.LANGUAGE_CONFIG_DIR)
        language_config_data = language_config.read()
        self._language = language_config_data
        language_config.close()

    def _create_dir(self):
        if (not os.path.exists(self.DIR)):
            os.mkdir('local')
            os.mkdir(self.DIR)
        
    def _get_language_data(self):
        language_archive = open(f'{self.DIR}{self._language}.json')
        self._language_data = {}
        archive_data = language_archive.read()
        self._language_data = json.loads(archive_data)
        language_archive.close()


