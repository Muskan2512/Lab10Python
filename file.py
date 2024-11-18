# write a python source code file and count sthe occurrences of each word in the file.

def CountOccurrences(file_name):
  fp=open(f"{file_name}","r")
  val=fp.read()
  val=val.lower().split(" ")
  d={}
  for i in val:
    exists=i in d
    if(exists):
      d[i]+=1
    else:
      d[i]=1
  return d

# CountOccurrences("demo.txt")

def NonDuplicates():
  file=input("Enter the filename:")
  d=CountOccurrences(file)
  l=[x for x,y in d.items() if y==1 and x not in '., ;1']
  l.sort()
  return l
# print(NonDuplicates())

# wapp that prompts the user to enter the text file name and display sthe number of vowels and consonants in the file.user a set to store the vowel and consonants.

def CountVowelsNConso():
  file_name=input("Enter the filename:")
  fp=open(f"{file_name}","r")
  val=fp.read()
  vowels,consonants=0,0
  s=set()
  for i in val:
    if i in 'aeiouAEIOU':
      vowels+=1
      s.add(i)
    elif i in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
      consonants+=1
  
  print(f"The number of vowels and consonants in the files are:{vowels},{consonants}")
  print("The set contains:",s)

# CountVowelsNConso()

def removeNewLine():
  file_name=input("Enter the filename:")
  fp=open(f"{file_name}","r+")
  fp.seek(0)
  val=fp.read()
  val=val.split("\n")
  print(val)
  val=''.join(val)
  # print(val)
  fp.seek(0)
  fp.write(val)

# removeNewLine()


import pandas as pd

def CSV():
  file_name=input("Enter the filename:")
  df = pd.read_csv(f'{file_name}')
  # Write the content to the destination CSV file
  
  # index=False will actually prevent the indexing done on the destination file 
  df.to_csv('destination.csv', index=False)
  print("Content copied from source.csv to destination.csv")
CSV()
  