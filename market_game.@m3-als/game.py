from deck import Deck
from dataclasses import dataclass, field
from typing import List
from card import Card, create_card


@dataclass
class MarketGame:
    num_players: int
    players: List[List[Card]] = field(init=False)
    market: List[Card] = field(default_factory=list)
    draw_pile: Deck = field(default_factory=Deck)

    def __post_init__(self):
        self.players = [[] for _ in range(self.num_players)]

    def deal_cards(self):
        self.draw_pile.shuffle()
        for _ in range(25):
            for player in self.players:
                card = self.draw_pile.draw()
                if card:
                    player.append(card)

    def play_turn(self) -> bool:
        if len(self.market) == 0:
            market_card = self.draw_pile.draw()
            if market_card:
                self.market.append(market_card)
                print(f"-------------------------------------//  بدأت اللعبة !!!  \\\----------------------------------")
                
                print(f"بطاقة السوق:( {market_card} )")

        for player_index in range(self.num_players):
            current_player_cards = self.players[player_index]
            print(f"عدد بطاقات اللاعب ({player_index + 1}): {len(current_player_cards)}")
            input(f"اللاعب {player_index + 1} ، اضغط Enter للعب...")

            if current_player_cards:
                drawn_card = current_player_cards.pop(0)
                print(f"اللاعب ( {player_index + 1} ) -- يلعب :( {drawn_card} )")
                self.market.append(drawn_card)

                if len(self.market) > 1 and drawn_card.get_rank == self.market[-2].get_rank:
                    print(f"------------------  اللاعب ({player_index + 1}) يطابق البطاقة! ----------------------")
                    num_collected = len(self.market)
                    self.collect_market_cards(player_index, drawn_card)
                    print(f"-------------- تمت اضافه :({num_collected - 1}) بطاقات للاعب :({player_index + 1}) -------------- ")
                else:
                    num_collected = len(self.market)
                    print(f" ----- لايوجد تطابق , عدد بطاقات السوق :({num_collected}) ---- ")

                    
            if not current_player_cards:
                print(f"اللاعب {player_index +2} ليس لديه بطاقات! اللاعب {3 - player_index} يفوز!")
                return True 

        return False
    

    def collect_market_cards(self, player_index: int, drawn_card: Card ):
        self.players[player_index].extend(self.market)
        self.market.clear()
        self.market.append(drawn_card)
        
        
        
        
        
        

    def start_game(self):
        self.deal_cards()
        while True:
            if self.play_turn():
                break
        self.end_game()

    def end_game(self):
        for i, player in enumerate(self.players):
            print(f"اللاعب {i + 1} لديه {len(player)} بطاقات.")
        print("انتهت اللعبة!")
        print(f"-------------------------------------//  تصميم واعداد /ENG. Mohammed Al-Sohole.  \\\----------------------------------")


# تشغيل وإعداد اللعبة مع تحديد عدد اللاعبين
if __name__ == "__main__":
    num_players = 2
    game = MarketGame(num_players)
    game.start_game()
