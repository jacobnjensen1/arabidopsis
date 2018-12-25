#! /usr/bin/env python


# Jacob: this is an example of good practice using commandline arguments, and making your script importable without side-effects.
# It also has an example of how to get a list of files available in the directory -- glob. With big data, you NEED this function.


# This is a super easy way to handle commandline arguments.
from argparse import ArgumentParser
# This is a super easy way to get a huge list of file names using unix syntax.
from glob import glob
# We want a safe way to join path names (not really necessary, just good practice.)
from os import path


def main(folder, level, flag) :
  print("You want to perform this level of analysis: %s" %level)
  if flag :
    print("You also set the flag!")
  # The command that I used is equivalent to saving the unix command "ls ${folder}/*" to a list.
  # You'll probably actually want to do something like this :
  #    files = [ f for f in glob("heatStress/*.txt") if "README" not in f ]
  # (After unzipping the files, of course.)
  files = glob(path.join(folder, "*"))
  print("I found %d files in that directory." %len(files))

# Check for __name__ because this only happens when this script is run directly (not when it's imported.)
# We run everything inside functions because we want all our python scripts to be importable without side-effects
# That means we can call this script with another script and get its functions without anything undesirable or unknown occurring.
if __name__ == '__main__' :
  # Make a parser object instance
  parser = ArgumentParser()
  # Add arguments
  parser.add_argument("folder", help="This is the directory you want to use. It can be an absolute or relative path.")
  parser.add_argument("level", choices=["basic", "special"], help="This is an example argument that you can give to your script from the command line.")
  parser.add_argument("f", action="store_true", default=False, help="This is an example boolean flag that you can give to your script from the command line.")
  # Parse arguments
  args = parser.parse_args()
  # Pass arguments into main
  main(args.folder, args.level, args.f)

