import json
from src.public.singleton import SingletonType

class user(metaclass=SingletonType):
    name = ''
    age = ''
    intro = ''
    number_of_entries = 0

    def to_json(self):
        json_form = {
                'name': self.name,
                'age': self.age,
                'intro': self.intro,
                'entries': self.number_of_entries
            }
        return json.dumps(json_form)

    def from_json(self, data):
        json_form = json.loads(data)
        self.name = json_form['name']
        self.age = json_form['age']
        self.intro = json_form['intro']
        self.number_of_entries = json_form['entries']

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nIntro: {self.intro}'