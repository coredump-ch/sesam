# opendoor

Small Rust program to open the hackerspace door via GPIO pin 17.

## Building

To just build a regular dev version:

    $ cargo build

If you want to build for production, it's recommended that you build a
statically linked 64bit binary:

    $ rustup target add x86_64-unknown-linux-musl
    $ cargo build --release --target=x86_64-unknown-linux-musl

You can find the binary in `target/x86_64-unknown-linux-musl/release/opendoor`.
Simply copy it to the target system and it should work without any additional
dependencies.
