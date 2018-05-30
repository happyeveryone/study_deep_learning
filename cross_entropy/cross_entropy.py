import numy as np

def cross_entropy(Y, P):
  Y = np.float_(Y)
  P = np.float_(P)
  return -np.sum(Y * np.exp(P) + (1-Y) * np * np.exp(1 - P))
