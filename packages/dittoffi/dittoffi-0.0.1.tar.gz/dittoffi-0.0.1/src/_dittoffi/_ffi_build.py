import os
import platform
from cffi import FFI
from pathlib import Path
from contextlib import contextmanager
from urllib import request
import asyncio
import itertools

SEARCH_PATH_ENV_VAR = "DITTOFFI_SEARCH_PATH"

LIB_VERSION = "4.0.1"
ffi = FFI()

@contextmanager
def read_header_file(file_path: str):
    """ Helper function to read the headers in the project.

    This function was added due to the specifities of cffi.
    Since this is a special module, it doesn't belong to the
    _dittoffi package officialy and consequently can access the
    header file using `importlib.ressources`.

    Args:
        file_path (_type_): relative path to the header.

    Yields:
        str : content of the header.
    """
    header_path = os.path.join(Path(__file__).parent, file_path)
    file = open(header_path)
    try:
        yield file.read()
    finally:
        file.close

def platform_lib_name() -> str:
    """Generate dynamic lib name."""
    platform_name = platform.system()

    lib_prefix = None
    lib_suffix = None

    if platform_name == "Linux":
        lib_prefix = "lib"
        lib_suffix = "so"
    elif platform_name == "Darwin":
        lib_prefix = "lib"
        lib_suffix = "dylib"
    elif platform_name == "Windows":
        lib_prefix = ""
        lib_suffix = "dll"
    else:
        raise SystemError(f"The platform {platform_name} is not supported yet!")

    lib_name = f"{lib_prefix}dittoffi.{lib_suffix}"

    return lib_name

async def download_libdittoffi(output_path:str, version:str, target:str, lib_name:str):
    url = f"https://software.ditto.live/rust/Ditto/{version}/{target}/release/{lib_name}"
    if dir_contains_file(output_path, lib_name):
        print("Lib already dowloaded!")
        return

    async def pending_download():
        chars = ["|","/", "-", "\\"]
        for pending_char in itertools.cycle(chars):
            print(f"Downloading dittoffi [{pending_char}]", end='\r')
            await asyncio.sleep(0.2)

    def download_url():
        request.urlretrieve(url, f"{output_path}/{lib_name}")

    loop = asyncio.get_event_loop()
    pending = loop.create_task(pending_download())
    download = loop.run_in_executor(None, download_url)
    await download
    pending.cancel()

def dir_contains_file(path:str, lib_name) -> bool:
    for file in os.listdir(path):
        if lib_name in file:
            return True
    return False

# LINKAGE DEPENDING OF ENV VARIABLES
# TODO see rust/build.rs to do similar things
async def find_ditto_path():
    lib_name = platform_lib_name()
    # DITTOFFI_SEARCH_PATH
    path = os.environ.get(SEARCH_PATH_ENV_VAR)
    if path is not None and dir_contains_file(path, lib_name):
        return path

    # TODO : if System lib folders contain dittoffi, return it
    # instead of downloading it, again.
    # Linux : /usr/lib, /usr/local/lib
    # Mac : Linux + /opt/homebrew/lib
    # Windows :
    # C:\Windows\System32
    # PWD
    path = os.environ.get("PWD")
    if path is not None and dir_contains_file(path, lib_name):
        return path

    #TODO : match target architecture
    await download_libdittoffi(path, LIB_VERSION, "x86_64-unknown-linux-gnu", lib_name)
    return path

async def prepare_compilation():
    with read_header_file("dittoffi.cffi") as content:
        ffi.cdef(content)

    with read_header_file("dittoffi.h") as content:
        ffi.set_source("_ffi", content,
            library_dirs = [await find_ditto_path()],
            libraries = ['dittoffi']
        )

asyncio.run(prepare_compilation())

if __name__ == "__main__":
    ffi.compile(verbose=True)
