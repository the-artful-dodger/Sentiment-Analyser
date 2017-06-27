from storage import Storage

class Emotion():
    # Emotion Lists
    angry = ['acrimonious', 'angry', 'annoyed', 'appalled', 'bitter', 'boiling', 'cross', 'devastated', 'disgusted',
             'enraged', 'frustrated', 'fuming', 'furious', 'hostile', 'in a huff', 'in a stew', 'incensed', 'indignant',
             'inflamed', 'infuriated', 'irate', 'irritated', 'livid', 'mad', 'offended', 'outraged', 'piqued',
             'provoked', 'rageful', 'resentful', 'sullen', 'up in arms', 'virulent', 'worked up', 'wrathful']
    sad = ['aching', 'afflicted', 'agonized', 'anguished', 'bereaved', 'blue', 'cheerless', 'clouded', 'crestfallen',
           'crushed', 'dark', 'dejected', 'depressed', 'despairing', 'despondent', 'disconsolate', 'discontented',
           'discouraged', 'disheartened', 'dismal', 'displeased', 'distressed', 'dolorous', 'down', 'downcast',
           'downhearted', 'dreadful', 'dreary', 'dull', 'embarrassed', 'flat', 'frowning', 'funereal', 'gloomy', 'glum',
           'grief-stricken', 'grieved', 'guilt', 'hapless', 'heartbroken', 'heavyhearted', 'humiliated', 'hurt',
           'ill at ease', 'in despair', 'in pain', 'in the dumps', 'injured', 'joyless', 'lonely', 'low spirited',
           'low', 'lugubrious', 'melancholy', 'moody', 'moping', 'mournful', 'offended', 'oppressed', 'out of sorts',
           'pathetic', 'piteous', 'regretful', 'remorse', 'rueful', 'sad', 'shamed', 'shocked', 'somber', 'sorrowful',
           'spiritless', 'suffering', 'sulky', 'sullen', 'tortured', 'tragic', 'unhappy', 'victimized', 'woebegone',
           'woeful', 'worried']
    happy = ['airy', 'amused', 'animated', 'beatific', 'blissful', 'blithe', 'bright', 'brisk', 'buoyant', 'cheerful',
             'cheery', 'comfortable', 'contented', 'convivial', 'debonair', 'ecstatic', 'elated', 'enthusiastic',
             'excited', 'exhilarated', 'exultant', 'festive', 'free & easy', 'frisky', 'genial', 'glad', 'gleeful',
             'great', 'happy', 'high-spirited', 'hilarious', 'humorous', 'important', 'inspired', 'jaunty', 'jocular',
             'jolly', 'jovial', 'joyful', 'joyous', 'jubilant', 'laughing', 'lighthearted', 'lively', 'lucky', 'merry',
             'mirthful', 'overjoyed', 'peaceful', 'playful', 'pleased', 'proud', 'rapturous', 'satisfied', 'saucy',
             'self-satisfied', 'serene', 'sparkling', 'spirited', 'sprightly', 'sunny', 'terrific', 'thankful',
             'tranquil', 'transported', 'vivacious', 'delighted', 'ecstatic', 'fabulous', 'fantastic', 'overjoyed']

    def __init__(self):
        # Create emotions database
        self.emotionStorage = Storage('emotions', 'C:\Users\Nirmal\PycharmProjects\Scr_dbms\data_storage', 'Emotions02')

        # Enter emotions in table
        # (<Word>, <Emotion>, <Weight>)
        #   ANGRY
        for keyword in Emotion.angry:
            try:
                self.emotionStorage.create_new_entry('Emotions02', "".join(["'", keyword, "'"]), "'angry'", '1')
            except:
                pass

        #   SAD
        for keyword in Emotion.sad:
            try:
                self.emotionStorage.create_new_entry('Emotions02', "".join(["'", keyword, "'"]), "'sad'", '1')
            except:
                pass

        #   HAPPY
        for keyword in Emotion.happy:
            try:
                self.emotionStorage.create_new_entry('Emotions02', "".join(["'", keyword, "'"]), "'happy'", '1')
            except:
                pass
