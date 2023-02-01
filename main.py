import random
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image


def play_game():

    global user_score
    global computer_score

    # get user choice
    user_choice = user_choice_var.get()
    # get computer choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    update_choice(computer_choice)
    # determine winner
    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result_label.config(text="You win!")
        user_score += 1
    else:
        result_label.config(text="You lose!")
        computer_score += 1
    # display computer choice
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    # update score labels
    user_score_label.config(text=f"User Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

#highlighting buttons


def highlight_rock():
    rock_button.config(bg='lightgray')
    paper_button.config(bg='white')
    scissors_button.config(bg='white')


def highlight_paper():
    rock_button.config(bg='white')
    paper_button.config(bg='lightgray')
    scissors_button.config(bg='white')


def highlight_scissors():
    rock_button.config(bg='white')
    paper_button.config(bg='white')
    scissors_button.config(bg='lightgray')


def unhighlight_rock():
    rock_button.config(bg='white')
    paper_button.config(bg='white')
    scissors_button.config(bg='white')


def update_choice(choice):
    if choice == "rock":
        rock_label.config(bg='red')
        paper_label.config(bg='white')
        scissors_label.config(bg='white')
    elif choice == "paper":
        rock_label.config(bg='white')
        paper_label.config(bg='red')
        scissors_label.config(bg='white')
    elif choice == "scissors":
        rock_label.config(bg='white')
        paper_label.config(bg='white')
        scissors_label.config(bg='red')


# create window
root = tk.Tk()
root.geometry("400x400")
root.title("Rock Paper Scissors")

# create variables
user_choice_var = tk.StringVar(value='rock')
user_score = 0
computer_score = 0

# create image objects

rock_image = Image.open('rock.png')
rock_image = rock_image.resize((60, 60))
rock_image.save('resized_rock.png')

paper_image = Image.open('paper.png')
paper_image = paper_image.resize((60, 60))
paper_image.save('resized_paper.png')

scissors_image = Image.open('scissors.png')
scissors_image = scissors_image.resize((60, 60))
scissors_image.save('resized_scissors.png')

# create image objects
rock_image = PhotoImage(file='resized_rock.png')
paper_image = PhotoImage(file='resized_paper.png')
scissors_image = PhotoImage(file='resized_scissors.png')

# create buttons
rock_button = tk.Button(root, image=rock_image, command=lambda: set_choice('rock') or play_game())
rock_button.grid(row=0, column=0)
rock_button.bind('<Button-1>', lambda event: unhighlight_rock() or highlight_rock())

paper_button = tk.Button(root, image=paper_image, command=lambda: set_choice('paper') or play_game())
paper_button.grid(row=0, column=1)
paper_button.bind('<Button-1>', lambda event: unhighlight_rock() or highlight_paper())

scissors_button = tk.Button(root, image=scissors_image, command=lambda: set_choice('scissors') or play_game())
scissors_button.grid(row=0, column=2)
scissors_button.bind('<Button-1>', lambda event: unhighlight_rock() or highlight_scissors())


# create labels

result_label = tk.Label(root, text=' ')
computer_choice_label = tk.Label(root, text=' ')
user_score_label = tk.Label(root, text=f"User Score: {user_score}")
computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}")
rock_label = tk.Label(root, image=rock_image, bg='white', bd=1)
paper_label = tk.Label(root, image=paper_image, bg='white', bd=1)
scissors_label = tk.Label(root, image=scissors_image, bg='white', bd=1)

# add widgets to window
result_label.grid(row=1, column=0, columnspan=3)
computer_choice_label.grid(row=2, column=0, columnspan=3)
user_score_label.grid(row=3, column=0)
computer_score_label.grid(row=3, column=1)
rock_label.grid(row=4, column=0)
paper_label.grid(row=4, column=1)
scissors_label.grid(row=4, column=2)

# a function to set the user_choice


def set_choice(choice):
    user_choice_var.set(choice)

# run loop


root.mainloop()
