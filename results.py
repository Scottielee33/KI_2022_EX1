import matplotlib.pyplot as plt

# seed 1 t/m 5
board = ["6x6", "7x7", "8x8", "9x9", "10x10"]
wins = [[95, 94, 93, 94, 95], [96, 94]]
time = [[23, 25, 25, 23, 22], [83, 102]]
  
plt.plot(board, wins, color = 'g', label = 'File Data')
  
plt.xlabel('Size board', fontsize = 12)
plt.ylabel('Average amount of wins', fontsize = 12)
  
plt.title('Wins on each size board', fontsize = 20)
plt.legend()
plt.show()