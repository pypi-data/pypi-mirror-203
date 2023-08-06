from operator import mul, add
from itertools import starmap

from pymem.exception import MemoryReadError

from trainerbase.gameobject import GameInt, GameFloat
from trainerbase.scriptengine import Script


GameNumber = GameInt | GameFloat
Number = int | float
Vector3 = tuple[Number, Number, Number]


class Teleport:
    def __init__(
        self,
        player_x: GameNumber,
        player_y: GameNumber,
        player_z: GameNumber,
        labels: dict[str, Vector3] = None,
        dash_coefficients: Vector3 = (1, 1, 1),
    ):
        self.player_x = player_x
        self.player_y = player_y
        self.player_z = player_z
        self.labels = {} if labels is None else labels

        self.saved_position = None

        self.dash_coefficients = dash_coefficients
        self.previous_position = None
        self.current_position = None
        self.movement_vector = (0, 0, 0)
        self.movement_vector_updater_script = None

    def set_coords(self, x: Number, y: Number, z: Number = 100):
        self.player_x.value = x
        self.player_y.value = y
        self.player_z.value = z

    def get_coords(self):
        return self.player_x.value, self.player_y.value, self.player_z.value

    def goto(self, label: str):
        self.set_coords(*self.labels[label])

    def save_position(self):
        self.saved_position = self.get_coords()

    def restore_saved_position(self) -> bool:
        """
        Returns False if position is not saved else True
        """

        if self.saved_position is None:
            return False

        self.set_coords(*self.saved_position)
        return True

    def update_movement_vector(self):
        try:
            self.current_position = self.get_coords()
        except MemoryReadError:
            return

        if self.previous_position is None:
            self.previous_position = self.current_position
            return

        x1, y1, z1 = self.previous_position
        x2, y2, z2 = self.current_position

        self.movement_vector = (
            x2 - x1,
            y2 - y1,
            z2 - z1,
        )

        self.previous_position = self.current_position

    def dash(self):
        if self.movement_vector is None:
            return

        dash_movement_vector_iter = starmap(mul, zip(self.movement_vector, self.dash_coefficients))
        new_coords = starmap(add, zip(self.get_coords(), dash_movement_vector_iter))

        self.set_coords(*new_coords)

    def create_movement_vector_updater_script(self):
        if self.movement_vector_updater_script == None:
            self.movement_vector_updater_script = Script(self.update_movement_vector, enabled=True)

        return self.movement_vector_updater_script


def regenerate(current_value: GameNumber, max_value: GameNumber, percent: Number, min_value: Number = 1):
    if current_value.value < max_value.value:
        current_value.value += max(round(max_value.value * percent / 100), min_value)
