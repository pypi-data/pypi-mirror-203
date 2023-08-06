def dashByLength(thelist):
	"""Returns Dashes Based On The Length Of The List"""
	mln = []
	dashes = []
	for hh in thelist:
		mln.append(len(str(hh)))
	for nope in range(mln[-1]):
	 	dashes.append('-')
	return ''.join(dashes)