import matplotlib.pyplot as plt

# seed 1 t/m 5
board = ["6x6", "7x7", "8x8"]
wins_mc = [[100, 100, 100, 100, 100], [100, 100, 99, 100, 100], [81, 78, 76, 81, 80]]
time_mc = [[21, 19, 21, 21, 19], [84, 76, 91, 76, 88], [349, 346, 325, 333, 314]]

wins_smart = [[100, 100, 100, 100, 100], [98, 100, 98, 98, 100], [97, 94, 94, 95, 95]]
wins_rook = [[93, 97, 93, 93, 91], [96, 91, 96, 88, 91], [90, 90, 94, 89, 92]]
time_smart = [[0.033, 0.026, 0.029, 0.028, 0.028], [0.058, 0.061, 0.058, 0.06, 0.054], [0.095, 0.099, 0.112, 0.114, 0.11]]

def average_list(lst):
    return sum(lst) / len(lst)

def average_graph(lst):
    temp_lst = []
    for i in lst:
        temp_lst.append(average_list(i))
    return temp_lst
  
def wins_graph():
    plt.plot(board, average_graph(wins_mc), color = 'g', label = 'Monte Carlo')
    plt.plot(board, average_graph(wins_smart), color= 'b', label = 'Clever Move')
    
    plt.xlabel('Size board', fontsize = 12)
    plt.ylabel('Average amount of wins', fontsize = 12)
    
    plt.title('Average amount of wins on each size board', fontsize = 20)
    plt.legend()
    plt.show()

def time_graph():
    plt.plot(board, average_graph(time_mc), color = 'g', label = 'Monte Carlo')
    plt.plot(board, average_graph(time_smart), color= 'b', label = 'Clever Move')
    
    plt.xlabel('Size board', fontsize = 12)
    plt.ylabel('Average amount of time', fontsize = 12)
    
    plt.title('Average amount of time to calculate move on each size board', fontsize = 20)
    plt.legend()
    plt.show()

def queen_vs_rook():
    plt.plot(board, average_graph(wins_smart), color = 'g', label = 'Queen')
    plt.plot(board, average_graph(wins_rook), color= 'b', label = 'Rook')
    
    plt.xlabel('Size board', fontsize = 12)
    plt.ylabel('Wins', fontsize = 12)
    
    plt.title('Average amount of wins on each size board', fontsize = 20)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    queen_vs_rook()