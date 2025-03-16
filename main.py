import pygame

WIDTH,HEIGHT = 300, 300

class Game:
  def __init__(self):
    pygame.init()
    
    self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("TIC TAC TOE")
    
    self.running = True
    
    self.cell_size = WIDTH / 3
    self.grid = self.create_game()
    
    self.mx,self.my = 0,0
    self.selected_square = None
    
    self.player_1_turn = True
    self.round = 0

  def create_game(self):
    grid = []
    for row in range(3):
      grid.append([])
      for col in range(3):
        grid[row].append( { 
                              "rect" : pygame.Rect(row * self.cell_size, col * self.cell_size, self.cell_size,self.cell_size),
                              "play" : "",
                              "color" : (255,255,255),
                              "pos" : [row * self.cell_size, col * self.cell_size] # top left pos
                              }  )    

    return grid
  
  def draw_game(self):
    for row in range(len(self.grid)):
      for col in range(len(self.grid[row])):
        
        if self.is_in_square(self.grid[row][col]["pos"]):
          color = (200,0,0)
          self.selected_square = self.grid[row][col]
        else: 
          color = self.grid[row][col]["color"]
          
        pygame.draw.rect(self.screen, color, self.grid[row][col]["rect"], 2)
        
        if self.grid[row][col]["play"] == "x":
          self.draw_x(self.grid[row][col])
          
        if self.grid[row][col]["play"] == "o":
          pygame.draw.circle(self.screen, (0,0,200), [self.grid[row][col]["pos"][0] + self.cell_size / 2, self.grid[row][col]["pos"][1] + self.cell_size / 2], self.cell_size //2 , 5)
      
  # Utils
  def check_win(self):
    self.check_row_col(True)
    self.check_row_col(False)
    self.check_diagonal()
    
  def check_diagonal(self):
    diagonal_1 = [self.grid[0][0]["play"], self.grid[1][1]["play"], self.grid[2][2]["play"]]
    diagonal_2 = [self.grid[2][0]["play"], self.grid[1][1]["play"], self.grid[0][2]["play"]]
    
    diagonal_1 = list(set(diagonal_1))
    diagonal_2 = list(set(diagonal_2))
      
    if len(diagonal_1) == 1 or len(diagonal_2) == 1:
      if diagonal_1[0] == "x" or diagonal_2[0] == "x" :
        print("player1 wins")
      elif diagonal_1[0] == "o" or diagonal_2[0] == "o" :
        print("player2 wins")
              
  # player wining condigtion col or row
  def check_row_col(self, is_checking_row):
    temp = ["", "", ""]
    for row in range(len(self.grid)):
      temp = ["", "", ""]
      for col in range(len(self.grid[row])):
        if is_checking_row:
          temp[col] = self.grid[col][row]["play"]
        else:
          temp[col] = self.grid[row][col]["play"]
          
      temp = list(set(temp))      
      if len(temp) == 1:
        if temp[0] == "x":
          print("player1 wins")
        elif temp[0] == "o":
          print("player2 wins")
    
  # Checks if mouse is hovering square
  def is_in_square(self, pos):
    # pos (x, y) = top left corner     # pos (x + cell_size, y) = top right corner # pos (x, y + cell_size) = bottom left corner   # pos (x + cell_size, y + cell_size) = bottom right corner
    if pos[0] < self.mx < (pos[0] + self.cell_size):
      if pos[1] < self.my < (pos[1] + self.cell_size):
        return True
  
  # Draws tne x shape
  def draw_x(self,square):
    pygame.draw.line(self.screen, (0,200,0),  square["pos"], [square["pos"][0] + self.cell_size, square["pos"][1] + self.cell_size] , 5)  
    pygame.draw.line(self.screen, (0,200,0),  [square["pos"][0], square["pos"][1] + self.cell_size], [square["pos"][0] + self.cell_size, square["pos"][1]] , 5)
  
  def run(self):
    while self.running:
      self.screen.fill((0,0,0)) # Fill the screen with black
      # Get mouse pos
      self.mx, self.my = pygame.mouse.get_pos()

      self.draw_game()
      
      
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          self.running = False
          
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_f:
            
            if self.player_1_turn and self.selected_square["play"] == "":
              self.selected_square["play"] = "x"
              self.player_1_turn = not self.player_1_turn
              self.round += 1
              
              
            if not self.player_1_turn and self.selected_square["play"] == "":
              self.selected_square["play"] = "o"
              self.player_1_turn = not self.player_1_turn
              self.round += 1
              
                


            self.check_win()
      
      pygame.display.update()

if __name__ == "__main__":
  Game().run()