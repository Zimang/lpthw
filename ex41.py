import random
from urllib.request import urlopen
import sys
WORD_URL="http://learncodethehardway.org/words.txt"
#array
WORDS=[]

#dic
PHRASES={
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef _init_(self,***)":
        "class %%% has-a _init_ that takes self and *** params",
    "class %%%(object):\n\tdef ***(self,@@@)":
        "class %%% has-a *** that takes self and @@@ params",
    "***=%%%()":
        "Set *** to an instance of class %%%.",
    "***=***(@@@)":
        "From *** get the *** func ,call it with params self, @@@.",
    "***.***='***'":
        "from *** get the *** atribute and set it to '***'"
}

#do they want to drill phrases first
if len(sys.argv)==2 and sys.argv[1]=="english":
    PHRASE_FIRST=True
else:
    PHRASE_FIRST=False

#load up the words from website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(),encoding="utf-8"))

def convert(snippet,phrases):
    #数组内赋值
    #[a.func() for a in array]
    class_names=[w.capitalize() for w in
                 random.sample(WORDS,snippet.count("%%%"))]
    other_names=random.sample(WORDS,snippet.count("***"))
    results=[]
    param_names=[]

    for i in range(0,snippet.count("@@@")):
        param_count=random.randint(1,3)
        param_names.append(", ".join(random.sample(WORDS,param_count)))

    for sentence in snippet,phrase:
        #[:]快捷复制数组的方法
        result=sentence[:]

        #fake class class_names
        for word in class_names:
            result=result.replace("%%%",word,1)

        #fake other names
        for word in other_names:
            result=result.replace("***",word,1)

        #fake param lists
        for word in param_names:
            result=result.replace("@@@",word,1)

        results.append(result)

    return results

#keep going until they hit CTRL_D
try:
    while True:
        snippets=list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase=PHRASES[snippet]
            question,answer=convert(snippet,phrase)
            if PHRASE_FIRST:
                question,answer=answer,question
            print(question)
            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
