import re
 
 
text = ['I','AAAPL','T']
cashtags = list(filter(lambda word:word != 'I'&&'T',text))
print(cashtags)                  