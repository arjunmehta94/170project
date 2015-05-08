import sys

# assumes output file is well formatted
# if you have errors, make sure you double check the output format 

ninstances = 495
def main(argv):
  fanswer = open("answer.out", "r")
  fout = open("score.txt", "w")
  for i in xrange(ninstances):
    print i
    finstance = open(`i+1`+".in", "r")
    N = int(finstance.readline())
    d = [[] for j in range(N)]
    for j in xrange(N):
        d[j] = [int(x) for x in finstance.readline().split()]
    c = finstance.readline().strip()
    finstance.close()

    perm = [int(x) for x in fanswer.readline().split()]
    fout.write(processCase(N, d, c, perm) + "\n")

  fout.close()
  fanswer.close()


def processCase(N, d, c, perm):
  if len(perm) != N:
    print "Number not correct"
    return "-1"
  v = [0] * N
  prev = 'X'
  count = 0
  for i in xrange(N):
    if perm[i] < 1 or perm[i] > N:
      print "Index not correct"
      return "-1"
    if v[perm[i]-1] == 1: 
      print "don't know"
      return "-1"
    v[perm[i]-1] = 1

    cur = c[perm[i]-1]
    if cur == prev:
      count += 1
    else:
      prev = cur
      count = 1

    if count > 3:
      print "color not correct"
      return "-1"

  cost = 0
  for i in xrange(N-1):
    cur = perm[i]-1
    next = perm[i+1]-1

    cost += d[cur][next]

  return str(cost)

if __name__ == '__main__':
    main(sys.argv[1:])