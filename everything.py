from random import *

class Outcome(object):
	def __init__(self, name, odds):
		self.name = name
		self.odds = odds

	def winAmount(self, amount):
		return self.odds * amount

	def __eq__(self, other):
		return self.name == other.name

	def __ne__(self, other):
		return self.name != other.name

	def __str__(self):
		return "%s (%s:1)" % (self.name, self.odds)

	def __repr__(self):
		return "%s (%s:1)" % (self.name, self.odds)


class Bin(object):
	def __init__(self, *outcomes):
		self.outcomes = list(set([outcome for outcome in outcomes]))

	def add(self, outcome):
		return self.outcomes.append(outcome)

	def __str__(self):
		return ', '.join(list([str(outcome) for outcome in self.outcomes]))

	def __repr__(self):
		return self.outcomes

	def __iter__(self):
		return iter(self.outcomes[:])
	

class Wheel(object):
	def __init__(self):
		self.bins = tuple(Bin() for i in range(38))
		self.outcomes = {}

	def addOutcome(self, number, outcome):
		self.bins[number].add(outcome)
		name = str(outcome).split(' (')[0]
		self.outcomes.update({name: outcome})

	def random_number(self):
		i = choice(range(38))
		return self.bins[i]

	def get(self, number):
		return self.bins[number]


class BinBuilder(object):
	def __init__(self, wheel):
		self.wheel = wheel

	def bets(self):
		self.straightBets()

	def straightBets(self):
		outcomes = [Outcome((i), 35) for i in range(37)] + [Outcome('00', 35)]
		for i, outcome in enumerate(outcomes):
			self.wheel.addOutcome(i,outcome)


class Bet():
	def __init__(self, amount, outcome):
		self.amount = amount
		self.outcome = outcome

	def winAmount(self):
		return self.outcome.winAmount(self.amount)

	def loseAmount(self):
		return self.amount

	def __str__(self):
		return "Amount: %s on %s" % (self.amount, self.outcome)


class Table(object):
	def __init__(self, limit):
		self.limit = limit
		self.bets = []

	def isValid(self, bet):
		if sum([bet.amount] + [bet1.amount for bet1 in self.bets]) > self.limit:
			print 'That bet exceeds the table limit!!', bet
			return False
		else:
			return True

	def placeBets(self, bet):
		if self.isValid(bet):
			self.bets.append(bet)
		else:
			return "InvalidBet"

	def __iter__(self):
		return iter(self.bets[:])

	def __str__(self):
		return str(self.bets)


class Player:
    def __init__(self,table, money, bets = []):
        self.table = table
        self.money = money
        self.bets = bets

    def placeBets(self):
        for bet in self.bets:
        	self.money -= bet.amount
        	if self.money <= 0:
        		return "you cannot place this bet, you don't have enough money"
        	else:
        		print "Betting", bet
    			self.table.placeBets(bet)

    def win(self, bet):
    	self.money += bet
    	return self.money

    def lose(self, bet):
		pass

class Game(object):
	def __init__(self, wheel, table):
		self.wheel = wheel
		self.table = table

		BinBuilder(self.wheel).bets()

	def cycle(self, player):
		
		print 'The player has', player.money
		print "Placing bets > "
		player.placeBets()
		print "Bets places"
		print "Spin the wheel"
		number = self.wheel.random_number()
		print 'Wheel stopped on', number

	   	for bet in self.table:
	   		print "Checking", bet
	   		money_bet = bet.amount
	   		for i in number:
				if bet.outcome == i.name:
					bet = i 
					money_won = bet.winAmount(money_bet)
					print 'Congratulations! You won $%s' % (money_won)
					player.win(money_won)					
					return 
        		else:
           			print 'Sorry, your bet wasn\'t a winner. Better luck next time!'
           			print 
		





	