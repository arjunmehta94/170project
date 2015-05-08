import sys

fin = open("answer2.out", "r")
T = 495
for t in xrange(1, T+1):
	d = fin.readline().split()
	for i in range(len(d)):
		d[i] = int(d[i]) + 1
	assign = str(d).split(', ')
	assign[0] = assign[0][1:]
	assign[-1] = assign[-1][0:1]
	fout = open("answer3.out", "a")
	fout.write("%s\n" % " ".join(map(str, assign)))

fin.close()
fout.close()