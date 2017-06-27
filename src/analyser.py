import string
from storage import Storage

class Analyser():
    def __init__(self):
        pass

    def remove_punctuation(self, data_list):
        corrected_list = []
        for e in data_list:
            if '\n' not in e:
                for word in e.split():
                    l = list(word.lower())
                    word = ''
                    for x in l:
                        if x not in string.punctuation:
                            word += x
                    corrected_list.append(word)

        return corrected_list

    def analyse_emotion(self, data_list):
        emo = Storage()

        data_list = self.remove_punctuation(data_list)
        # print data_list
        wt_angry = 0
        wt_sad = 0
        wt_happy = 0

        for word in data_list:
            try:
                # print word
                res = emo.search_for_keyword('emotions', 'C:\Users\Nirmal\PycharmProjects\Scr_dbms\data_storage', 'Emotions02', word)
                print res
                if res[0][1] == 'angry':
                    wt_angry += res[0][2]
                if res[0][1] == 'sad':
                    wt_sad += res[0][2]
                if res[0][1] == 'happy':
                    wt_happy += res[0][2]
            except:
                pass

        return wt_angry, wt_sad, wt_happy
