import jieba

# An dictionary from Chinese to English
class ZH_dic:
    __dict:dict = {}
    def __init__(self):
        with open("translation.txt") as fp:
            line = fp.readline()
            while line:
                #process
                words = line.strip().split()
                self.__dict.update({words[0]: words[1]})
                line = fp.readline()
        pass
    def get(self, word:str):
        return self.__dict.get(word, None)

zh_dic:ZH_dic = ZH_dic()

# extract keyword from wordlist(only Chinese, support trandational Chinese)
def spiltWord(wordsZH:str):
    global zh_dic
    seg_list = jieba.cut(wordsZH, cut_all=True, HMM=False)
    # print("/ ".join(seg_list))
    for seg in seg_list:
        trans = zh_dic.get(seg)
        if trans is not None:
            return trans
    return "notunderstand"
