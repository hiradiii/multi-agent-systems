import random

class VacuumCleanerAgent:
    def __init__(self):
        self.x = random.randint(0, 3)
        self.y = random.randint(0, 3)
        self.orientation = random.choice(['north', 'south', 'east', 'west'])
        self.moves = []
        self.cost = 0
    
    def sense(self, grid):
        return grid[self.x][self.y]
    
    def act(self, status):
        if status == 'dirty':
            self.moves.append('suck')
            self.cost += 2
            return 'suck'
        elif self.orientation == 'north':
            self.moves.append('forward')
            self.cost += 1
            self.x -= 1
            if self.x < 0:
                self.x = 0
                self.orientation = 'east'
            return 'forward'
        elif self.orientation == 'south':
            self.moves.append('forward')
            self.cost += 1
            self.x += 1
            if self.x > 3:
                self.x = 3
                self.orientation = 'west'
            return 'forward'
        elif self.orientation == 'east':
            self.moves.append('forward')
            self.cost += 1
            self.y += 1
            if self.y > 3:
                self.y = 3
                self.orientation = 'south'
            return 'forward'
        elif self.orientation == 'west':
            self.moves.append('forward')
            self.cost += 1
            self.y -= 1
            if self.y < 0:
                self.y = 0
                self.orientation = 'north'
            return 'forward'

def create_grid():
    grid = [['clean' for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if random.random() < 0.5:
                grid[i][j] = 'dirty'
    return grid

def play_game():
    grid = create_grid()
    agent1 = VacuumCleanerAgent()
    agent2 = VacuumCleanerAgent()
    while any('dirty' in row for row in grid):
        agent1_action = agent1.act(agent1.sense(grid))
        agent2_action = agent2.act(agent2.sense(grid))
        if agent1_action == 'suck':
            grid[agent1.x][agent1.y] = 'clean'
        if agent2_action == 'suck':
            grid[agent2.x][agent2.y] = 'clean'
    if agent1.cost == agent2.cost:
        if len(agent1.moves) <= len(agent2.moves):
            print("Agent 1 wins!")
        else:
            print("Agent 2 wins!")
    elif agent1.cost < agent2.cost:
        print("Agent 1 wins!")
    else:
        print("Agent 2 wins!")
    print("Agent 1 path:", agent1.moves)
    print("Agent 2 path:", agent2.moves)
    print("Agent 1 cost:", agent1.cost)
    print("Agent 2 cost:", agent2.cost)

play_game()
