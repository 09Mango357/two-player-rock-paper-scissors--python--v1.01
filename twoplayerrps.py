a = input("player one input: ")
print("\n" * 50)

b = input("player two input: ")
if a == "rock" and b == "scissors":
  print("Player 1 wins")
if a == "scissors" and b == "paper":
  print("Player 1 wins")
if a == "paper" and b == "rock":
  print("Player 1 wins")
  
if a == "rock" and b == "paper":
  print("Player 2 wins")
if a == "scissors" and b == "rock":
  print("Player 2 wins")
if a == "paper" and b == "scissors":
  print("Player 2 wins")