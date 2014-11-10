#!/usr/local/bin/python2.7
 
import random
 
#Info for the game
def displayInf():
  print "This is my Rock Paper Scissors game for the reddit Python begginer project."
  print "Warning: if you pick any thing other than the choices you will lose."
 
 
#gets the users choice and returns it
def getOpt():
  print "\n\n\nRock. Paper. Scissor...Shoot"
  get = raw_input("\n\nChoose: ")
 
  #checks if the input of the user was capitalized or not if not then it makes it capitalized
  if get[0].islower():
    get = get.capitalize()
     
  return get
 
 
 
#Randomly chooses the cpu's choice and returns it
def cpuMV(Opt):
  MV = random.choice(Opt)
  print "\nThe Cpu chose: " + MV
  return MV
 
 
 
#This is the algorithm for determining the winner of the game, it returns all of the data when done 
def detWin(comOpt, playerOpt, Opt, Pwin = False, Cwin = False, Tie = False):
 
  if comOpt == playerOpt:
    Tie = True
     
  elif comOpt == Opt[0] and playerOpt == Opt[1]:
    Pwin = True
     
  elif comOpt == Opt[1] and playerOpt == Opt[2]:
    Pwin = True
     
  elif comOpt == Opt[2] and playerOpt == Opt[0]:
    Pwin = True
  else:
    Cwin = True
     
  return [Pwin,Cwin,Tie]
 
 
 
#This function will check the results of previous function and print the winner and append to the score
def getRes(data, score, Victor =["\nYou have won!","\nYou lost...","\nDraw..."],num = 0):
 
  for obj in data:
    if obj is True:
       
      print(Victor[num])
       
      if obj == data[0] and obj is True:
        score[0] += 1
         
      elif obj == data[1] and obj is True:
        score[1] += 1
         
      else:
        score[2] += 1
         
    num += 1
  return score
 
 
 
#This is the score board it writes the score based on the data, and ask the user if they would like to continue
def printData(score, cont = False, pos = ["NO","no","No","n","N"]):
   
  print "\nWins: " + str(score[0]), "Loses: " + str(score[1]), "Draws: " + str(score[2])
 
  ans = raw_input("\nWould you like to continue: ")
 
  if ans not in pos:
    cont = True
 
  return cont
 
 
 
#The game loop
def main(Optlist = ["Rock","Paper","Scissor"], score = [0,0,0]):
   
  done = False
  displayInf()
   
  while not done:
     
    playerOpt = getOpt()
    comOpt = cpuMV(Optlist)
    out = detWin(comOpt,playerOpt,Optlist)
    score = getRes(out,score)
    cont = printData(score)
     
    if cont is False:
      done = True
 
       
     
if __name__ in "__main__":
  main()