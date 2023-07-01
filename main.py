# Imports
import customtkinter as ctk
from random import randint

# App Setup
app = ctk.CTk()
app.title('CTk_TicTacToe')
w = app.winfo_screenwidth()
h = app.winfo_screenheight()
app.geometry(f'{int(w/1.5)}x{int(h/1.35)}')

# Initial Apperance
ctk.set_appearance_mode('system')

# Variables
turn_number = 1
button_font = font=('Arial', 65, 'bold')
button_array = []
player_turn = []
winner = []
x_score = 0
o_score = 0

# Frame Widgets
top_label = ctk.CTkLabel(master=app, text='CTk TicTacToe', text_color='black', font=('Arial', 40, 'bold'))
top_label.pack()
player_frame = ctk.CTkFrame(master=app, fg_color='transparent', width=w/3)
player_frame.pack(pady=10)
game_frame = ctk.CTkFrame(master=app, fg_color='black', width=w/3, height=h/2, border_width=2, border_color='black')
game_frame.pack()
button_frame = ctk.CTkFrame(master=app, fg_color='transparent', width=w/3)
button_frame.pack(pady=10)

# Label Widgets
x_label = ctk.CTkLabel(master=player_frame, text="Player X", text_color='green', font=('Arial', 20, 'bold'))
x_label.grid(row=0, column=0, padx=10)
x_player_light = ctk.CTkButton(master=player_frame, text=None, height=12, width=12, fg_color='black', border_width=2,
                               border_color='black', state='disabled')
x_player_light.grid(row=0, column=1)
player_label = ctk.CTkLabel(master=player_frame, text='', font=('Arial', 20, 'bold'), width=w/5)
player_label.grid(row=0, column=2, padx=10)
o_label = ctk.CTkLabel(master=player_frame, text="Player O", text_color='red', font=('Arial', 20, 'bold'))
o_label.grid(row=0, column=3)
o_player_light = ctk.CTkButton(master=player_frame, text=None, height=12, width=12, fg_color='black', border_width=2,
                               border_color='black', state='disabled')
o_player_light.grid(row=0, column=4, padx=10)
x_score_label = ctk.CTkLabel(master=player_frame, text=x_score, text_color='green', font=('Arial', 20, 'bold'))
x_score_label.grid(row=1, column=0)
o_score_label = ctk.CTkLabel(master=player_frame, text=o_score, text_color='red', font=('Arial', 20, 'bold'))
o_score_label.grid(row=1, column=3)


# Functions
def win_condition():
    if button_array[0].cget('text'):
        if button_array[0].cget('text') == button_array[1].cget('text') and button_array[0].cget('text') == \
            button_array[2].cget('text'):
            win_score()
            for button in button_array[0:3]:
                button.configure(border_width=3, border_color='yellow')
            for button in button_array:
                button.configure(state='disabled')
        elif button_array[0].cget('text') == button_array[3].cget('text') and button_array[0].cget('text') == \
            button_array[6].cget('text'):
            win_score()
            for button in button_array[0:7:3]:
                button.configure(border_width=3, border_color='yellow')
            for button in button_array:
                button.configure(state='disabled')
    if button_array[8].cget('text'):
        if button_array[2].cget('text') == button_array[5].cget('text') and button_array[2].cget('text') == \
            button_array[8].cget('text'):
            win_score()
            for button in button_array[2:9:3]:
                button.configure(border_width=3, border_color='yellow')
            for button in button_array:
                button.configure(state='disabled')
        elif button_array[6].cget('text') == button_array[7].cget('text') and button_array[6].cget('text') == \
            button_array[8].cget('text'):
            win_score()
            for button in button_array[6:9]:
                button.configure(border_width=3, border_color='yellow')
            for button in button_array:
                button.configure(state='disabled')
    if button_array[4].cget('text'):
        if button_array[4].cget('text') == button_array[1].cget('text') and button_array[4].cget('text') == \
            button_array[7].cget('text'):
            win_score()
            for button in button_array[1:8:3]:
                button.configure(border_width=3, border_color='yellow')
            for button in button_array:
                button.configure(state='disabled')
        elif button_array[4].cget('text') == button_array[3].cget('text') and button_array[4].cget('text') == \
            button_array[5].cget('text'):
            win_score()
            for button in button_array[3:6]:
                button.configure(border_width=3, border_color='yellow')
            for button in button_array:
                button.configure(state='disabled')
        elif button_array[4].cget('text') == button_array[0].cget('text') and button_array[4].cget('text') == \
            button_array[8].cget('text'):
            win_score()
            for button in button_array[0:9:4]:
                button.configure(border_width=3, border_color='yellow')
            for button in button_array:
                button.configure(state='disabled')
        elif button_array[4].cget('text') == button_array[2].cget('text') and button_array[4].cget('text') == \
            button_array[6].cget('text'):
            win_score()
            for button in button_array[2:7:2]:
                button.configure(border_width=3, border_color='yellow')
            for button in button_array:
                button.configure(state='disabled')

def tie_contition():
    if turn_number == 10 and winner == []:
        x_player_light.configure(fg_color='black')
        o_player_light.configure(fg_color='black')
        player_label.configure(text=f'Game is a tie!', text_color='black')

def clear_board():
    global turn_number
    turn_number = 1
    player_turn.clear()
    winner.clear()
    starting_player()
    for button in button_array:
        button.configure(text='', state='normal', border_width=0)

def click_button(button_press):
    global turn_number
    turn_number += 1
    if player_turn[-1] == 'O':
        eval(button_press).configure(text='O', text_color='red', state='disabled', text_color_disabled='red')
        player_turn.append('X')
        player_label.configure(text="X Player's Turn", text_color='green')
        x_player_light.configure(fg_color='yellow')
        o_player_light.configure(fg_color='black')
    else:
        eval(button_press).configure(text='X', text_color='green', state='disabled', text_color_disabled='green')
        player_turn.append('O')
        player_label.configure(text="O Player's Turn", text_color='red')
        x_player_light.configure(fg_color='black')
        o_player_light.configure(fg_color='yellow')
    win_condition()
    tie_contition()

def quit():
    app.destroy()

def starting_player():
    global turn_number
    starter = randint(1, 2)
    if starter == 1:
        player_turn.append('X')
        player_label.configure(text="X Player's Turn", text_color='green')
        x_player_light.configure(fg_color='yellow')
        o_player_light.configure(fg_color = 'black')
    else:
        player_turn.append('O')
        player_label.configure(text="O Player's Turn", text_color='red')
        x_player_light.configure(fg_color='black')
        o_player_light.configure(fg_color='yellow')

def win_score():
    global x_score
    global o_score
    x_player_light.configure(fg_color='black')
    o_player_light.configure(fg_color='black')
    if player_turn[-1] == 'O':
        player_label.configure(text='Player X wins!', text_color='green')
        x_score += 1
        x_score_label.configure(text=x_score)
    else:
        player_label.configure(text='Player O wins!', text_color='red')
        o_score += 1
        o_score_label.configure(text=o_score)
    winner.append('yes')


# Button Widgets
button_tl = ctk.CTkButton(master=game_frame, fg_color='gainsboro', text='', height=h/6, width=w/10, font=button_font,
                          command=lambda m='button_tl': click_button(m))
button_array.append(button_tl)
button_tl.grid(row=0, column=1, padx=2, pady=2)
button_tm = ctk.CTkButton(master=game_frame, fg_color='gainsboro', text='', height=h/6, width=w/10, font=button_font,
                          command=lambda m='button_tm': click_button(m))
button_array.append(button_tm)
button_tm.grid(row=0, column=2, padx=2, pady=2)
button_tr = ctk.CTkButton(master=game_frame, fg_color='gainsboro', text='', height=h/6, width=w/10, font=button_font,
                          command=lambda m='button_tr': click_button(m))
button_array.append(button_tr)
button_tr.grid(row=0, column=3, padx=2, pady=2)
button_ml = ctk.CTkButton(master=game_frame, fg_color='gainsboro', text='', height=h/6, width=w/10, font=button_font,
                          command=lambda m='button_ml': click_button(m))
button_array.append(button_ml)
button_ml.grid(row=1, column=1, padx=2, pady=2)
button_mm = ctk.CTkButton(master=game_frame, fg_color='gainsboro', text='', height=h/6, width=w/10, font=button_font,
                          command=lambda m='button_mm': click_button(m))
button_array.append(button_mm)
button_mm.grid(row=1, column=2, padx=2, pady=2)
button_mr = ctk.CTkButton(master=game_frame, fg_color='gainsboro', text='', height=h/6, width=w/10, font=button_font,
                          command=lambda m='button_mr': click_button(m))
button_array.append(button_mr)
button_mr.grid(row=1, column=3, padx=2, pady=2)
button_bl = ctk.CTkButton(master=game_frame, fg_color='gainsboro', text='', height=h/6, width=w/10, font=button_font,
                          command=lambda m='button_bl': click_button(m))
button_array.append(button_bl)
button_bl.grid(row=2, column=1, padx=2, pady=2)
button_bm = ctk.CTkButton(master=game_frame, fg_color='gainsboro', text='', height=h/6, width=w/10, font=button_font,
                          command=lambda m='button_bm': click_button(m))
button_array.append(button_bm)
button_bm.grid(row=2, column=2, padx=2, pady=2)
button_br = ctk.CTkButton(master=game_frame, fg_color='gainsboro', text='', height=h/6, width=w/10, font=button_font,
                          command=lambda m='button_br': click_button(m))
button_array.append(button_br)
button_br.grid(row=2, column=3, padx=2, pady=2)

# Functional Buttons
restart_button = ctk.CTkButton(master=button_frame, text='Restart', fg_color='green', height=30, width=30,
                               corner_radius=30, hover_color='darkgreen', font=('Arial', 20), command=clear_board)
restart_button.pack(side='left', padx=25)
quit_button = ctk.CTkButton(master=button_frame, text='Quit', fg_color='red', height=30, width=30, corner_radius=30,
                            hover_color='darkred', font=('Arial', 20), command=quit)
quit_button.pack(side='right', padx=25)

starting_player()

# Loop
app.mainloop()