from layers.biwEngine.boardEngine.chess_board.chess_basic_space import ChessSpace
from layers.baseGame.boardEngine.board_logic import BoardLogic
from layers.baseGame.boardEngine.board_space import BoardSpace
from layers.baseGame.gameCharacter.game_character import GameCharacter
from layers.baseGame.game_event import GameEvent
from layers.baseGame.game_extension import GameExtension
from layers.baseGame.game_item import GameItem

class ChessBoard(BoardLogic):
    _id: str
    spaces: [BoardSpace]
    items: [GameItem]
    characters: [GameCharacter]
    events: [GameEvent]
    extensions: [GameExtension]

    def __init__(self, _id: str = None):
        if _id is None:
            self.create_board()
        else:
            self.load_board(_id=_id)

    def board_importer(self, json_board):
        import json
        board_data = json.load(json_board)

        self.spaces = [ChessSpace().space_importer(space_data=space) for space in
                       board_data.get("spaces", None)]
        self.items = [ChessSpace().space_importer(item_data=item) for item in board_data.get("items", None)]
        self.characters = [(character_data=character) for character in board_data.get("characters", None)]
        self.events = [(event_data=event) for event in board_data.get("events", None)]
        self.extensions = [(extension_data=extension) for extension in board_data.get("extensions", None)]

    def create_board(self):
        # TODO: Add items, characters and extensions logic here
        pass
        # TODO: Add id and db handling here
        pass

    def load_board(self, _id: str = None):
        # TODO: Check if id is valid or not
        pass

    def save_board(self):
        # TODO: Check if everything is fine before and after save
        pass
