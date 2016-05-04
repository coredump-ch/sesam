//! Open the hackerspace door via GPIO pin 17.
//!
//! For this to work, the GPIO driver needs to be loaded and the necessary
//! write permissions on the sysfs are required.

extern crate sysfs_gpio;

use std::time::Duration;
use std::thread::sleep;
use std::process::exit;

use sysfs_gpio::{Direction, Pin};
use sysfs_gpio::Result as GpioResult;

const GPIO_PIN: u64 = 17;
const OPEN_SECONDS: u64 = 5;


fn open_door(gpio_pin: u64) -> GpioResult<()> {
    let pin = Pin::new(gpio_pin);
    pin.with_exported(|| {
        try!(pin.set_direction(Direction::Out));
        try!(pin.set_value(1));
        sleep(Duration::from_secs(OPEN_SECONDS));
        try!(pin.set_value(0));
        Ok(())
    })
}


fn main() {
    println!("Opening door on GPIO {} for {} seconds...", GPIO_PIN, OPEN_SECONDS);
    open_door(GPIO_PIN).unwrap_or_else(|e| {
        println!("Opening failed: {:?}", e);
        exit(1);
    });
    println!("Done!");
}
