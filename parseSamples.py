import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import *

class StanfordNLP:
    def __init__(self):
        self.server = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(addr=("127.0.0.1", 8080)))
    
    def parse(self, text):
        return json.loads(self.server.parse(text))

nlp = StanfordNLP()
#result = nlp.parse("Can you hand me a psuedophed?")
#pprint(result)


#Loop for the easy sample data
easy = open("easy.txt","r")
resultEasy = open("resultEasy.txt","w")
for line in easy:
    parsed = nlp.parse(line)
    #comand for writing to result file
    pprint(parsed,resultEasy)
resultEasy.close()
easy.close()


medium = open("medium.txt","r")
resultMedium = open("resultMedium.txt","w")
for line in medium:
    parsed = nlp.parse(line)
    #comand for writing to result file
    pprint(parsed,resultMedium)
resultMedium.close()
medium.close()

hard = open("hard.txt","r")
resultHard = open("resultHard.txt","w")
for line in hard:
    parsed = nlp.parse(line)
    #comand for writing to result file
    pprint(parsed,resultHard)
resultHard.close()
hard.close()



#from nltk.tree import Tree
#tree = Tree.parse(result['sentences'][0]['parsetree'])
#pprint(tree)
