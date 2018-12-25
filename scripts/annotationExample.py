#! /usr/bin/env python

# This script is an example of how to get gene data from the annotation file.
# Maybe you really like my function for reading annotations and you want to import it into your own script.
# You can do that! Use the line below :
#
# from annotationExample import readAnnotations
#


def readAnnotations(fname) :
  annotations = {}
  start = False
  fh = open(fname, 'rt')
  lines = fh.readlines()
  fh.close()
  # We'll save the header as reference.
  header = lines[0].strip().split('\t')
  for line in lines[1:] :
    line = line.strip().split('\t')
    # We store the whole line so the header is a parallel list.
    # We could have stored each element in the list as a dict,
    #  but then "annotations" would have been a very large dict of dicts.
    # The computer probably has enough ram, but I think this method might be faster.
    # I'm not an expert on efficiency, though.
    annotations[line[0]] = line
  return header, annotations

def printAnnotation(ID, header, annotations) :
  print("For %s:" %ID)
  for i in range(len(header)) :
    print("\t%s: %s" %(header[i], annotations[ID][i]))

def testGetAnnotation() :
  fname = "../annotationFiles/affy_ATH1_array_elements-2010-12-20.txt"
  affyIDs = ["267631_at", "AFFX-LysX-M_at"]
  header, annotations = readAnnotations(fname)
  for ID in affyIDs :
    printAnnotation(ID, header, annotations)

if __name__ == "__main__" :
  testGetAnnotation()
