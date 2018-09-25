import random


class Player():
	memory = []
	memory_s = 0
	prob = 1
	reward = 0
	cost = [0, -1, -8, -12]
	decision = lambda self: True

	def __init__(self, memory_size, probability=1, decision= lambda self : True):
		self.memory_s = memory_size
		self.prob = probability
		self.decision = decision

	def confess(self):
		if self.prob < random.uniform(0, 1):
			return not self.decision(self)
		else:
			return self.decision(self)

	def add_memory(self, me, you):
		if me:
			if you:
				self.reward += -8
			else:
				self.reward += 0
		else:
			if you:
				self.reward += -12
			else:
				self.reward += -1

		if len(self.memory)==self.memory_s:
			self.memory.pop()
		self.memory.append((me, you))

	def get_reward(self):
		return self.reward

def good(self):
	return False

def tic_for_toe(self):
	if len(self.memory)>0:
		return self.memory[-1][1]
	else:
		return False


p1 = Player(3, decision = good)
p2 = Player(3, decision = tic_for_toe)

for i in range(20):
	a1 = p1.confess()
	a2 = p2.confess()
	p1.add_memory(a1, a2)
	p2.add_memory(a2, a1)
	print("Game {}, actions p1: {} p2: {}".format(i, a1, a2))
print("Reward p1: {} p2: {}".format(p1.get_reward(), p2.get_reward()))
