import enum


class ONumbers(enum.IntEnum):
    PROBE_VICE_CENTER = 100
    ALIGNC = enum.auto()
    ROTARY_PROBE_BORE = enum.auto()
    ABOVE_VICE = enum.auto()
    ABOVE_ROTARY = enum.auto()
    PROBE_CALIBRATE = enum.auto()


class Tool(enum.IntEnum):
    PROBE = 1
