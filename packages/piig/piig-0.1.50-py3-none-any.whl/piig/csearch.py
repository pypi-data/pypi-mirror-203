import piig as G


class SearchConstraint:
    # position roughly center above start of search.
    above: G.Gvalue
    # min size of thing to look for.

    amin: G.Gvalue
    # max size to search in one dimension for the thing
    # to probe.  G.RVALnstains max size of things measured.
    amax: G.Gvalue

    # when measuring z, how far to
    # move from an xy edge inwards to work it out.
    indent: G.Gvalue

    # steps between probes

    delta: G.Gvalue
    # safe distance above probed z surface to move
    skim_distance: G.Gvalue

    # how far to backoff before probing slowly
    backoff: G.Gvalue

    # how far to look down for a surface once we've
    # already located the rough z0
    search_depth: G.Gvalue
    # how far to look down and not found is a not there
    #
    found_if_below: G.Gvalue

    # to work out when there's a probe hit,
    # say probe from z.. 0,   then any stop < iota
    # is taken as a miss.
    iota: G.Gvalue

    def __init__(
        self,
        above=None,
        amax=None,
        indent=None,
        amin=None,
        delta=None,
        skim_distance=None,
        backoff=None,
        search_depth=None,
        found_if_below=None,
        iota=None,
    ):
        super().__init__()
        if amin is None:
            amin = amax * 0.5

        if search_depth is None:
            search_depth = G.Const(-0.1)

        if found_if_below is None:
            found_if_below = search_depth * 0.5

        if backoff is None:
            backoff = G.Const(x=0.1, y=0.1, z=0.1)

        if indent is None:
            indent = round(amax * 0.1, 1)

        if delta is None:
            delta = G.Const(x=1.5, y=1.5, z=1.5)

        if skim_distance is None:
            skim_distance = G.Const(0.3)

        if iota is None:
            iota = G.Const(x=0.025, y=0.025, z=0.025)

        self.iota = iota
        self.delta = delta

        self.amin = amin
        self.indent = indent
        self.amax = amax

        print(self.amin.xy + 3)
        self.above = above
        self.skim_distance = skim_distance
        self.backoff = backoff
        self.search_depth = search_depth
        self.found_if_below = found_if_below

    def __repr__(self):
        return f"{self.above} {self.amin}  {self.amax} {self.indent}"

    @property
    def comment(self):
        return [
            "Search Constraints:",
            "start:",
            f"  {self.above}",
            "boundary:",
            f"  x= (-{(self.amax[0] * 0.5)}..-{(self.amin[0] * 0.5)})",
            f"..({(self.amin[0] * 0.5)}..{(self.amax[0] * 0.5)})",
            f"  y= (-{(self.amax[1] * 0.5)}..-{(self.amin[1] * 0.5)})",
            f"..({(self.amin[1] * 0.5)}..{(self.amax[1] * 0.5)})",
            f"  z= ({(-self.amax[2])}..{(-self.amin[2])})",
            "indent:",
            f"  {self.indent}",
            "delta:",
            f"  {self.delta}",
        ]
