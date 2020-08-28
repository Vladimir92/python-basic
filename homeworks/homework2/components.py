from dataclasses import dataclass

from homeworks.homework2.exceptions import NegativeParameterError, WheelDriveTypeError


@dataclass
class Engine:
    horses: int

    def __post_init__(self):
        if self.horses < 0:
            raise NegativeParameterError("Engine cannot have negative horsepower", self.horses)

    def get_coef(self):
        return 0.01 * self.horses


@dataclass
class SportEngine(Engine):
    wheel_drive: str
    max_ratio: int

    def __post_init__(self):
        super().__post_init__()
        if self.wheel_drive not in ['full', 'front', 'rear']:
            raise WheelDriveTypeError(self.wheel_drive)
        if self.max_ratio < 0:
            raise NegativeParameterError("Engine must have rpm of positive engine", self.max_ratio)

    def get_race_coef(self):
        wd_coef = 1.1 # front
        if self.wheel_drive == 'full':
            wd_coef = 1.25
        elif self.wheel_drive == 'rear':
            wd_coef = 1.05
        return wd_coef * (0.01 * self.horses) + 0.01 * self.max_ratio


@dataclass
class AvionicEngine(Engine):
    velocity: int
    efficiency: float

    def __post_init__(self):
        super().__post_init__()
        if self.velocity < 0:
            raise NegativeParameterError("Engine must have velocity of positive engine", self.velocity)
        if self.efficiency < 0.1 or self.efficiency > 1:
            raise NegativeParameterError("Engine must have efficiency from 0.1 to 1", self.efficiency)

    def get_fly_coef(self):
        return self.efficiency * (0.01 * self.horses + 0.002 * self.velocity)


@dataclass
class Weaponry:
    missiles: int
    gun_ammo: int
    flares: int

    def __post_init__(self):
        if self.missiles < 0:
            raise NegativeParameterError("Cannot have negative missile amount", self.missiles)
        if self.gun_ammo < 0:
            raise NegativeParameterError("Gun rounds cannot be negative", self.gun_ammo)
        if self.flares < 0:
            raise NegativeParameterError("Flares amount must be positive", self.flares)

    def fight(self, enemies):
        firepower = 10 * self.gun_ammo + 100 * self.missiles + 5 * self.flares
        enemy_firepower = 8000 * enemies
        if firepower > enemy_firepower:
            self.missiles -= enemies
            if self.missiles < 0:
                self.missiles = 0
            self.gun_ammo -= enemies * 100
            if self.gun_ammo < 0:
                self.gun_ammo = 0
            self.flares -= enemies
            if self.flares < 0:
                self.flares = 0
            print(f"Fight won against {enemies} enemies! "
                  f"Remaining {self.missiles} missiles, {self.gun_ammo} ammo, {self.flares} flares.")
            return True
        print(f"Not enough firepower {firepower} to fight {enemies} enemies with {enemy_firepower} firepower. Retreating")
        return False
