import random as rd

def get_seq(input_file):
	coordinates = []
	with open(input_file, "r") as filin:
		for n, line in enumerate(filin):
			if n == 0:
				seq = line.strip()
			else:
				line = line.strip()
				line = line[1:-1].split(",")
				line = list(map(int, line))
				coordinates.append(line)
	return [seq, coordinates]
			


class Residue:
	def __init__(self, name, polarity, coordinates):
		self.name = name
		self.polarity = polarity
		self.coordinates = coordinates
	
	def end_move(self, neighbour, protein_coordinates):
		available_mvt = []
		right = [neighbour.coordinates[0] + 1, neighbour.coordinates[1]]
		left = [neighbour.coordinates[0] - 1, neighbour.coordinates[1]]
		bottom = [neighbour.coordinates[0], neighbour.coordinates[1] - 1]
		top = [neighbour.coordinates[0], neighbour.coordinates[1] + 1]	
		if tuple(right) not in protein_coordinates:
			available_mvt.append(right)
		if tuple(left) not in protein_coordinates:
			available_mvt.append(left)
		if tuple(bottom) not in protein_coordinates:
			available_mvt.append(bottom)
		if tuple(top) not in protein_coordinates:
			available_mvt.append(top)
		mvt = rd.choice(available_mvt)
		protein_coordinates.remove(tuple(self.coordinates))
		self.coordinates = mvt
		protein_coordinates.add(tuple(self.coordinates))
	
	def corner_move(self, neighbour1, neighbour2, protein_coordinates):
		# Right bottom movement. 
		if neighbour1.coordinates[0] > self.coordinates[0] and neighbour2.coordinates[1] < self.coordinates[1]:
			if tuple([neighbour1.coordinates[0], neighbour2.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour1.coordinates[0], neighbour2.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
			else:
				print("redo step")
		elif neighbour2.coordinates[0] > self.coordinates[0] and neighbour1.coordinates[1] < self.coordinates[1]:
			if tuple([neighbour2.coordinates[0], neighbour1.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour2.coordinates[0], neighbour1.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
			else:
				print("redo step")
		# Left top movement.
		elif neighbour1.coordinates[0] < self.coordinates[0] and neighbour2.coordinates[1] > self.coordinates[1]:
			if tuple([neighbour1.coordinates[0], neighbour2.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour1.coordinates[0], neighbour2.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
			else:
				print("redo step")
		elif neighbour2.coordinates[0] < self.coordinates[0] and neighbour1.coordinates[1] > self.coordinates[1]:
			if tuple([neighbour2.coordinates[0], neighbour1.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour2.coordinates[0], neighbour1.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
			else:
				print("redo step")
		# Right top movement.
		elif neighbour1.coordinates[0] > self.coordinates[0] and neighbour2.coordinates[1] > self.coordinates[1]:
			if tuple([neighbour1.coordinates[0], neighbour2.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour2.coordinates[0], neighbour1.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
			else:
				print("redo step")
		elif neighbour2.coordinates[0] > self.coordinates[0] and neighbour1.coordinates[1] > self.coordinates[1]:
			if tuple([neighbour2.coordinates[0], neighbour1.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour2.coordinates[0], neighbour1.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
			else:
				print("redo step")
		# Left bottom movement
		elif neighbour1.coordinates[0] < self.coordinates[0] and neighbour2.coordinates[1] < self.coordinates[1]:
			if tuple([neighbour1.coordinates[0], neighbour2.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour1.coordinates[0], neighbour2.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
			else:
				print("redo step")
		elif neighbour2.coordinates[0] < self.coordinates[0] and neighbour1.coordinates[1] < self.coordinates[1]:
			if tuple([neighbour2.coordinates[0], neighbour1.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour2.coordinates[0], neighbour1.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
			else:
				print("redo step")
		else:
			print("redo step")
			
		
			
if __name__ == "__main__":
	
	seq, coordinates = get_seq("../data/HP2.txt")
	
	# creating list        
	protein = []
  
	# appending instances to list
	for n, res in enumerate(seq):
		protein.append(Residue("residue" + str((n+1)), res, coordinates[n]))
	
	# Creating set for all coordinates
	protein_coordinates = set()
	for res in protein:
		protein_coordinates.add(tuple(res.coordinates))

	"""
	print(protein[2].coordinates)
	print("\n")
	print(protein_coordinates)
	
	protein[-1].end_move(protein[-2], protein_coordinates)
	print("\n")
	print(protein[-1].coordinates)
	print("\n")
	print(protein_coordinates)
	
	
	protein[2].corner_move(protein[1], protein[3], protein_coordinates)
	print("\n")
	print(protein[2].coordinates)
	print("\n")
	print(protein_coordinates)
	"""
	
	
	
	
	
	
	
	
