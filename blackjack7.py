<<<<<<<< HEAD:blackjack7.py
import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import pygame
========
def importblackjack_Game():
 import tkinter as tk
 from tkinter import messagebox
 import random
 from PIL import Image, ImageTk
>>>>>>>> fe8760b3c723072b061b0eb69bebc4212e9f3f4e:Blackjack.py

 def create_deck():
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

 def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for rank, suit in hand:
        if rank in ['jack', 'queen', 'king']:
            value += 10
        elif rank == 'ace':
            num_aces += 1
            value += 11
        else:
            value += int(rank)
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

 def is_blackjack(hand):
    return calculate_hand_value(hand) == 21

 def is_bust(hand):
    return calculate_hand_value(hand) > 21

 def deal_card(deck):
    return deck.pop()

 class BlackjackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")
        self.root.geometry("800x600")

        pygame.mixer.init()  # Initialize the mixer module for sound effects

        self.deck = create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_balance = 1000
        self.bet = 0

        self.card_images = self.load_card_images()
        self.create_widgets()
        self.start_new_game()

        self.play_background_music()  # Play background music

    def load_card_images(self):
        card_images = {}
        for suit in ['spades', 'hearts', 'diamonds', 'clubs']:
            for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']:
                image = Image.open(f'cards/{rank}_of_{suit}.jpg').resize((80, 120))  # Resize images to 80x120 pixels
                card_images[(rank, suit)] = ImageTk.PhotoImage(image)
        card_images['back'] = ImageTk.PhotoImage(Image.open('cards/back.jpg').resize((80, 120)))  # Resize the back image
        return card_images

    def create_widgets(self):
        # Load and set the background image
        self.bg_image = Image.open('cards/table.jpg')
        self.bg_image = self.bg_image.resize((800, 600), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.background_label = tk.Label(self.root, image=self.bg_photo)
        self.background_label.place(relwidth=1, relheight=1)

        # Load the player avatar
        self.avatar_image = Image.open('cards/avatar.png').resize((100, 100), Image.LANCZOS)
        self.avatar_photo = ImageTk.PhotoImage(self.avatar_image)

        avatar_frame = tk.Frame(self.root, bg="green")
        avatar_frame.pack(pady=10)

        self.avatar_label = tk.Label(avatar_frame, image=self.avatar_photo, bg="green")
        self.avatar_label.pack()

        self.balance_label = tk.Label(avatar_frame, text=f"Balance: ${self.player_balance}", font=("Helvetica", 18), bg="green", fg="white")
        self.balance_label.pack(pady=10)

        top_frame = tk.Frame(self.root, bg="green")
        top_frame.pack(pady=10)

        button_style = {"font": ("Helvetica", 14), "bg": "darkred", "fg": "white", "borderwidth": 2, "relief": "raised"}

        self.reset_button = tk.Button(top_frame, text="Reset", command=self.reset_game, **button_style)
        self.reset_button.pack(side=tk.RIGHT, padx=10)

        bet_frame = tk.Frame(self.root, bg="green")
        bet_frame.pack(pady=10)

        self.bet_label = tk.Label(bet_frame, text="Bet: $", font=("Helvetica", 18), bg="green", fg="white")
        self.bet_label.pack(side=tk.LEFT)

        self.bet_entry = tk.Entry(bet_frame, font=("Helvetica", 14))
        self.bet_entry.pack(side=tk.LEFT, padx=10)

        self.deal_button = tk.Button(bet_frame, text="Deal", command=self.deal, **button_style)
        self.deal_button.pack(side=tk.LEFT, padx=10)

        action_frame = tk.Frame(self.root, bg="green")
        action_frame.pack(pady=10)

        self.hit_button = tk.Button(action_frame, text="Hit", command=self.hit, state=tk.DISABLED, **button_style)
        self.hit_button.pack(side=tk.LEFT, padx=10)

        self.stand_button = tk.Button(action_frame, text="Stand", command=self.stand, state=tk.DISABLED, **button_style)
        self.stand_button.pack(side=tk.LEFT, padx=10)

        self.player_label = tk.Label(self.root, text="Player's Hand: (Value: 0)", font=("Helvetica", 18), bg="green", fg="white")
        self.player_label.pack(pady=10)

        self.player_cards_frame = tk.Frame(self.root, bg="green")
        self.player_cards_frame.pack(pady=10)

        self.dealer_label = tk.Label(self.root, text="Dealer's Hand: (Value: 0)", font=("Helvetica", 18), bg="green", fg="white")
        self.dealer_label.pack(pady=10)

        self.dealer_cards_frame = tk.Frame(self.root, bg="green")
        self.dealer_cards_frame.pack(pady=10)

    def reset_game(self):
        self.player_balance = 1000
        self.balance_label.config(text=f"Balance: ${self.player_balance}")
        self.start_new_game()

    def start_new_game(self):
        self.deck = create_deck()
        self.player_hand = []
        self.dealer_hand = []

        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.deal_button.config(state=tk.NORMAL)

        self.clear_hand_labels()

    def clear_hand_labels(self):
        for widget in self.player_cards_frame.winfo_children():
            widget.destroy()
        for widget in self.dealer_cards_frame.winfo_children():
            widget.destroy()

    def deal(self):
        try:
            self.bet = int(self.bet_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Bet", "Please enter a valid bet amount.")
            return

        if self.bet > self.player_balance or self.bet <= 0:
            messagebox.showerror("Invalid Bet", "Please enter a bet within your balance.")
            return

        self.deal_button.config(state=tk.DISABLED)
        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)

        self.deal_card_animation('player', 2, self.player_hand)
        self.deal_card_animation('dealer', 2, self.dealer_hand, initial=True)

    def deal_card_animation(self, player, num_cards, hand, initial=False):
        if num_cards == 0:
            self.update_hand_labels(initial)
            if player == 'player' and is_blackjack(self.player_hand):
                self.player_balance += int(self.bet * 1.5)
                self.play_win_sound()
                self.end_round("Player has blackjack! Player wins!")
            return

        if player == 'player':
            hand.append(deal_card(self.deck))
            self.update_hand_labels()
        elif player == 'dealer':
            hand.append(deal_card(self.deck))
            self.update_hand_labels(initial)

        self.root.after(500, self.deal_card_animation, player, num_cards - 1, hand, initial)

    def hit(self):
        self.player_hand.append(deal_card(self.deck))
        self.update_hand_labels()
        if is_bust(self.player_hand):
            self.player_balance -= self.bet
            self.end_round("Player busts! Dealer wins.")

    def stand(self):
        while calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(deal_card(self.deck))
        self.update_hand_labels()
        if is_bust(self.dealer_hand):
            self.player_balance += self.bet
            self.play_win_sound()
            self.end_round("Dealer busts! Player wins!")
        else:
            self.determine_winner()

    def determine_winner(self):
        player_value = calculate_hand_value(self.player_hand)
        dealer_value = calculate_hand_value(self.dealer_hand)
        if player_value > dealer_value:
            self.player_balance += self.bet
            self.play_win_sound()
            self.end_round("Player wins!")
        elif player_value < dealer_value:
            self.player_balance -= self.bet
            self.end_round("Dealer wins!")
        else:
            self.end_round("It's a tie!")

    def update_hand_labels(self, initial=False):
        self.clear_hand_labels()

        for card in self.player_hand:
            card_label = tk.Label(self.player_cards_frame, image=self.card_images[card], bg="green")
            card_label.pack(side=tk.LEFT, padx=5)

        for i, card in enumerate(self.dealer_hand):
            if initial and i == 1:
                card_label = tk.Label(self.dealer_cards_frame, image=self.card_images['back'], bg="green")
            else:
                card_label = tk.Label(self.dealer_cards_frame, image=self.card_images[card], bg="green")
            card_label.pack(side=tk.LEFT, padx=5)

        self.player_label.config(text=f"Player's Hand: (Value: {calculate_hand_value(self.player_hand)})")
        self.dealer_label.config(text=f"Dealer's Hand: (Value: {calculate_hand_value(self.dealer_hand) if not initial else '??'})")

    def end_round(self, result):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.deal_button.config(state=tk.NORMAL)
        self.balance_label.config(text=f"Balance: ${self.player_balance}")
        self.update_hand_labels()  # Reveal dealer's hand value
        messagebox.showinfo("Round Over", result)
        self.start_new_game()

<<<<<<<< HEAD:blackjack7.py
    def play_win_sound(self):
        pygame.mixer.music.load("sounds/win.mp3")
        pygame.mixer.music.play()

    def play_background_music(self):
        pygame.mixer.music.load("sounds/music.mp3")
        pygame.mixer.music.play(-1)  # Loop the music indefinitely

if __name__ == "__main__":
========
 if __name__ == "__main__":
>>>>>>>> fe8760b3c723072b061b0eb69bebc4212e9f3f4e:Blackjack.py
    root = tk.Tk()
    game = BlackjackGame(root)
    root.mainloop()
