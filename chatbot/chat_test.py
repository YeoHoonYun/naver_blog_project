from PyKomoran import *
import word_dict

komoran = Komoran("EXP")

result = {}
word_dict = word_dict.word_class()
check_list = word_dict.word_dic

def deep_word(dic, word):
    global result
    result = {}
    for anal in dic.keys():
        if list(anal) in word:
            deep_word(dic[anal], word)

    if "functions" in dic.keys():
        result = dic

def word_anal(word,body):
    words = [str(x).split("/") for x in komoran.get_list(word)]
    print("POS : ", words)
    deep_word(check_list(body), words)
    print(result)
    try:
        for function in result.get("functions"):
            print("실행한 명령 : ", function)
        return result
    except:
        print("등록되지 않은 명령입니다. 선택할 명령을 다시 말해주세요..")
        result["message"] = "등록되지 않은 명령입니다. 곧 추가하겠습니다."
        return result

if __name__ == '__main__':
    result = {}
    while True:
        word = input("명령어를 입력하세요. \n")
        res = word_anal(word.lower(), "testYun")
        print("실행한 타입 : ", res)
        print("###########################")
