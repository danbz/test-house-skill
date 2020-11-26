from mycroft import MycroftSkill, intent_file_handler


class TestHouse(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('house.test.intent')
    def handle_house_test(self, message):
        self.speak_dialog('house.test')


def create_skill():
    return TestHouse()

