import os

def c4box(a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6, c1, c2, c3, c4, c5, c6, d1, d2, d3, d4, d5, d6, e1, e2, e3, e4, e5, e6, f1, f2, f3, f4, f5, f6, g1, g2, g3, g4, g5, g6, ra, rb, rc, rd, re, rf, rg):
  return f"""
  ___________________________
 | {a6} | {b6} | {c6} | {d6} | {e6} | {f6} | {g6} |
 | {a5} | {b5} | {c5} | {d5} | {e5} | {f5} | {g5} |
 | {a4} | {b4} | {c4} | {d4} | {e4} | {f4} | {g4} |
 | {a3} | {b3} | {c3} | {d3} | {e3} | {f3} | {g3} |
 | {a2} | {b2} | {c2} | {d2} | {e2} | {f2} | {g2} |
 | {a1} | {b1} | {c1} | {d1} | {e1} | {f1} | {g1} |
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
   {ra}   {rb}   {rc}   {rd}   {re}   {rf}   {rg}"""

turn = "o"
print("Enter < or >, a or d to switch between columns.")
while True:
  locs = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
  stacks = [0, 0, 0, 0, 0, 0, 0]
  pl = 0
  end = False
  checkv = ["^", " ", " ", " ", " ", " ", " "]
  print(c4box(locs[0], locs[1], locs[2], locs[3], locs[4], locs[5], locs[6], locs[7], locs[8], locs[9], locs[10], locs[11], locs[12], locs[13], locs[14], locs[15], locs[16], locs[17], locs[18], locs[19], locs[20], locs[21], locs[22], locs[23], locs[24], locs[25], locs[26], locs[27], locs[28], locs[29], locs[30], locs[31], locs[32], locs[33], locs[34], locs[35], locs[36], locs[37], locs[38], locs[39], locs[40], locs[41], checkv[0], checkv[1], checkv[2], checkv[3], checkv[4], checkv[5], checkv[6]))
  while True:
    if turn == "o":
      print("Enter o to place your o")
    else:
      print("Enter x to place your x")
    while True:
      inp = str(input())
      if inp == "<" or inp == "a":
        if pl == 0:
          print("You cannot go left any further.")
        else:
          checkv[pl] = " "
          pl -= 1
          checkv[pl] = "^"
          break
      elif inp == ">" or inp == "d":
        if pl == 6:
          print("You cannot go right any further.")
        else:
          checkv[pl] = " "
          pl += 1
          checkv[pl] = "^"
          break
      elif inp == "o" or inp == "x":
        if stacks[pl] >= 6:
          print("You cannot place any more in this column")
        elif turn == "o":
          if inp == "x":
            print("It is not x's turn yet!")
          else:
            locs[pl * 6 + stacks[pl]] = "o"
            turn = "x"
            stacks[pl] += 1
            break
        elif turn == "x":
          if inp == "o":
            print("It is not o's turn yet!")
          else:
            locs[pl * 6 + stacks[pl]] = "x"
            turn = "o"
            stacks[pl] += 1
            break
    os.system("clear")
    print(c4box(locs[0], locs[1], locs[2], locs[3], locs[4], locs[5], locs[6], locs[7], locs[8], locs[9], locs[10], locs[11], locs[12], locs[13], locs[14], locs[15], locs[16], locs[17], locs[18], locs[19], locs[20], locs[21], locs[22], locs[23], locs[24], locs[25], locs[26], locs[27], locs[28], locs[29], locs[30], locs[31], locs[32], locs[33], locs[34], locs[35], locs[36], locs[37], locs[38], locs[39], locs[40], locs[41], checkv[0], checkv[1], checkv[2], checkv[3], checkv[4], checkv[5], checkv[6]))
    for i in range(len(locs)):
      if locs[i] == "x":
        if i < 3 or i > 5 and i < 9 or i > 11 and i < 15 or i > 17 and i < 21 or i > 23 and i < 27 or i > 29 and i < 33 or i > 35 and i < 39:
          if locs[i+1] == "x" and locs[i+2] == "x" and locs[i+3] == "x":
            print("X wins!")
            end = True
            break
        if i < 21:
          if locs[i+6] == "x" and locs[i+12] == "x" and locs[i+18] == "x":
            print("X wins!")
            end = True
            break
        if i < 3 or i > 5 and i < 9 or i > 11 and i < 15 or i > 17 and i < 21:
          if locs[i+7] == "x" and locs[i+14] == "x" and locs[i+21] == "x":
            print("X wins!")
            end = True
            break
        if i > 2 and i < 6 or i > 8 and i < 12 or i > 14 and i < 18 or i > 20 and i < 24:
          if locs[i+5] == "x" and locs[i+10] == "x" and locs[i+15] == "x":
            print("X wins!")
            end = True
            break
      elif locs[i] == "o":
        if i < 3 or i > 5 and i < 9 or i > 11 and i < 15 or i > 17 and i < 21 or i > 23 and i < 27 or i > 29 and i < 33 or i > 35 and i < 39:
          if locs[i+1] == "o" and locs[i+2] == "o" and locs[i+3] == "o":
            print("O wins!")
            end = True
            break
        if i < 21:
          if locs[i+6] == "o" and locs[i+12] == "o" and locs[i+18] == "o":
            print("O wins!")
            end = True
            break
        if i < 3 or i > 5 and i < 9 or i > 11 and i < 15 or i > 17 and i < 21:
          if locs[i+7] == "o" and locs[i+14] == "o" and locs[i+21] == "o":
            print("O wins!")
            end = True
            break
        if i > 2 and i < 6 or i > 8 and i < 12 or i > 14 and i < 18 or i > 20 and i < 24:
          if locs[i+5] == "o" and locs[i+10] == "o" and locs[i+15] == "o":
            print("O wins!")
            end = True
            break
    if " " not in locs:
      print("It's a tie!")
      end = True
    if end == True:
      while True:
        end = str(input("Would you like to play again?(y/n): "))
        if end == "y" or end == "Y":
          while True:
            print("Choose which side begins first: x/o")
            turn = str(input())
            if turn == "x" or turn == "X":
              turn = "x"
              break
            elif turn == "o" or turn == "O":
              turn = "o"
              break
          break
        elif end == "n" or end == "N":
          print("Thanks for playing!")
          quit()
      if end == "y" or end == "Y":
        break
