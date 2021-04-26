from casino import *

print("Welcome to the Casino Blackjack App")
print("The minimum bet at this table is $20.")


money = int(input("\nHow many money are you willing to play with today: "))

game = Game(money)


playing = True

while playing:

    game_deck = Deck()
    game_deck.build_deck()
    game_deck.shuffle_deck()

    p1 = Player()
    d1 = Dealer()

    game.display_money()
    game.set_bet()

    p1.draw_hand(game_deck)
    d1.draw_hand(game_deck)

    game.disMonBet()

    print(f"The dealer is showing a {d1.hand[0].rank} of {d1.hand[0].suit}")

    while p1.playing_hand:
        p1.dispaly_hand()
        p1.get_hand_value()
        p1.update_hand(game_deck)

    d1.hit(game_deck)
    d1.dispaly_hand()

    game.scoring(p1.hand_value, d1.hand_value)
    game.payout()

    if game.money < 20:
        playing = False
        print("Sorry, you ran out of money...Try Again.")
