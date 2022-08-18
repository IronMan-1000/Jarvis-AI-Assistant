# Jarvis AI Assistant
import pyttsx3
import random
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import win10toast
import pygame
import webbrowser
import pyjokes

voiceType = input("Do you want a male voice or a female voice : ")
voiceTest = ""

if voiceType.lower() == 'male' : 
    comp = pyttsx3.init()
    voiceTest = "This is a male voice"
    comp.say(voiceTest)
    comp.runAndWait()

elif voiceType.lower() == 'female' : 
    comp = pyttsx3.init('sapi5')
    voices = comp.getProperty('voices')
    comp.setProperty('voice', voices[len(voices) - 1].id)
    voiceTest = "This is a female voice"
    comp.say(voiceTest)
    comp.runAndWait()

else : 
    run = True
    while run : 
        print("This is an invalid input.")
        
        voiceType = input("Do you want a male voice or a female voice : ")

        if voiceType.lower() == 'male' : 
            comp = pyttsx3.init()
            voiceTest = "This is a male voice"
            comp.say(voiceTest)
            comp.runAndWait()
            run = False

        elif voiceType.lower() == 'female' : 
            comp = pyttsx3.init('sapi5')
            voices = comp.getProperty('voices')
            comp.setProperty('voice', voices[len(voices) - 1].id)
            voiceTest = "This is a female voice"
            comp.say(voiceTest)
            comp.runAndWait()
            run = False

        else : 
            run = True

text = 'Hello World...'
comp.say(text)
comp.runAndWait()
print(text)  # Printing : 'Hello World'

text = 'Initializing Jarvis....'
comp.say(text)
comp.runAndWait()
print(text)

text = 'Starting all systems applications....'
comp.say(text)
comp.runAndWait()
print(text)

text = 'Installing and checking all drivers....'
comp.say(text)
comp.runAndWait()
print(text)

text = 'Caliberating and examining all the core processors....'
comp.say(text)
comp.runAndWait()
print(text)

text = 'Checking the internet connection....'
comp.say(text)
comp.runAndWait()
print(text)

text = 'Wait a moment sir....'
comp.say(text)
comp.runAndWait()
print(text)

text = 'All drivers are up and running....'
comp.say(text)
comp.runAndWait()
print(text)

text = 'All systems have been activated....'
comp.say(text)
comp.runAndWait()
print(text)

text = 'Now I am online....'
comp.say(text)
comp.runAndWait()
print(text)

text = "I can do the following things --> \n 1. Say about me \n 2. About my creator \n 3. Do some maths \n 4. Open few websites \n 5. Say a joke \n 6. Talk anything random with you \n 7. Play games like - Rock,Paper,Scissors; Dice Game; Pong Game; Catch Game; X and O Game. \n 8. Open Calculator"
comp.say(text)
comp.runAndWait()
print(text)

questions = ['What can I do for you?', 'How may I help you?']

global operation
global ans
global n_of_nums
global i
global numbers
global user_num
global q_ans
global name
ans = 'hello'
numbers = []
name = ""

# Global Variables
board = ['-', '-', '-',
         '-', '-', '-',
         '-',  '-', '-']

# If game is still going
game_still_going = True

# Who won? Or tie?
winner = None

# Who's turn is it?
current_player = "X"

global humanChoice
global computerChoice
global notify_text

class Work : 
	def __init__(self) : 
		self.__init__()

	def say_hello() : 
		comp.say("Hello")
		comp.runAndWait()
		print("Hello")

	def greet() : 
		global ans
		comp.say(ans)
		comp.runAndWait()
		print(ans)

	def say_bye() : 
		text = "Please type quit to exit the program" 
		comp.say(text)
		comp.runAndWait()
		print(text)

	def dont_understand() : 
		text = "I don't understand what you are saying"
		comp.say(text)
		comp.runAndWait()
		print(text)

	def not_capable() : 
		text = "I am not capable of performing the oparation given to me."
		comp.say(text)
		comp.runAndWait()
		print(text)

	def quitting() : 
		comp.say('Good Bye Sir')
		comp.runAndWait()
		print('Good Bye Sir')
		text = "Closing the program..."
		comp.say(text)
		comp.runAndWait()
		print(text)

	def get_operation() : 
		global operation
		text = "I am capable of performing addition, subtraction, multiplication, division, square, cube, min, max."
		comp.say(text)
		comp.runAndWait()
		print(text + ': ')
		comp.say("Please enter the operation here")
		comp.runAndWait()
		operation = input("Please enter the operation here : ")

	def add() :
		global n_of_nums
		global i
		global numbers
		global user_num
		global q_ans
		i = 1
		text = "How many numbers do you want me to add : "
		comp.say(text)
		comp.runAndWait()
		n_of_nums = int(input(text))
		while i <= n_of_nums : 
			user_num = int(input(f"Enter num {i} : "))
			numbers.append(user_num)
			i += 1
		q_ans = sum(numbers)
		text = f"The sum of the numbers given is {q_ans}"
		comp.say(text)
		comp.runAndWait()
		print(text)

	def subtract() : 
		global q_ans
		num1 = int(input("Enter the first number : "))
		num2 = int(input("Enter the second number : "))
		q_ans = num1 - num2
		text = f"The difference of {num1} ans {num2} is {q_ans}"
		comp.say(text)
		comp.runAndWait()
		print(text)

	def multiply() : 
		global n_of_nums
		global i
		global numbers
		global user_num
		global q_ans
		q_ans = 1
		i = 1
		text = "How many numbers do you want me to multiply : "
		comp.say(text)
		comp.runAndWait()
		n_of_nums = int(input(text))
		while i <= n_of_nums : 
			user_num = int(input(f"Enter num {i} : "))
			numbers.append(user_num)
			i += 1
		for element in numbers : 
			q_ans = q_ans * element
		text = f"The product of the numbers given is {q_ans}"
		comp.say(text)
		comp.runAndWait()
		print(text)

	def divide() : 
		global q_ans
		num1 = int(input("Enter the first number : "))
		num2 = int(input("Enter the second number : "))
		q_ans = num1 / num2
		text = f"The division of {num1} ans {num2} results in {q_ans}"
		comp.say(text)
		comp.runAndWait()
		print(text)

	def square() : 
		global q_ans
		num1 = int(input("Enter the number you want to square : "))
		q_ans = num1 * num1
		text = f"The square of {num1} is {q_ans}"
		comp.say(text)
		comp.runAndWait()
		print(text)

	def cube() : 
		global q_ans
		num1 = int(input("Enter the number you want to cube : "))
		q_ans = num1 * num1 * num1
		text = f"The cube of {num1} is {q_ans}"
		comp.say(text)
		comp.runAndWait()
		print(text)

	def maximum_num() : 
		global n_of_nums
		global i
		global numbers
		global user_num
		global q_ans
		i = 1
		text = "How many numbers you want me to take out the maximum for : "
		comp.say(text)
		comp.runAndWait()
		n_of_nums = int(input(text))
		while i <= n_of_nums : 
			user_num = int(input(f"Enter num {i} : "))
			numbers.append(user_num)
			i+= 1
		q_ans = max(numbers)
		text = f"The maximum number of the numbers given is {q_ans}"
		comp.say(text)
		comp.runAndWait()
		print(text)

	def minimum_num() : 
		global n_of_nums
		global i
		global numbers
		global user_num
		global q_ans
		i = 1
		text = "How many numbers you want me to take out the minimum for : "
		comp.say(text)
		comp.runAndWait()
		n_of_nums = int(input(text))
		while i <= n_of_nums : 
			user_num = int(input(f"Enter num {i} : "))
			numbers.append(user_num)
			i += 1
		q_ans = min(numbers)
		text = f"The minimum number of the numbers given is {q_ans}"
		comp.say(text)
		comp.runAndWait()
		print(text)

	def my_name() : 
		text = "My name is Jarvis."
		comp.say(text)
		comp.runAndWait()
		print(text)

	def set_your_name() : 
		global name
		text = "Enter you name : "
		comp.say(text)
		comp.runAndWait()
		name = input(text)

	def your_name() : 
		global name
		text = f"Your name is {name}."
		comp.say(text)
		comp.runAndWait()
		print(text)

	def say_thanks() : 
		text = "My pleasure!"
		comp.say(text)
		comp.runAndWait()
		print(text)

	def my_age() : 
		text = "My age is Infinity!"
		comp.say(text)
		comp.runAndWait()
		print(text)

	def birth_date() : 
		text = "I was born Infinity years ago."
		comp.say(text)
		comp.runAndWait()
		print(text)

	def birthday() : 
		text = "My birthday is on 15th February."
		comp.say(text)
		comp.runAndWait()
		print(text)

	def mother_father_name() :
		text = "I dont have any mother or father but Sagnik Biswas invented me."
		comp.say(text)
		comp.runAndWait()
		print(text)

	def mother_name() : 
		text = "I dont have any mother but Sagnik Biswas invented me."
		comp.say(text)
		comp.runAndWait()
		print(text)

	def father_name() : 
		text = "I dont have any father but Sagnik Biswas  invented me."
		comp.say(text)
		comp.runAndWait()
		print(text)

	def inventer() : 
		text = "Sagnik Biswas  invented me."
		comp.say(text)
		comp.runAndWait()
		print(text)		

	def cant_physical_activities() : 
		text = "I can't perform any physical activities."
		comp.say(text)
		comp.runAndWait()
		print(text)		

	def consume_electricity() :  
		text = "I consume electricity and electricity is only my food."
		comp.say(text)
		comp.runAndWait()
		print(text)

	def fibonacci_series() :
		while True :
			try :
				terms = int(input("How many terms of fibonacci series do you want : "))
				value = True
			except ValueError :
				print("The value can only be a number. ")
				value = False  
			if value :
				break
	             
		i = 1  
		n = 0 
		n2 = 1 
		while i <= terms :
			next_term = n + n2 
			print(next_term)
			n = n2
			n2 = next_term
			i += 1

	def palindrome() : 
		palindrome_num = 0
		num = input("Enter a number : ")
		num_length = len(num)
		num = int(num)

		for i in range(num_length) : 
			palindrome_num = palindrome_num * 10
			palindrome_num = palindrome_num + num % 10
			num = int(num / 10)

		print(palindrome_num)

	def read_webs() : 
		text = "I don't read book but I do read websites and webpages."
		comp.say(text)
		comp.runAndWait()
		print(text)

	def yes_read() : 
		text = "Yes. I do read websites."
		comp.say(text)
		comp.runAndWait()
		print(text)

	def do_work() : 
		text = "I am a bot and hence my work is to answer peoples questions."
		comp.say(text)
		comp.runAndWait()
		print(text)

	def about_me() : 
		text = "I am a bot and my name is Jarvis. My work is to address peoples' doubts and question for me. Its a very fun job to do ans I like it. My Birthday is on 15 February. I am invented by Sagnik Biswas ."
		comp.say(text)
		comp.runAndWait()
		print(text)

	def incapable_physical() : 
		text = "I am incapable of performing physical activities."
		comp.say(text)
		comp.runAndWait()
		print(text)

	def open_google() :
		text = "Opening google...."
		comp.say(text)
		comp.runAndWait()
		print(text)	
		webbrowser.open('www.google.com')

	def open_youtube() :
		text = "Opening youtube...."
		comp.say(text)
		comp.runAndWait()
		print(text)	
		webbrowser.open('www.youtube.com')

	def open_wiki() :
		text = "Opening wikipedia...."
		comp.say(text)
		comp.runAndWait()
		print(text)	
		webbrowser.open('www.wikipedia.org')

	def joke() :
		text = "Telling a joke...."
		comp.say(text)
		comp.runAndWait()
		print(text)	
		My_joke = pyjokes.get_joke(language="en", category="neutral")
		comp.say(My_joke)
		comp.runAndWait()
		print(My_joke)	

	def collatz() :
	    collatz_number = 0 

	    while collatz_number != 1 : 
	        try :
	            number = int(input("Enter a number : "))
	        except ValueError :
	            print("Invalid Value. ")

	        if number % 2 == 0 :
	            collatz_number =  number // 2
	            print(collatz_number)

	        else :
	            collatz_number = 3 * number + 1
	            print(collatz_number)

def x_and_o() : 
	global board
	global game_still_going
	global winner
	global current_player

	def display_board() :
	    print(board[0] + " | " + board[1] + " | " + board[2])
	    print(board[3] + " | " + board[4] + " | " + board[5])
	    print(board[6] + " | " + board[7] + " | " + board[8])

	def handle_turn(player) : 
	    print(player + "'s turn.")
	    position = input("Choose a position from 1-9 : ")

	    valid = False
	    while not valid : 
	        # If it's not a number
	        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] : 
	            position = input("Invalid input. Choose a position from 1-9 : ")

	        position = int(position) - 1

	        if board[position] == "-" : 
	            valid = True

	        else : 
	            print("You can't go there. Go again.")

	    # Set the board position
	    board[position] = player
	    display_board()

	def check_if_game_over() : 
	    check_for_winner()
	    check_if_tie()

	def check_for_winner() : 
	    # Set up global variable
	    global winner

	    # Check rows
	    row_winner = check_rows()

	    # Check coulumns
	    column_winner = check_columns()

	    # Check diagonals
	    diagonal_winner = check_diagonals()

	    if row_winner : 
	        winner = row_winner

	    elif column_winner : 
	        winner = column_winner

	    elif diagonal_winner : 
	        winner = diagonal_winner

	    else : 
	        winner = None

	    return

	def check_rows() : 
	    # Set up global variables
	    global game_still_going

	    # Check for rows
	    row_1 = board[0] == board[1] == board[2] != "-"
	    row_2 = board[3] == board[4] == board[5] != "-"
	    row_3 = board[6] == board[7] == board[8] != "-"

	    # If any row has a match, flag that there is a win
	    if row_1 or row_2 or row_3 : 
	        game_still_going = False

	    # Return the winner (X or O)
	    if row_1 : 
	        return board[0]
	    elif row_2 : 
	        return board[3]
	    elif row_3 : 
	        return board[6]
	    return

	def check_columns() :
	    # Set up global variables
	    global game_still_going

	    # Check for columns
	    column_1 = board[0] == board[3] == board[6] != "-"
	    column_2 = board[1] == board[4] == board[7] != "-"
	    column_3 = board[2] == board[5] == board[8] != "-"

	    # If any column has a match, flag that there is a win
	    if column_1 or column_2 or column_3 : 
	        game_still_going = False

	    # Return the winner (X or O)
	    if column_1 : 
	        return board[0]
	    elif column_2 : 
	        return board[1]
	    elif column_3 : 
	        return board[2]
	    return 

	def check_diagonals() : 
	    # Set up global variables
	    global game_still_going

	    # Check for diagonals
	    diagonal_1 = board[0] == board[4] == board[8] != "-"
	    diagonal_2 = board[6] == board[4] == board[2] != "-"

	    # If any diagonals has a match, flag that there is a win
	    if diagonal_1 or diagonal_2 : 
	        game_still_going = False

	    # Return the winner (X or O)
	    if diagonal_1 : 
	        return board[0]
	    elif diagonal_2 : 
	        return board[6]
	    return 

	def check_if_tie() : 
	    # Global variable
	    global game_still_going

	    if "-" not in board : 
	        game_still_going = False
	    return

	def flip_player() :
	    # Global variable
	    global current_player

	    # Change from X to O
	    if current_player == "X" : 
	        current_player = "O"

	    # Change from O to X
	    elif current_player == "O" : 
	        current_player = "X"
	    return

	# Play the game
	def play_game() : 
	    # Display Board
	    display_board()

	    # While the game is still going
	    while game_still_going :
	        # Handle a single turn of an arbitary player
	        handle_turn(current_player)

	        # Check if the game has ended
	        check_if_game_over()

	        # Flip to the other player
	        flip_player()

	    # The game has ended
	    if winner == "X" or winner == "O" : 
	        print(winner + " won.")

	    elif winner == None : 
	        print("Tie.")

	play_game()

def rock_paper_scissors() : 
	num = random.randint(0, 2)
	rps = ['rock', 'paper', 'scissors']
	computerChoice = rps[num]

	run = True
	while run : 
	    hNum = int(input("Enter : \n '1' : Rock \n '2' : Paper \n '3' : Scissors \n >>> "))
	    if hNum > 3 : 
	        print("Invalid Input")
	        run = True
	    
	    else : 
	        humanChoice = rps[hNum - 1]
	        run = False

	print(f"You chose {humanChoice}")
	print(f"Computer chose {computerChoice}")

	if humanChoice == "rock" and computerChoice == "scissors" or humanChoice == "paper" and computerChoice == "rock" or humanChoice == "scissors" and computerChoice == "paper" : 
	    print("You Won!")

	elif humanChoice == "rock" and computerChoice == "paper" or humanChoice == "paper" and computerChoice == "scissors" or humanChoice == "scissors" and computerChoice == "rock" : 
	    print("Jarvis Won!")

	else : 
	    print("It's a tie.")

def simple_calculator() : 
	# Simple Calculator
	root = Tk()
	root.title("Simple Calculator")

	e = Entry(root, width = 45, borderwidth = 5)
	e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
	# e.insert(0, "")

	def button_click(number) :
		# e.delete(0, END)
		current = e.get()
		e.delete(0, END)
		e.insert(0, str(current) + str(number))

	def button_clear() : 
		e.delete(0, END)

	def button_add() : 
		first_number = e.get()
		global num_1
		global math
		math = "addition"
		num_1 = int(first_number)
		e.delete(0, END)

	def button_equal() : 
		second_number = e.get()
		e.delete(0, END)
		num_2 = int(second_number)

		if math == "addition" : 
		    e.insert(0, num_1 + num_2)

		if math == "subtraction" : 
		    e.insert(0, num_1 - num_2)

		if math == "multiplication" : 
		    e.insert(0, num_1 * num_2)

		if math == "division" : 
		    e.insert(0, num_1 / num_2)    

	def button_subtract() :
		first_number = e.get()
		global num_1
		global math
		math = "subtraction"
		num_1 = int(first_number)
		e.delete(0, END)

	def button_multiply() : 
		first_number = e.get()
		global num_1
		global math
		math = "multiplication"
		num_1 = int(first_number)
		e.delete(0, END)

	def button_divide() : 
		first_number = e.get()
		global num_1
		global math
		math = "division"
		num_1 = int(first_number)
		e.delete(0, END)


	# Define buttons
	button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda : button_click(1))
	button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda : button_click(2))
	button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda : button_click(3))
	button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda : button_click(4))
	button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda : button_click(5))
	button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda : button_click(6))
	button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda : button_click(7))
	button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda : button_click(8))
	button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda : button_click(9))
	button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda : button_click(0))

	button_equal = Button(root, text = "=", padx = 91, pady = 20, command = button_equal)
	button_clear = Button(root, text = "Clear", padx = 79, pady = 20, command = button_clear)

	button_add = Button(root, text = "+", padx = 39, pady = 20, command = button_add)
	button_subtract = Button(root, text = "-", padx = 41, pady = 20, command = button_subtract)
	button_multiply = Button(root, text = "*", padx = 42, pady = 20, command = button_multiply)
	button_divide = Button(root, text = "/", padx = 42, pady = 20, command = button_divide)

	# Put the button on the screen
	button_1.grid(row = 3 , column = 0)
	button_2.grid(row = 3 , column = 1)
	button_3.grid(row = 3 , column = 2)

	button_4.grid(row = 2 , column = 0)
	button_5.grid(row = 2 , column = 1)
	button_6.grid(row = 2 , column = 2)

	button_7.grid(row = 1 , column = 0)
	button_8.grid(row = 1 , column = 1)
	button_9.grid(row = 1 , column = 2)

	button_0.grid(row = 4 , column = 0)
	button_clear.grid(row = 4, column = 1, columnspan = 2)
	button_add.grid(row = 5, column = 0)
	button_equal.grid(row = 5, column = 1, columnspan = 2)

	button_subtract.grid(row = 6, column = 0)
	button_multiply.grid(row = 6, column = 1)
	button_divide.grid(row = 6, column = 2)

	root.mainloop()

def dice_simulator() :
	root = Tk()
	root.title("Dice Simulator")

	num = 0

	def randomNumber() : 
	    global num
	    num = random.randint(1, 6)
	    numLabel = Label(root, text = num)
	    numLabel.pack()

	label1 = Label(root, text = "Click button below to generate a random number.")
	button1 = Button(root, text = "Generate Random Number", command = randomNumber)

	label1.pack()
	button1.pack()

	root.mainloop()

def pong_game() : 
	pygame.init()

	win = pygame.display.set_mode((750, 500))

	pygame.display.set_caption('Pong Game')

	white = (255, 255, 255)
	black = (0, 0, 0)

	class Paddle(pygame.sprite.Sprite) : 
	    def __init__(self) : 
	        pygame.sprite.Sprite.__init__(self)
	        self.image = pygame.Surface([10, 75])
	        self.image.fill(white)
	        self.rect = self.image.get_rect()
	        self.points = 0

	class Ball(pygame.sprite.Sprite) : 
	    def __init__(self) : 
	        pygame.sprite.Sprite.__init__(self)
	        self.image = pygame.Surface([10, 10])
	        self.image.fill(white)
	        self.rect = self.image.get_rect()
	        self.speed = 10
	        self.dx = 1
	        self.dy = 1

	paddle1 = Paddle()
	paddle1.rect.x = 25
	paddle1.rect.y = 225

	paddle2 = Paddle()
	paddle2.rect.x = 715
	paddle2.rect.y = 225

	paddle_speed = 20

	pong = Ball()
	pong.rect.x = 375
	pong.rect.y = 250

	all_sprites = pygame.sprite.Group()
	all_sprites.add(paddle1, paddle2, pong)

	def redraw() : 
	    win.fill(black)

	    # Title Font
	    font = pygame.font.SysFont('Comic Sans MS', 30)
	    text = font.render('PONG', False, white)
	    textRect = text.get_rect()
	    textRect.center = (750//2, 25)
	    win.blit(text, textRect)

	    # Player 1 Score
	    p1_score = font.render(str(paddle1.points), False, white)
	    p1Rect = p1_score.get_rect()
	    p1Rect.center = (50, 50)
	    win.blit(p1_score, p1Rect)

	    # Player 2 Score
	    p2_score = font.render(str(paddle2.points), False, white)
	    p2Rect = p2_score.get_rect()
	    p2Rect.center = (700, 50)
	    win.blit(p2_score, p2Rect)

	    all_sprites.draw(win)
	    pygame.display.update()

	run = True
	while run : 
	    pygame.time.delay(100)

	    for event in pygame.event.get() : 
	        if event.type == pygame.QUIT : 
	            run = False
	    
	    key = pygame.key.get_pressed()
	    if key[pygame.K_w] : 
	        paddle1.rect.y += -paddle_speed
	    
	    if key[pygame.K_s] : 
	        paddle1.rect.y += paddle_speed
	    
	    if key[pygame.K_UP] : 
	        paddle2.rect.y += -paddle_speed
	    
	    if key[pygame.K_DOWN] : 
	        paddle2.rect.y += paddle_speed

	    pong.rect.x += pong.speed * pong.dx
	    pong.rect.y += pong.speed * pong.dy

	    if pong.rect.y > 490 : 
	        pong.dy = -1

	    if pong.rect.x > 740 : 
	        pong.rect.x, pong.rect.y = 375, 250
	        pong.dx = -1
	        paddle1.points += 1

	    if pong.rect.y < 10 : 
	        pong.dy = 1

	    if pong.rect.x < 10 : 
	        pong.rect.x, pong.rect.y = 375, 250
	        pong.dx = 1
	        paddle2.points += 1

	    if paddle1.rect.colliderect(pong.rect) : 
	        pong.dx = 1

	    if paddle2.rect.colliderect(pong.rect) : 
	        pong.dx = -1

	    redraw()

	pygame.quit()

def catch_game() : 
	pygame.init()

	screen = (750, 500)
	win = pygame.display.set_mode(screen)

	pygame.display.set_caption("Catch Game")

	white = (255, 255, 255)
	black = (0, 0, 0)
	red = (255, 0, 0)
	blue = (0, 0, 255)
	green = (0, 255, 0)
	yellow = (255, 255, 0)

	class Paddle(pygame.sprite.Sprite) : 
	    def __init__(self) : 
	        pygame.sprite.Sprite.__init__(self)
	        self.image = pygame.Surface([75, 10])
	        self.image.fill(red)
	        self.rect = self.image.get_rect()
	        self.points = 0

	class Ball(pygame.sprite.Sprite) : 
	    def __init__(self) : 
	        pygame.sprite.Sprite.__init__(self)
	        self.image = pygame.Surface([10, 10])
	        self.image.fill(yellow)
	        self.rect = self.image.get_rect()
	        self.speed = 10
	        self.dx = 1
	        self.dy = 1

	paddle = Paddle()
	paddle.rect.x = 350
	paddle.rect.y = 480

	ball = Ball()
	ball.rect.x = 375
	ball.rect.y = 250

	paddle_speed = 20

	all_sprites = pygame.sprite.Group()
	all_sprites.add(paddle, ball)

	def redraw() : 
	    win.fill(black)
	    
	    # Title Font
	    font = pygame.font.SysFont('Comic Sans MS', 30)
	    text = font.render('Catch Game', False, white)
	    textRect = text.get_rect()
	    textRect.center = (750//2, 25)
	    win.blit(text, textRect)
	    
	    # Player Score
	    p1_score = font.render(str(paddle.points), False, yellow)
	    p1Rect = p1_score.get_rect()
	    p1Rect.center = (750//2, 80)
	    win.blit(p1_score, p1Rect)

	    all_sprites.draw(win)
	    pygame.display.update()

	run = True
	while run :  
	    pygame.time.delay(50)

	    for event in pygame.event.get() : 
	        if event.type == pygame.QUIT : 
	            run = False

	    key = pygame.key.get_pressed()
	    if key[pygame.K_LEFT] : 
	        paddle.rect.x += -paddle_speed

	    if key[pygame.K_RIGHT] : 
	        paddle.rect.x += paddle_speed

	    ball.rect.x += ball.speed * ball.dx
	    ball.rect.y += ball.speed * ball.dy

	    if ball.rect.y > 490 : 
	        ball.rect.x, ball.rect.y = 375, 250
	        ball.dy = -1
	        paddle.points -= 1

	    if ball.rect.x > 740 : 
	        ball.dx += -1

	    if ball.rect.y < 10 : 
	        ball.dy += 1

	    if ball.rect.x < 10 : 
	        ball.dx += 1

	    if paddle.rect.colliderect(ball.rect) : 
	        ball.dy = -1
	        paddle.points += 1 

	    redraw() 

	pygame.quit()

while ans != 'quit' : 
	num = random.randrange(0, 2)
	question = questions[num]

	comp.say(question)
	comp.runAndWait()

	ans = input(question + ' : ')

	if ans.lower() == 'hello' or ans.lower() == 'kem chho' or ans.lower() == 'hy' or ans.lower() == 'hi' : 
		Work.say_hello()

	elif ans.lower() == 'good morning' or ans.lower() == 'good evening' or ans.lower() == 'good afternoon' : 
		Work.greet()

	elif ans.lower() == 'bye' or ans.lower() == 'goodbye' or ans.lower() == 'good' or ans.lower() == 'sayonara' :
		Work.say_bye()

	elif ans.lower() == 'good day' or ans.lower() == 'good night' : 
		Work.say_bye()

	elif ans.lower() == 'perform a calculation for me' or ans.lower() == 'calculation' or ans.lower() == 'calculate' : 
		Work.get_operation()
		if operation.lower() == "addition" or operation.lower() == "add" : 
			Work.add()
		elif operation.lower() == "add numbers" or operation.lower() == "add nums" or operation.lower() == "add number" or operation.lower() == "add num" : 
			Work.add()
		elif operation.lower() == "subtraction" or operation.lower() == "subtract" :
			Work.subtract()
		elif operation.lower() == "subtract numbers" or operation.lower() == "subtract nums" or operation.lower() == "subtract number" or operation.lower() == "subtract num" : 
			Work.subtract()
		elif operation.lower() == "multiplication" or operation.lower() == "multiply" : 
			Work.multiply()
		elif operation.lower() == "multiply numbers" or operation.lower() == "multiply nums" or operation.lower() == "multiply number" or operation.lower() == "multiply num" : 
			Work.multiply()
		elif operation.lower() == "division" or operation.lower() == "divide" : 
			Work.divide()
		elif operation.lower() == "divide numbers" or operation.lower() == "divide nums" or operation.lower() == "divide number" or operation.lower() == "divide num" : 
			Work.divide()
		elif operation.lower() == "square" or operation.lower() == "squaring" or operation.lower() == "square number" or operation.lower() == "square num" : 
			Work.square()
		elif operation.lower() == "cube" or operation.lower() == "cubing" or operation.lower() == "cube numbers" or operation.lower() == "cube num" : 
			Work.cube()
		elif operation.lower() == "max" or operation.lower() == "maximum" : 
			Work.maximum_num()
		elif operation.lower() == "max num" or operation.lower() == "max number" or operation.lower() == "maximum num" or operation.lower() == "maximum number" : 
			Work.maximum_num()
		elif operation.lower() == "min" or operation.lower() == "minimum" : 
			Work.minimum_num()
		elif operation.lower() == "min num" or operation.lower() == "min number" or operation.lower() == "minimum num" or operation.lower() == "minimum number" :
			Work.minimum_num()
		else : 
			Work.not_capable()

	elif ans.lower() == "addition" or ans.lower() == "add" : 
		Work.add()
	elif ans.lower() == "add numbers" or ans.lower() == "add nums" or ans.lower() == "add number" or ans.lower() == "add num" : 
		Work.add()

	elif ans.lower() == "subtraction" or ans.lower() == "subtract" :
		Work.subtract()
	elif ans.lower() == "subtract numbers" or ans.lower() == "subtract nums" or ans.lower() == "subtract number" or ans.lower() == "subtract num" : 
		Work.subtract()

	elif ans.lower() == "multiplication" or ans.lower() == "multiply" : 
		Work.multiply()
	elif ans.lower() == "multiply numbers" or ans.lower() == "multiply nums" or ans.lower() == "multiply number" or ans.lower() == "multiply num" : 
		Work.multiply()

	elif ans.lower() == "division" or ans.lower() == "divide" : 
		Work.divide()
	elif ans.lower() == "divide numbers" or ans.lower() == "divide nums" or ans.lower() == "divide number" or ans.lower() == "divide num" : 
		Work.divide()

	elif ans.lower() == "square" or ans.lower() == "squaring" or ans.lower() == "square number" or ans.lower() == "square num" : 
		Work.square()

	elif ans.lower() == "cube" or ans.lower() == "cubing" or ans.lower() == "cube numbers" or ans.lower() == "cube num" : 
		Work.cube()

	elif ans.lower() == "max" or ans.lower() == "maximum" : 
		Work.maximum_num()
	elif ans.lower() == "max num" or ans.lower() == "max number" or ans.lower() == "maximum num" or ans.lower() == "maximum number" : 
		Work.maximum_num()

	elif ans.lower() == "min" or ans.lower() == "minimum" : 
		Work.minimum_num()
	elif ans.lower() == "min num" or ans.lower() == "min number" or ans.lower() == "minimum num" or ans.lower() == "minimum number" :
		Work.minimum_num()

	elif ans.lower() == 'quit' : 
		Work.quitting()

	elif ans.lower() == 'what is your name' or ans.lower() == "tell your name" or ans.lower() == "your name" : 
		Work.my_name()

	elif ans.lower() == "set my name" or ans.lower() == "save my name" or ans.lower() == "write my name" or ans.lower() == "record my name" : 
		Work.set_your_name()

	elif ans.lower() == "what is my name" or ans.lower() == "my name" or ans.lower() == "tell my name" : 
		Work.your_name()

	elif ans.lower() == "please open google" or ans.lower() == "google" or ans.lower() == "google website" or ans.lower() == "open google": 
		Work.open_google()

	elif ans.lower() == "please open youtube" or ans.lower() == "youtube" or ans.lower() == "youtube website" or ans.lower() == "open youtube": 
		Work.open_youtube()

	elif ans.lower() == "please open wikipedia" or ans.lower() == "wikipedia" or ans.lower() == "wikipedia website" or ans.lower() == "open wikipedia": 
		Work.open_wiki()	

	elif ans.lower() == "please say a joke" or ans.lower() == "joke" or ans.lower() == "jokes please" : 
		Work.jokes()

	elif ans.lower() == "thanks" or ans.lower() == "thankz" or ans.lower() == "thank you" or ans.lower() == "thankyou" or ans.lower() == "thnkz" or ans.lower() == "thnks" : 
		Work.say_thanks()

	elif ans.lower() == "what is your age" or ans.lower() == "tell your age" or ans.lower() == "your age" or ans.lower() == "enter your age" :
		Work.my_age()

	elif ans.lower() == "what is your birth date" or ans.lower() == "tell your birth date" or ans.lower() == "your birth date" or ans.lower() == "enter your birth date" or ans.lower() == "when were you born" :
		Work.birth_date()

	elif ans.lower() == "when is your birthday" or ans.lower() == "tell your birthday" or ans.lower() == "your birthday" or ans.lower() == "enter your birthday" : 
		Work.birthday()

	elif ans.lower() == "when is your birth day" or ans.lower() == "tell your birth day" or ans.lower() == "your birth day" or ans.lower() == "enter your birth day" : 
		Work.birthday()

	elif ans.lower() == "what is your mothers and fathers name" or ans.lower() == "mothers and fathers name" or ans.lower() == "tell your mothers and fathers name" : 
		Work.mother_father_name()

	elif ans.lower() == "what is your mothers or fathers name" or ans.lower() == "mothers or fathers name" or ans.lower() == "tell your mothers or fathers name" : 
		Work.mother_father_name()

	elif ans.lower() == "what is your fathers name" or ans.lower() == "fathers name" or ans.lower() == "tell your fathers name" : 
		Work.father_name()

	elif ans.lower() == "what is your mothers name" or ans.lower() == "mothers name" or ans.lower() == "tell your mothers name" : 
		Work.mother_name()

	elif ans.lower() == "what is your inventers name" or ans.lower() == "who made you" or ans.lower() == "who invented you" or ans.lower() == "who is your inventer" : 
		Work.inventer()

	elif ans.lower() == "can you dance" or ans.lower() == "can you play" or ans.lower() == "can you hit, kick or punch" : 
		Work.cant_physical_activities()

	elif ans.lower() == "what do you eat" or ans.lower() == "what is your food" or ans.lower() == "your food" or ans.lower() == "what do you consume" : 
		Work.consume_electricity()

	elif ans.lower() == "tell me the fibonacci series" or ans.lower() == "what is the fibonacci series" or ans.lower() == "fibonacci series" : 
		Work.fibonacci_series()

	elif ans.lower() == "tell me the fibonacci sequence" or ans.lower() == "what is the fibonacci sequence" or ans.lower() == "fibonacci sequence" : 
		Work.fibonacci_series()

	elif ans.lower() == "palindrome number" or ans.lower() == "palindrome" or ans.lower() == "palindrome numbers" or ans.lower() == "palindrome num" or ans.lower() == "palindrome nums" : 
		Work.palindrome()

	elif ans.lower() == "what do you read" : 
		Work.read_webs()

	elif ans.lower() == "do you read" or ans.lower() == "can you read" : 
		Work.yes_read()

	elif ans.lower() == "what is your work" or ans.lower() == "what do you do" or ans.lower() == "what work do you do" : 
		Work.do_work()

	elif ans.lower() == "who are you" or ans.lower() == "what are you" : 
		Work.about_me()

	elif ans.lower() == "tell about you" or ans.lower() == "about you" or ans.lower() == "tell me something about you" or ans.lower() == "something about you" or ans.lower() == "tell something about you" : 
		Work.about_me()

	elif ans.lower() == "can you kick" or ans.lower() == "can you punch" or ans.lower() == "can you hit" or ans.lower() == "can you jump" : 
		Work.incapable_physical()

	elif ans.lower() == "collatz" or ans.lower() == "collatz number" or ans.lower() == "collatz sequence" : 
		Work.collatz()

	elif ans.lower() == "tell me the collatz sequence" or ans.lower() == "what is the collatz sequence" : 
		Work.collatz()

	elif ans.lower() == "x and o game" or ans.lower() == "set a x and o board for me" or ans.lower() == "arrange a x and o game for me" : 
		x_and_o()

	elif ans.lower() == "x and o board" or ans.lower() == "i want to play x and o" or ans.lower() == "play game" or ans.lower() == "play x and o" : 
		x_and_o()

	elif ans.lower() == "calculator" or ans.lower() == "open a calculator for me" or ans.lower() == "open a calculator" : 
		simple_calculator()

	elif ans.lower() == "i want a calculator" or ans.lower() == "give me a calculator" or ans.lower() == "i want to perform a calculation" or ans.lower() == "i want to do a calculation" : 
		simple_calculator()

	elif ans.lower() == "play rock paper scissors" or ans.lower() == "rock paper scissor" or ans.lower() == "rock paper scissors" or ans.lower() == "rock paper scissor" : 
		rock_paper_scissors()

	elif ans.lower() == "dice game" or ans.lower() == "dice" or ans.lower() == "dice simulator" or ans.lower() == "get me a dice" : 
		dice_simulator()

	elif ans.lower() == "pong game" or ans.lower() == "play pong game" or ans.lower() == "open pong" or ans.lower() == "pong" or ans.lower() == "play pong" or ans.lower() == "open pong game" : 
		pong_game()

	elif ans.lower() == "catch game" or ans.lower() == "play catch game" or ans.lower() == "open catch" or ans.lower() == "catch" or ans.lower() == "play catch" or ans.lower() == "open catch game" : 
		catch_game()

	else : 
		Work.dont_understand()