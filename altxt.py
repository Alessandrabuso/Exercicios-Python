""""




Inclua um método que retorne a distância entre duas palavras"""

class AlTxt():
    __path = ''
    __fl = None
    __txt = None
    __pnt = [",", ".", ";", ":", "!","?", "-"]
    __sw = ["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself",
            "youselves","he","him","his","himself","she","her","hers","herself","it","its","itself",
            "they","them","their","theirs","themselves","what","which","who","whom","this","that",
            "these","those","am", "is","are","was","were","be","been","being","have","has","had",
            "having","do","does","did","doing","a","an","the","and","but","if","or","because",
            "as","until","while","of","at","by","for","with","about","against","between","into",
            "through", "during", "before", "after","above","below","to","from","up","down","in",
            "out","on","off","over","under","again","further","then","once","here","there","when",
            "where","why","how","all","any","both","each","few","more","most","other","some","such",
            "no","nor","not","only","own","same","so","than","too","very","s","t","can","will",
            "just","don","should","now","i'm"]
    __stopwrds = []

    def __init__(self, pth):
        self.__path = pth
        self.__fl = open(pth, 'r')
        self.__txt = self.__fl.readlines()

    def strlist(self):
        # Representa um texto como uma lista de Strings
        text = [line.replace("\n", "") for line in self.__txt]
        return text

    def strsep(self):
        # Retorna individualmente cada palavra do texto
        b = []
        a = [i.split() for i in self.__txt if i != None]
        for c in a:
            for word in c:
                for letter in word:
                    if letter in self.__pnt:
                        word = word.replace(letter,"")
                b.append(word)

        return b

    def ocrr(self):
        # Conta a quantidade de ocorrências de cada palavra do texto
        lis = self.strsep()
        a = [i.lower() for i in lis]
        a.sort()
        b = a[:]
        tempo = []
        out = []
        dic = {}
        temp = [[item for item in a if item == palavra] for palavra in b]
        for item in temp:
            if item not in out:
                out.append(item)
                tempo.append(len(item))
        for i in range(len(tempo)):
            dic[out[i][0]] = tempo[i]
        return dic

    def tenmost(self):
        # Retorne as 10 palavras mais frequentes
        dic = list(self.ocrr())
        return dic[0:10]

    def mdesvio(self):
        # Retorna a média e desvio padrão da quantidade de ocorrências
        a = 0
        b = 0
        dic = self.ocrr()
        bas = len(dic.values())
        for i in dic.values():
            a += i
        md = a/bas
        for i in dic.values():
            b += (i-md)**2
        dv = (b/bas   )**(1/2)
        return md, dv

    def stopword(self):
        # Cadastra StopWords
        # Retorne um novo arquivo eliminando todas as StopWords do texto
        lst = self.strsep()
        out = ''
        arq = open("no_sw.txt", 'w')
        for word in lst:
            if word in self.__sw and word not in self.__stopwrds:
                self.__stopwrds.append(word)
        for line in self.__txt:
            b = [y.replace("\n","") for y in line.split(" ")]
            for word in b:
                if word.lower() not in self.__sw:
                    out += word
                    out += " "
            arq.write(out)
            arq.write("\n")
            out = ''
        arq.close()
        return self.__stopwrds

    def dist(self, stra, strb):
        # Retorna a distância entre duas palavras
        import textdistance
        return (textdistance.levenshtein(stra, strb))


obj = AlTxt('/home/alessandra/Exercicios Python/she.txt')

#print(obj.strlist())
#print(obj.strsep())
#print(obj.ocrr())
#print(obj.tenmost(   ))
#print(obj.mdesvio())
#print(obj.stopword())
print(obj.dist('arrow','arow'))





