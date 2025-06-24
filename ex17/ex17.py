
from sys import argv
from os.path import exists

script,from_file,to_file = argv

print("Copying from %s to %s"%(from_file,to_file))

fromFileData = open(from_file)
dataInFile = fromFileData.read()

print("the file data is %d bytes long" %len(dataInFile))
print("does the output file exist? %r" %exists(to_file))
print("ready hit RETURN to continue, if you want to cancel Ctrl-C")
input("?")

outfile = open(to_file,"w")
outfile.write(dataInFile)

print("Copying all done")

outfile.close()
fromFileData.close()

print("do you want to read the copy contents Return to agree Ctr-C to disagree")
input("?")
toFile = open(to_file)
print(toFile.read())


