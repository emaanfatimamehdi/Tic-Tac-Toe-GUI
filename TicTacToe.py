import tkinter as tk

# Main Window
window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("400x500")
window.resizable(False, False)

# Game Variables
current_player = "X"
game_over = False

# Store all buttons
buttons = []

# Functions
def button_clicked(row, column):
    global current_player, game_over

    # Game over hai to kuch nahi hoga
    if game_over:
        return

    # Agar button already filled hai
    if buttons[row][column]["text"] != "":
        return

    # X ya O button par show karo
    buttons[row][column]["text"] = current_player

    # X aur O ke different colors
    if current_player == "X":
        buttons[row][column].config(
            fg="black"
        )
    else:
        buttons[row][column].config(
            fg="red"
        )

    # Winner check
    if check_winner():
        status_label.config(
            text=current_player + " Wins!"
        )
        game_over = True
        return

    # Draw check
    if check_draw():
        status_label.config(
            text="It's a Draw!"
        )
        game_over = True
        return

    # Player change
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    # Status update
    status_label.config(
        text="Player " + current_player + "'s Turn"
    )


def check_winner():

    # Check Rows
    
    for row in range(3):

        if (
            buttons[row][0]["text"] ==
            buttons[row][1]["text"] ==
            buttons[row][2]["text"] != ""
        ):
            return True

   
    # Check Columns

    for column in range(3):

        if (
            buttons[0][column]["text"] ==
            buttons[1][column]["text"] ==
            buttons[2][column]["text"] != ""
        ):
            return True

    # Check First Diagonal

    if (
        buttons[0][0]["text"] ==
        buttons[1][1]["text"] ==
        buttons[2][2]["text"] != ""
    ):
        return True
    
    # Check Second Diagonal
 
    if (
        buttons[0][2]["text"] ==
        buttons[1][1]["text"] ==
        buttons[2][0]["text"] != ""
    ):
        return True

    return False


def check_draw():

    # Har button check karo
    for row in range(3):

        for column in range(3):

            # Agar koi empty button hai
            # to draw nahi hua
            if buttons[row][column]["text"] == "":
                return False

    return True

def new_game():
    global current_player, game_over
    # Game reset
    current_player = "X"
    game_over = False

    # Status reset
    status_label.config(
        text="Player X's Turn"
    )

    # Saare buttons empty karo
    for row in range(3):

        for column in range(3):

            buttons[row][column].config(
                text="",
                fg="black"
            )


# Title

title_label = tk.Label(
    window,
    text="Tic Tac Toe",
    font=("Arial", 28, "bold")
)

title_label.pack(
    pady=15
)


# Status Label


status_label = tk.Label(
    window,
    text="Player X's Turn",
    font=("Arial", 18)
)

status_label.pack(
    pady=5
)

# Game Board

game_frame = tk.Frame(window)

game_frame.pack(
    pady=20
)

# Create 3 × 3 Buttons
# -----------------------------

for row in range(3):

    button_row = []

    for column in range(3):

        button = tk.Button(
            game_frame,
            text="",
            font=("Arial", 35, "bold"),
            width=3,
            height=1,

            # Button click
            command=lambda r=row, c=column:
                button_clicked(r, c)
        )

        button.grid(
            row=row,
            column=column,
            padx=5,
            pady=5
        )

        button_row.append(button)

    buttons.append(button_row)


# New Game Button
# -----------------------------

new_game_button = tk.Button(
    window,
    text="New Game",
    font=("Arial", 16, "bold"),
    command=new_game
)

new_game_button.pack(
    pady=20
)

# Start Program
window.mainloop()