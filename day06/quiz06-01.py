import sys
input_quiz = sys.argv[1]
output_quiz=sys.argv[2]

filereader=open(input_quiz,'r',newline='')
filewriter=open(output_quiz,'w',newline='')

header = filereader.readline()
print(header)

filereader.close()
filewriter.close()