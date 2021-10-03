from mycroft import MycroftSkill, intent_file_handler


class Condoprova(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('condoprova.intent')
    def handle_condoprova(self, message):
        self.speak_dialog('condoprova')


def create_skill():
    return Condoprova()

