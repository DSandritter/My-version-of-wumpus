alive = True

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
  10: [1, 6, 9, 11],
  11: []

}
#maps allow to have nonconsecutive numbers

def niceExitList(roomExits):
  global alive
  numExits = len(roomExits)
  if numExits == 0:
    alive = False
    return "You are trapped! this room has no exits and you have starved"
  if numExits == 1:
    return f"This room's only exit is to room {roomExits[0]}"
  if numExits == 2:
      return f"this room has exits to rooms {roomExits[0] and roomExits[1]}"
  niceList = "This room has exits to rooms:"
  for exitNum in range(numExits-1):
    niceList += f"{roomExits[exitNum]},"
  niceList += f"an {roomExits[-1]}."
  return niceList

def look():
  print(f"\nyou are in room {currentRoom}")
  print(niceExitList(caveMap[currentRoom]))

  
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



while alive:
  look()
  nextAction = input("\nWhat's next? ")
  if nextAction.lower()[0] == "m":
    move()
    continue
  if nextAction.lower()[0] == "q":
    break



  print(f"I'm sorry, I don't know how to quit {nextAction}.")
  print("I know how to quit.")