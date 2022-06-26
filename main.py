from tkinter import *
import pandas
import random


# ----------------- Global ----------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "Spanish"

try:
    data = pandas.read_csv("./data/progress.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/spanish.csv")
except pandas.errors.EmptyDataError:
    data = pandas.read_csv("./data/spanish.csv")

cards = data.to_dict(orient="records")
current_card = random.choice(cards)
word_text = current_card.get("Spanish")


# ----------------- FUNCTIONS ----------------- #
def flip_card():
    global flip_button
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_text, text=current_card.get("English"), fill="white")
    canvas.itemconfig(language_text, text="English", fill="white")
    flip_button.place_forget()


def next_card():
    global current_card, word_text, flip_button
    current_card = random.choice(cards)
    word_text = current_card.get(LANGUAGE)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(language_text, text=LANGUAGE, fill="black")
    canvas.itemconfig(card_text, text=word_text, fill="black")
    flip_button.place(x=380, y=375)


def remove_card():
    cards.remove(current_card)
    temp_data = pandas.DataFrame(cards)
    temp_data.to_csv("./data/progress.csv", index=False)
    next_card()


# ----------------- USER INTERFACE ----------------- #
# Master Window
master = Tk()
master.title("Get It Right!")
master.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text=LANGUAGE, font=("Arial", 40, "italic"))
card_text = canvas.create_text(400, 263, text=word_text, font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# ----------------- BUTTONS ----------------- #
# Button Images
green_check = PhotoImage(file="./images/right.png")
red_x = PhotoImage(file="./images/wrong.png")
flip_ico = PhotoImage(file="./images/flip.png")

wrong_button = Button(image=red_x, highlightthickness=0, bg=BACKGROUND_COLOR, border=0, command=next_card)
wrong_button.grid(column=0, row=1, padx=50)
right_button = Button(image=green_check, highlightthickness=0, bg=BACKGROUND_COLOR, border=0, command=remove_card)
right_button.grid(column=1, row=1, padx=50)
flip_button = Button(image=flip_ico, highlightthickness=0, border=0, bg="white", command=flip_card)
flip_button.place(x=380, y=375)


# Keep open until close event
master.mainloop()
