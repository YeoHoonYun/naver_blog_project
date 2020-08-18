import json

class word_class:
    def __init__(self):
        pass

    def hello(self):
        command_list = []
        return command_list

    def ok(self):
        command_list = []
        return command_list

    def sumeon(self):
        command_list = []
        command_list.append(["/services/light/turn_on","light.living_room"])
        return command_list
    def uaochul(self):
        command_list = []
        command_list.append(["/services/light/turn_off","light.living_room"])
        return command_list

    def word_dic(self, body):
        return {
            ('안녕하세요', 'NNP'): {
                "functions": self.hello(),
                "message" : "Hello",
                "type": "인사"
            },
            ("?","SF") : {
                ('되', 'VV') : {
                    ('잘', 'MAG') : {
                        ('실행', 'NNP') : {
                            "functions": self.ok(),
                            "message": "잘 실행되었습니다.",
                            "type": "긍정"
                        }
                    }
                },
                ('되', 'XSV'): {
                    ('잘', 'MAG'): {
                        ('실행', 'NNG'): {
                            "functions": self.ok(),
                            "message": "잘 실행되었습니다.",
                            "type": "긍정"
                        }
                    }
                }
            },
            ('모드', 'NNP') : {
                ('수면', 'NNP') : {
                    ('실행', 'NNP') : {
                        "functions": self.sumeon(),
                        "message": "수면모드를 실행합니다.",
                        "type": "모드실행"
                    }
                },
                ('외출', 'NNP'): {
                    ('실행', 'NNP'): {
                        "functions": self.uaochul(),
                        "message": "외출모드를 실행합니다.",
                        "type": "모드실행"
                    }
                }
            }
        }
