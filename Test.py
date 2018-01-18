#Test
from everything import *
	

wheel = Wheel()
table = Table(3000)
gosho = Player(table, 3500, [Bet(100, 37),Bet(100, 7), Bet(50,36), Bet(100, 2), Bet(150, 13)])

game = Game(wheel, table)

game.cycle(gosho)
