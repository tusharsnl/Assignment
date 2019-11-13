class Path:
  def __init__(self,base_str):
    self.base_path = base_str
  def common(self,stack):
    l1 = imp_string.split('/')
    if('' in  l1):
      l1.remove('')
    for each in l1:
      if(each == '..'):
        stack.pop()
      else:
        stack.append(each)
  def cd(self, base_path):

    current_path = self.base_path
    stack = current_path.split('/')

    stack.remove('')
    if(imp_string[0]!='.'):
      if(imp_string[0].isalpha()):
        self.common(stack)
      else:
        stack[:]=[]
        self.common(stack)

    else:
      self.common(stack)
    s="/"
    for each in stack:
      s=s+each+'/'
    s = s[:-1]
    print(s)

base_str='/a/b/c/d'
imp_string='c/d'

path = Path(base_str)
path.cd(imp_string)
