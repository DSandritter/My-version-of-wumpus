currentRoom = 1
caveMap = {
  1: [2, 7, 10],
  2: [1, 3, 5, 8],
  3: [2, 4, 7],
  4: [3, 5, 9],
  5: [2, 4, 6],
  6: [5, 7, 10],
  7: [1, 3, 6, 8],
  8: [2, 7, 9],
  9: [4, 8, 10],
  10: [1, 6, 9]

}
#maps allow to have nonconsecutive numbers

def look():
  print(f"\nyou are in room {currentRoom}")
  if len(caveMap[currentRoom]) == 0:
    print ("You are trapped! This room has no exits.")
  print(f"Exits lead to room: {caveMap[currentRoom]}")

  
def move():
  global currentRoom
  nextRoom = int(input("Where will you like to go? "))
  if nextRoom not in caveMap[currentRoom]: 
    print(f"I'm sorry you can not get into room {nextRoom} from here.")
    return
  if nextRoom not in caveMap:
      print(f"oh no! Room {nextRoom} doesn't exist")
      return
  currentRoom  = nextRoom



print("Hunt the Wumpus")
print()



while True:
  look()
  nextAction = input("\nWhat's next? ")
  if nextAction.lower()[0] == "m":
    move()
    continue
  if nextAction.lower()[0] == "q":
    break



  print(f"I'm sorry, I don't know how to quit {nextAction}.")
  print("I know how to quit.")