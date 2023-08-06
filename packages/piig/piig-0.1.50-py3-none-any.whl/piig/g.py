class GSTATE:
    pass


# state for a single compiation thread, down through macros  etc.
class CSTATE:
    ebss: int
    next_label: int
    stats: list

    def __init__(self):
        self.ebss = 100
        self.next_label = 1000
        self.stats = []


# state through a single function, pushed and poped around calls
class FSTATE:
    pass
