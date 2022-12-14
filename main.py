from src.printer import printer
from src.localization import localization as text
from src.user import user
from src.ui import MainWindow
from PyQt5.QtWidgets import QApplication
import os, sys

class main:
    TEXT_WIDTH = 80
    CONFIG_FILE_NAME = 'conf.ini'
    print = None
    user = user()

    def __init__(self):
        self.print = printer()
        self._printStart()
        self._verify_profile_files()
        self.app = QApplication(sys.argv)
        self.window = MainWindow()

    def _printStart(self):
        self.print.space()
        self.print.success('=' * self.TEXT_WIDTH)
        self.print.success(
            str(text().init).center(self.TEXT_WIDTH)
        )
        self.print.success('=' * self.TEXT_WIDTH)
        self.print.space()

    def _verify_profile_files(self):
        if (os.path.exists(self.CONFIG_FILE_NAME)):
            self.load_account()
        else:
            self.create_new_account()

    def create_new_account(self):
        try:
            self._query_config()
            self._create_config_file()
            self.print.success(text().safe_data)
        except Exception as exc:
            self.print.error(f'{text().error}: {exc}')
            if (os.path.exists(self.CONFIG_FILE_NAME)):
                os.remove(self.CONFIG_FILE_NAME)
        
    def _query_config(self):
        self.user.name = input(text().name)
        self._ask_age()
        self.user.intro = text().welcome

    def _ask_age(self):
        self.user.age = input(text().age)
        while (not self.user.age.isnumeric()):
            self.print.error(text().age_error)
            self.user.age = input(text().age)

    def _create_config_file(self):
        config_file = open(self.CONFIG_FILE_NAME, 'w')
        config_file.write(self.user.to_json())
        config_file.close()
        
    def load_account(self):
        config_file = open(self.CONFIG_FILE_NAME)
        config_file_data = config_file.read()
        self.user.from_json(config_file_data)
        self.print.slowly_success(text().safe_data)


if __name__ == '__main__':
    app = main()
    sys.exit(app.app.exec_())