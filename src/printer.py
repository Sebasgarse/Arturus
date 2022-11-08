import time
class printer:
    START = '\x1b['
    GREEN = '6;30;42'
    RED = '5;30;41'
    END = '\x1b[0m'

    def success(self, text):
        print(f'{self.START}{self.GREEN}m{text}{self.END}')

    def space(self):
        print('')

    def error(self, text: str):
        print(f'{self.START}{self.RED}m{text}{self.END}')

    def slowly(self, text: str, speed: int = 1):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(speed * 0.1)
        print('')

    def slowly_success(self, text: str, speed: int = 1):
        for char in text:
            print(f'{self.START}{self.GREEN}m{char}{self.END}', end='', flush=True)
            time.sleep(speed * 0.1)
        print('')
            