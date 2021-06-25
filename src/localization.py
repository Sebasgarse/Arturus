import os
import json
from src.public.singleton import SingletonType

class localization(metaclass=SingletonType):
    _DIR = 'local/languages/'
    _LANGUAGE_CONFIG_DIR = 'language.ini'
    _DEFAULT_LANGUAGE = 'spanish'

    def __init__(self):
        self._create_user_language()
        self._get_user_language()
        self._create_dir()
        self._get_language_data()
        self.__dict__ = self._language_data

    def _create_user_language(self):
        if (not os.path.exists(self._LANGUAGE_CONFIG_DIR)):
            language_config = open(self._LANGUAGE_CONFIG_DIR, 'w')
            language_config.write(self._DEFAULT_LANGUAGE)
            language_config.close()

    def _get_user_language(self):
        language_config = open(self._LANGUAGE_CONFIG_DIR)
        language_config_data = language_config.read()
        self._language = language_config_data
        language_config.close()

    def _create_dir(self):
        if (not os.path.exists(self._DIR)):
            os.mkdir('local')
            os.mkdir(self._DIR)
        
    def _get_language_data(self):
        language_archive = open(f'{self._DIR}{self._language}.json')
        self._language_data = {}
        archive_data = language_archive.read()
        self._language_data = json.loads(archive_data)
        language_archive.close()


