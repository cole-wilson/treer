start = '/home'






















































import subprocess
import os
import time
print('\n\n\n\n\n')
def get():
  ls = str(subprocess.check_output(['ls']))
  ls = ls.replace('\\n',' ').replace('b\'','').replace('\'','')
  ls = ls.split()
  return ls


os.chdir(start)

c = get()
#print(get())



def main():
  #print(os.getcwd())
  tab = ''
  star = os.getcwd().count('/') - start.count('/')
  if os.getcwd() == start:
    tab = start + '/'
  else:
    for x in range(star-1):
      tab = tab + '|  '
    tab = tab + '├── '
  for x in get():
    print(tab + x)
    time.sleep(0)
    try:
      os.chdir(os.getcwd() + '/' + x)
      main()
    except PermissionError:
      print('------Permission Denied------')
      
    except:
      #print(tab + 'Error...')
      os.chdir(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
      

main()