class Map:
	def __init__(self,size = None):
		self.size = size # (no of rows, no of cols)
		self.population = 0
	def from_ascii(self,asciimap):
		lines = asciimap.strip(" \n").split()
		self.size = (len(lines), len(lines[0]))
		x = 1
		for line in lines:
			for c in line:
				if c == "#":
					self.population |= x
				x <<= 1
				
		
	def add(self,pos):
		nr = 1<<(pos[0]*self.size[1]+pos[1])
		self.population |= nr
	@staticmethod
	def n_ones(x):
		n = 0
		while x != 0:
			n += x & 1
			x >>= 1
		return n
	def popsize(self):
		return self.n_ones(self.population)
	def number(self,pos):
		r,c = pos
		return 1 << (r*self.size[1]+c)
	def pos(self, n):
		x = n
		if x<= 0:
			raise ValueError()
		k = 0
		plist = []
		while x:
			if x&1:
				plist.append((k//self.size[1], k%self.size[1]))
			k += 1			
			x >>= 1
		return plist
		

	def mask(self,maskint):
		return self.population & maskint
	def neighbourmask(self,p):
		# p = (rownr, colnr) or number
		nrows,ncols = self.size
		if not isinstance(p,int):
			rownr,colnr = p
			pos = self.number(p)
		else:
			pos = p
			rownr,colnr = self.pos(p)[0]
		if rownr == 0:
			if colnr == 0:
				return (pos<<1) | (pos<<ncols)
			elif colnr == ncols-1:
				return (pos>>1) | (pos<<ncols)
			else:
				return (pos>>1) | (pos<<1) | (pos<<ncols)
		elif rownr == nrows-1:
			if colnr == 0:
				return (pos<<1) | (pos>>ncols)
			elif colnr == ncols-1:
				return (pos>>1) | (pos>>ncols)
			else:
				return (pos>>1) | (pos<<1) | (pos>>ncols)
		else:
			if colnr == 0:
				return (pos<<1) | (pos>>ncols) | (pos<<ncols)
			elif colnr == ncols-1:
				return (pos>>1) | (pos>>ncols) | (pos<<ncols)
			else:
				return (pos>>1) | (pos<<1) | (pos>>ncols) | (pos<<ncols)
	def __str__(self):
		str = ""
		x = self.population
		for k in range(self.size[0]):
			for m in range(self.size[1]):
				str += ("#" if (x&1) else ".")
				x >>= 1
			str += "\n"
		return str
	def neighbourprint(self):
		nrows,ncols = self.size
		s = ""
		for r in range(nrows):
			for c in range(ncols):
				center = self.number((r,c))
				mask = self.neighbourmask((r,c))
				n = self.n_ones(self.mask(mask))
				s += str(n)
			s += "\n"
		return s
		
	def update(self):
		verbose = False
		nrows,ncols = self.size
		newpop = 0
		if verbose: s = "" # for debugging
		for r in range(nrows):
			for c in range(ncols):
				center = self.number((r,c))
				mask = self.neighbourmask((r,c))
				n = self.n_ones(self.mask(mask))
				if verbose: s += str(n)
				if center & self.population: # if (r,c) is infested
					if n == 1:
						newpop |= center
				else: # if (r.c) is not infested
					if n in {1,2}:
						newpop |= center
			if verbose: s += "\n"
		if verbose: print(s)
		self.population = newpop

class RecursiveMap(Map):
	def __init__(self, originmap = Map(), center = None):
		self.maps = [originmap] # a list of maps
		self.origin = 0 # the index in maps for the origin of maps
		if center = None:
			self.center = (originmap.size[0]//2, originmap.size[0]//2)
		else 
			self.center = center
		# self.center: the position where an inner map sits in its outer map
	def add_inner_map(self, map):
		self.append(map)
	def add_outer_map(self, map):
		self.insert(0, map)
		self.origin += 1
	def update(self):
		pass
		# to be implemented...
	
def test():
	mymap = Map((4,5))
	print(mymap.population)
	print(str(mymap))	
	mymap.add((2,3))
	print(mymap.population)
	print(str(mymap))
	mymap.add((0,2))
	mymap.add((1,3))
	mymap.add((2,2))
	print(mymap.population)
	print(str(mymap))
	print(mymap.popsize())
	print(mymap.pos(mymap.population))
	mymap.update()

	print(str(mymap))
	print(mymap.popsize())
	print(mymap.pos(mymap.population))

def example():
	indata = "....# #..#. #..## ..#.. #...."
	mymap = Map()
	mymap.from_ascii(indata)
	#print(str(mymap), mymap.popsize(), mymap.population)
	divindexlist = []
	divindex = mymap.population
	k=0
	while divindex not in divindexlist:
		if k<2: print(mymap,mymap.neighbourprint())
		divindexlist.append(divindex)
		mymap.update()
		divindex = mymap.population
		k+=1
	print(mymap)
	print(divindex)

	
def part1():
	indata = "..#.# #.##. .#..# #.... ....#"
	mymap = Map()
	mymap.from_ascii(indata)
	#print(str(mymap), mymap.popsize(), mymap.population)
	divindexlist = []
	divindex = mymap.population
	while divindex not in divindexlist:
		print(mymap)
		divindexlist.append(divindex)
		mymap.update()
		divindex = mymap.population
	print(mymap)
	print(divindex)
		
#example()	
part1()
