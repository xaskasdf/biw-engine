from layers.baseGame.boardEngine.board_space import BoardSpace
from layers.baseGame.gameError.game_error import GameError


class ChessSpace(BoardSpace):
    invoker = "ChessSpace"
    _id: any = None
    x_axis_pos = float
    y_axis_pos = float
    z_axis_pos = float
    # Collision is not allowed by default since spaces should be unique, but who knows, maybe allowing to fuck up
    # things could provide new mechanixs  ;*
    collision_allow = False
    item_allow = True
    character_allow = True
    event_allow = True

    def __init__(self, _id: str = None, ref_id: str = None):
        if _id is None:
            if ref_id is not None:
                self.create_board_space(ref_id=ref_id)
            else:
                raise GameError(
                    invoker=self.invoker,
                    invoker_code=self.invoker_code,
                    message="Can't create a board space with no reference.",
                    code=3,
                    data=self,
                )
        else:
            self.load_board_space(_id=_id)

    def space_importer(self, space_data: any = None):
        return self

    def create_board_space(self, ref_id: str = None):
        if ref_id == "testCreateVTK":
            return "caca"

    def load_board_space(self, _id: any = None):
        return _id
