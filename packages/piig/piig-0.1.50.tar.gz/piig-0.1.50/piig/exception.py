import contextlib
import typing



class ErrorHere(RuntimeError):
    pass


class AllDone(RuntimeError):
    pass


class NothingSimpler(RuntimeError):
    pass


class NotThisWay(RuntimeError):
    pass


class CantBeDone(RuntimeError):
    pass


# def make_ErrorHere(txt):
#     log.debug(f"Raised{g.gctx.where()} {txt}")
#     return ErrorHere(f"{g.gctx.where()} {txt}")


def rErrorHere(txt) -> typing.NoReturn:
    #    log.debug(f"Raised{g.gctx.where()} {txt}")
    raise ErrorHere(f"{txt}")


# for asking for forgiveness rarther than permission.
@contextlib.contextmanager
def try_this():
    try:
        yield
    except (NotThisWay, CantBeDone, TypeError):
        # the usual failures
        pass

    except AttributeError as e:
        # prog errors somethings.
        # comes when ask for attributes in non us types.
        if e.name not in ("opinfo", "precedence", "to_gcode"):
            breakpoint()
            breakpoint()
            raise e
            breakpoint()
        pass


@contextlib.contextmanager
def expect_no_errors():
    try:
        yield
    except Exception as e:
        breakpoint()
        print("bAD ", e)
        print("bAD ", e)
