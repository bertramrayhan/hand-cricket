from random import randint
from random import choice

def intro():
  print('Welcome to hand cricket!')
  print('The first one that reach 40 points will win the game')
  print('You will battle against computer')
  print()

def bat_or_bowl():
  global player_status
  coin_toss = choice(['heads','tails'])
  
  while True:
    coin = input('Choose heads or tails: ').lower()
    print()
    if coin not in ['heads', 'tails']:
      print('This is not the choice.')
    else:
      break

  print(f'Coin toss was {coin_toss}')
  if coin == coin_toss:
    print('You won the toss!')
    while True:
      print()
      player_status = input('Choose bat or bowl: ').lower()
      if player_status not in ['bat', 'bowl']:
        print('This is not the choice')
      else: 
        break
  else: 
    player_status = choice(["bat","bowl"])
    print('You loss the toss :(')
    print(f'You will {player_status} first')

def check_input():
  while True:
      try:
          user_input = int(input('Choose number from 1-6: '))
          if user_input not in range(1, 7):  # range(1, 7) includes 1 to 6
              print('Please choose a number from 1-6')
              print()
          else:
              return user_input
      except ValueError:
          print('Invalid input. Please enter a number from 1-6.')
          print()

def leaderboard():
  print()
  print(f"Player's score: {player_score}           computer's score: {computer_score}")
  print()
  print(f'You pick {player_status}')

player_status = None
player_score = 0
computer_score = 0
#ditaruh diluar function karena ada dua function yang ingin mengubah variabel ini

def main():
  global player_status, player_score, computer_score

  
  intro()

  bat_or_bowl()

  print()
  print('The battle will begin!')
  while True:
    leaderboard()
  
    #pick number
    pick_number_player = check_input()
    pick_number_computer = randint(1,6)
    


    if pick_number_player == pick_number_computer:
      print(f'Computer picks {pick_number_computer}')
      print('You pick the number as computer')
      if player_status == 'bat':
        player_status = 'bowl'
        continue
      else:
        player_status = 'bat'
        continue
    else:
      if player_status == 'bat':
        player_score += pick_number_player
      else:
        computer_score += pick_number_computer
      
    #check win
    if player_score >= 40:
      print()
      print('You win!!')
      break
    elif computer_score >= 40:
      print()
      print('Computer win :(')
      break

    print(f'Computer picks {pick_number_computer}')


if __name__ == '__main__':
  main()