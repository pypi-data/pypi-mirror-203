try:
    from ._ffi import ffi, lib
except ImportError:
    raise FileNotFoundError("Could not find the library `dittoffi`. \
Did you expose its location using LD_LIBRARY_PATH? \
You can also put it in a system folder such as `/usr/lib`.")

__all__ = ["ffi", "lib"]