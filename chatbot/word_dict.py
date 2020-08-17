import json

class word_class:
    def __init__(self):
        pass

    def hello(self):
        command_list = []
        command_list.append("Hello!")
        return command_list

    def ok(self):
        command_list = []
        command_list.append("잘 됩니다. 걱정하지마세요.")
        return command_list

    def sumeon(self):
        command_list = []
        command_list.append("수면모드를 실행합니다.")
        command_list.append("전등을 끕니다.")
        command_list.append("청소기를 끕니다.")
        return command_list
    def uaochul(self):
        command_list = []
        command_list.append("외출모드를 실행합니다.")
        command_list.append("전등을 킵니다.")
        command_list.append("청소기를 킵니다.")
        return command_list

    def word_dic(self, body):
        return {
            ('안녕하세요', 'NNP'): {
                "functions": self.hello(),
                "type": "인사"
            },
            ("?","SF") : {
                ('되', 'VV') : {
                    ('잘', 'MAG') : {
                        ('실행', 'NNP') : {
                            "functions": self.ok(),
                            "type": "긍정"
                        }
                    }
                },
                ('되', 'XSV'): {
                    ('잘', 'MAG'): {
                        ('실행', 'NNG'): {
                            "functions": self.ok(),
                            "type": "긍정"
                        }
                    }
                }
            },
            ('모드', 'NNP') : {
                ('수면', 'NNP') : {
                    ('실행', 'NNP') : {
                        "functions": self.sumeon(),
                        "type": "모드실행"
                    }
                },
                ('외출', 'NNP'): {
                    ('실행', 'NNP'): {
                        "functions": self.sumeon(),
                        "type": "모드실행"
                    }
                }
            }
        }