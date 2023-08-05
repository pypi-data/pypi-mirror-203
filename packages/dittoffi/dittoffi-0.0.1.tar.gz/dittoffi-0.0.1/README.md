# FFI Module for Ditto.

Need a `libdittoffi.so` in the folder to work atm

Its path must be specified using:
```
export DITTOFFI_SEARCH_PATH=...
export LD_LIBRARY_PATH=...
```

## Update Headers
When the FFI signatures change, the headers inside this directory must be updated.

`dittoffi.h` can be replaced by the same-titled generated file, thanks to safer-ffi.
Use `make build-python` at the root of the project in order to do so.
The `dittoffi.cffi` must be manually updated at the moment. Safer-ffi we generate it
in the future.

Need a `libdittoffi.so` library to work.