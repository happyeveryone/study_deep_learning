import numpy as np

def softMax(L):
  expl = np.exp(L)
  sumexp = sum(L)
  result = []
  for i in expl:
    result.append(i*1.0/sumexp)
  return result

#def softmax(L):
#     expL = np.exp(L)
#     return np.divide (expL, expL.sum())
