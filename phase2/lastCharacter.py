import sys
fin = open("answer3.out", "r")
T = 495
for t in xrange(1, T+1):
	arrsum = 0
	d = fin.readline().split()
	for i in range(len(d)):
		d[i] = int(d[i])
	for i in xrange(1, len(d)):
		arrsum += d[i]
	for i in xrange(1, len(d)+1):
		if i not in d[:len(d)]:
			d[-1] = i
	assign = str(d).split(', ')
	assign[0] = assign[0][1:]
	if d[-1] < 10:
		assign[-1] = assign[-1][0:1]
	else:
		assign[-1] = assign[-1][0:2]
	fout = open("answer4.out", "a")
	fout.write("%s\n" % " ".join(map(str, assign)))
