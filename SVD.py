'''
Representing a Windows Based Concurrence Matrix
Corpus: The quick brown fox jumped over the moon and was happy with that.
- Make sure to convert everything to small
- X is the cooccurence Matrix
'''

import numpy as np
la =np.linalg
corpus= "the quick brown fox jumped over the moon and he was happy with that."

class concurrenceMatrix(object):
    """docstring for concurrenceMatrix."""
    def __init__(self):
        super(concurrenceMatrix, self).__init__()

    def breakintoWords(self, corpus):
        res = []
        temp = corpus.split(" ")
        res = temp[:-1]
        temp1 = temp[-1].split(".")
        res.append(temp1[0])
        res.append(temp[-1][-1])
        return res

    def ngram(self, words, type):
        listofngrams = list(zip(*[words[i:] for i in range(type)]))
        return listofngrams

    def arrayed(self,words):
        #Form a N*N array , which represent bigrams only for now
        #initialize
        N = len(words)
        X = [[0]*N for i in range(N)]
        listofngrams = self.ngram(words, 2)
        for idx, gram in enumerate(listofngrams):
            centerword = gram[0]
            for idx2,gram2 in enumerate(listofngrams):
                if centerword==gram2[0]:
                    idxnew = words.index(gram2[1])
                    X[idx][idxnew]=1
        return X

obj = concurrenceMatrix()
words = obj.breakintoWords(corpus)
X = np.asarray(obj.arrayed(words))
#print(X)
U, S, Vh = la.svd(X, full_matrices=False)

import matplotlib.pyplot as plt
#plotting the cooccurence Matrix
plt.figure()
#print(U.shape, S.shape, Vh.shape)
#print(U)
for i in range(len(words)):
    print(np.max(U[i,:]))
    plt.text(U[i,0], U[i,1], words[i])
#ax=plt.gca()
#ax.set_ylim([0,0.05])
#ax.set_xlim([0,0.03])
#plt.show()
