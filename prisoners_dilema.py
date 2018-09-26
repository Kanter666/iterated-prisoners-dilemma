import random


class Player():
	"""Player class - models memory, randomness in answer and can take a decision
	function as an input - default is always confess (return True)."""
	memory = []
	memory_s = 0
	prob = 1
	reward = 0
	cost = [0, -1, -8, -12]
	decision = lambda self: True
	name = "true"

	def __init__(self, memory_size, probability=1, decision= lambda self : True, cost = [0, -1, -8, -12]):
		self.memory_s = memory_size
		self.prob = probability
		self.decision = decision
		self.name = decision.__name__
		self.cost = cost

	def confess(self):
		if self.prob < random.uniform(0, 1):
			return not self.decision(self)
		else:
			return self.decision(self)

	def add_memory(self, me, you):
		if me:
			if you:
				self.reward += self.cost[2]
			else:
				self.reward += self.cost[0]
		else:
			if you:
				self.reward += self.cost[3]
			else:
				self.reward += self.cost[1]

		if len(self.memory)==self.memory_s:
			self.memory.pop()
		self.memory.append((me, you))

	def get_reward(self):
		return self.reward

	def null_reward(self):
		self.reward = 0
		self.memory = []

	def get_decision_type(self):
		return self.name

"""Functions that decide players strategy"""
def rand(self):
	return bool(random.getrandbits(1))

def tic_for_toe(self):
	if len(self.memory)>0:
		return self.memory[-1][1]
	else:
		return False

def worry_cat(self):
	if len(self.memory)>0:
		if not self.memory[-1][0] and not self.memory[-1][1]:
			return False
		else:
			for s in range(0, min(3, len(self.memory))):
				if self.memory[-1-s][0] and not self.memory[-1-s][1]:
					return False
		if self.memory[-1][1]:
			return True
		else:
			return False
	else:
		return True

"""Function that plays n iterations of games with 2 players"""
def game(p1, p2, n=1):
	for g in range(games):
		a1 = p1.confess()
		a2 = p2.confess()
		p1.add_memory(a1, a2)
		p2.add_memory(a2, a1)
		# print("Game {}, actions p1: {} p2: {}".format(g, a1, a2))
	return (p1.get_reward(), p2.get_reward())

"""Game code - runs iteration of games for all players and then writes results"""
games = 10 000
probability = 1
memory = 3

p1 = Player(memory, probability=probability, decision=rand)
p2 = Player(memory, probability=probability, decision=tic_for_toe)
p3 = Player(memory, probability=probability, decision=worry_cat)

players = [p1, p2, p3]
for i in range(0, len(players)-1):
	for j in range(i+1, len(players)):
		print("Player1 {}, Player2 {}".format(players[i].get_decision_type(), players[j].get_decision_type()))
		r1, r2 = game(players[i], players[j], n=games)
		print("Awerage reward p1: {} p2: {}".format(r1/games, r2/games))
		players[i].null_reward()
		players[j].null_reward()
