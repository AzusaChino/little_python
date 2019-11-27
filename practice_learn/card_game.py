class Card:
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'k']
    SUITS = ['梅', '方', '红', '黑']

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            res = self.suit + self.rank
        else:
            res = "XX"
        return res

    def order(self):
        if self.rank == 'A':
            face_num = 1
        elif self.rank == 'J':
            face_num = 11
        elif self.rank == 'Q':
            face_num = 12
        elif self.rank == 'K':
            face_num = 13
        else:
            face_num = int(self.rank)
