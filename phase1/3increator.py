nodes = 48
group = 0
changed = 1
for y in range(nodes):
	for x in range(nodes):
		if changed == 4:
			if((((group + 1) * 4) - 1) <= x <= (((group + 1) * 4) + 1)):
				print '0',
			else:
				print '100',
		elif (group * 4) <= x <= (((group + 1) * 4) - 1):
			print '0',
		elif changed == 3 and x == ((group + 1) * 4):
			print '0',
		else: 
			print '100',
	
	if changed == 4:
		changed = 1
		group += 1
	else:
		changed += 1

	print "\n"