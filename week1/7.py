birthdays = {'Alice':'Apr 1', 'Bob':'Dec 12', 'Carol':'Mar 14'}
while True:
    print('Enter a name : (blank to quit)')
    name= input('-->')
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday ?')
        bday = input('-->')
        birthdays[name] = bday
        print('Birthday database updated.')

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count={}
for character in message:
    count.setdefault(character, 0)
    count[character]= count[character] + 1
print(count)

# import sys, copy
# STARTING_PIECES={'a8':'bR', 'b8':'bN','c8':'bB','d8':'bQ','e8':'bK',
#                  'f8':'bB','g8':'bN', 'h8':'bR', 'a7':'bP', 'b7':'bP',
#                  'c7':'bP','d7':'bP', 'e7':'bP', 'f7':'bP','g7':'bP','h7':'bP',
#                  'a1':'wR', 'b1':'wN','c1':'wB','d1':'wQ','e1':'wK',
#                  'f1':'wB','g1':'wN', 'h1':'wR', 'a2':'wP', 'b2':'wP',
#                  'c2':'wP','d2':'wP', 'e2':'wP', 'f2':'wP','g2':'wP','h2':'wP'}

# BOARD_TEMPLATE = """
#     a    b    c    d    e    f    g    h
#    ____ ____ ____ ____ ____ ____ ____ ____
#   ||||||    ||||||    ||||||    ||||||    |
# 8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
#   ||||||____||||||____||||||____||||||____|
#   |    ||||||    ||||||    ||||||    ||||||
# 7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
#   |____||||||____||||||____||||||____||||||
#   ||||||    ||||||    ||||||    ||||||    |
# 6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
#   ||||||____||||||____||||||____||||||____|
#   |    ||||||    ||||||    ||||||    ||||||
# 5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
#   |____||||||____||||||____||||||____||||||
#   ||||||    ||||||    ||||||    ||||||    |
# 4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
#   ||||||____||||||____||||||____||||||____|
#   |    ||||||    ||||||    ||||||    ||||||
# 3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
#   |____||||||____||||||____||||||____||||||
#   ||||||    ||||||    ||||||    ||||||    |
# 2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
#   ||||||____||||||____||||||____||||||____|
#   |    ||||||    ||||||    ||||||    ||||||
# 1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
#   |____||||||____||||||____||||||____||||||
# """
# WHITE_SQUARE = '||'
# BLACK_SQUARE = '  '

# def print_chessboard(board):
#     squares = []
#     is_white_square=True
#     for y in '87654321':
#         for x in 'abcdefgh':
#             print(x,y, is_white_square)
#             if x+y in board.keys():
#                 squares.append(board[x+y])
#             else:
#                 if is_white_square:
#                     squares.append(WHITE_SQUARE)
#                 else:
#                     squares.append(BLACK_SQUARE)
#             is_white_square = not is_white_square
#         is_white_square = not is_white_square
#     print(BOARD_TEMPLATE.format(*squares))
# print('Interactive Chessboard')
# print('by Al sweigart al@inventwithpython.com')
# print()
# print('Pieces : ')
# print('  w - White, b - Black')
# print('  P - Pawn, N- Knight, B - Bishop, R - Rook, Q - Queen, K - King')
# print('Commands : ')
# print('  move e2 e4 - Movess the piece at e2 to e4')
# print('  remove e2 - Removes hte piece at e2')
# print('  set e2 wP - Sets square e2 to a white pawn')
# print('  reset - Resets pieces back to their starting squares')
# print('  clear - Clears the entire board')
# print('  fill wP - Fills the entire board with white pawns.')
# print('  quit - Quits the program')
# main_board = copy.copy(STARTING_PIECES)
# while True:
#     print_chessboard(main_board)
#     response = input('> ').split()
#     if response[0] == 'move':
#         main_board[response[2]] = main_board[response[1]]
#         del main_board[response[1]]
#     elif response[0] == 'remove':
#         del main_board[response[1]]
#     elif response[0] == 'set':
#         main_board[response[1]] = response[2]
#     elif response[0]=='reset':
#         main_board = copy.copy(STARTING_PIECES)
#     elif response[0]=='clear':
#         main_board= {}
#     elif response[0] == 'fill':
#         for y in '87654321':
#             for x in 'abcdefgh':
#                 main_board[x+y] = response[1]
#     elif response[0] == 'quit':
#         sys.exit()

all_guests = {'Alice': {'apples':5, 'pretzels':12},
              'Bob':{'ham sandwiches': 3, 'apples':2},
              'Carol':{'cups':3, 'apple pies':1}}
def total_brought(guests,item):
    num_brought = 0
    for k,v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought
print('Number of things being brought: ')
print(' - Apples            '+ str(total_brought(all_guests, 'apples')))
print(' - Cups              '+str(total_brought(all_guests,  'cups')))
print(' - Cakes             '+str(total_brought(all_guests,  'cakes')))
print(' - Ham Sandwiches    '+str(total_brought(all_guests,  'ham sandwiches')))
print(' - Apple Pies        '+str(total_brought(all_guests,  'apple pies')))
spam = {}

spam.setdefault('color', 'Black')
print(spam)