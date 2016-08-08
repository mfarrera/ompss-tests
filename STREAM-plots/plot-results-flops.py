#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys
import re
import matplotlib.pyplot as plt


def main():
  f = open('stream-results-ompss.txt','r')
  s = f.read()
  #match = re.search(r'Triad:\s*',s)
  match = re.findall(r'Triad:\s+(\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s*.*',s)
  if not match:
    print ('did not find')
    sys.exit(0)

## Blocksize in MB
  blocksizelist=[float(x[0])/1024/1024 for x in match]
## Rate in MB/s
  throughputlistompss=[float(x[5]) for x in match]
  print (blocksizelist)
  print (throughputlistompss)

  f = open('stream-results-serial.txt','r')
  s = f.read()
  #match = re.search(r'Triad:\s*',s)
  match = re.search(r'Triad:\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s*.*',s)
  if not match:
    print ('did not find')
    sys.exit(0)

## Rate in MB/s
  throughputlistserial=[float(match.group(5)) for x in blocksizelist]
  print (throughputlistserial)
  
  f = open('stream-results-openmp.txt','r')
  s = f.read()
  #match = re.search(r'Triad:\s*',s)
  match = re.search(r'Triad:\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s*.*',s)
  if not match:
    print ('did not find')
    sys.exit(0)

## Rate in MB/s
  throughputlistopenmp=[float(match.group(5)) for x in blocksizelist]
  print (throughputlistopenmp)

#times_s = [ x[0] for x in tuple_list_st]
#plt.figure(1)
#plt.subplot(211)
  plt.title("Stream Triad")
  plt.plot(blocksizelist,throughputlistompss,label="OmpSs")
  plt.plot(blocksizelist,throughputlistserial,label="Serial")
  plt.plot(blocksizelist,throughputlistopenmp,label="OpenMP")
  plt.xlabel('Block size (MB)')
  plt.xscale('log')
  plt.xticks(blocksizelist,blocksizelist)
  plt.ylabel('Flops/s')
  plt.legend(prop={'size':10})

  plt.show()
  return


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
