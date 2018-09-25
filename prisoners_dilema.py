import random

class player():
	memory = []
	memory_s = 0
	prob = 1
	reward = 0
	cost = [0, -1, -8, -12]

	def __init__(self, memory_size, probability=1):
		self.memory_s = memory_size
		self.prob = probability

	def confess(self):
		if self.prob < random.uniform(0, 1):
			return not self.decision()
		else:
		 return self.decision()

	def decision(self):
		return True

	def addMemory(self, me, you):
		if me:
			if you:
				reward += -8
			else:
				reward += 0
		if len(self.memory)==self.memory_s:
			self.memory.pop()
		self.memory.append((me, you))




p1 = player(2, 0.5)

for i in range(20):
	print(p1.confess())