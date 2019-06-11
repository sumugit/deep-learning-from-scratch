import sys, os
sys.path.append(os.pardir)
from datasets.mnist import load_mnsit

(X_train, t_train), (X_test, t_test) = \
  load_mnist(flatten=True, normalization=False)
  
  
print(x_train.shape)
