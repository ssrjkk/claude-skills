---
name: rust-embedded
description: "Rust for embedded systems"
category: embedded
tags: [rust, embedded, microcontroller, no-std, arm, risc-v]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Rust Embedded

> Develop embedded systems firmware with Rust for safety, performance, and modern tooling.

## Quick Start
```rust
//! Blinky example for STM32 microcontroller
#![no_std]
#![no_main]

use cortex_m_rt::entry;
use panic_halt as _;
use stm32f4xx_hal::{
    pac,
    prelude::*,
    timer::Timer,
};
use embedded_hal::digital::OutputPin;

#[entry]
fn main() -> ! {
    // Get peripherals
    let dp = pac::Peripherals::take().unwrap();
    let cp = cortex_m::Peripherals::take().unwrap();

    // Configure clocks
    let rcc = dp.RCC.constrain();
    let clocks = rcc.cfgr.sysclk(48.MHz()).freeze();

    // Configure LED pin (PC13 on many STM32 boards)
    let gpioc = dp.GPIOC.split();
    let mut led = gpioc.pc13.into_push_pull_output();

    // Configure timer
    let mut timer = Timer::syst(cp.SYST, 1.Hz(), &clocks);

    // Blink loop
    loop {
        led.set_high().unwrap();
        timer.wait(); // 1 second delay
        led.set_low().unwrap();
        timer.wait();
    }
}
```

```toml
# .cargo/config.toml — Cross-compilation target
[target.thumbv7em-none-eabihf]
runner = "gdb-multiarch"
rustflags = ["-C", "link-arg=-Tlink.x", "-C", "linker=arm-none-eabi-gcc"]

[build]
target = "thumbv7em-none-eabihf"
```

```rust
// Embedded HAL traits — abstraction for portability
use embedded_hal::{
    blocking::delay::DelayMs,
    digital::OutputPin,
    spi::SpiDevice,
};

fn control_display<D: DelayMs<u32>, P: OutputPin>(
    delay: &mut D,
    reset: &mut P,
) {
    reset.set_low().unwrap();
    delay.delay_ms(10);
    reset.set_high().unwrap();
    delay.delay_ms(100);
}
```

## Key Concepts
`#![no_std]` enables bare-metal code without the standard library. The Embedded HAL provides portable hardware abstraction. `cortex-m-rt` handles vector table and startup. Use probe-rs for flashing and debugging.

## When to Use
- Firmware for ARM Cortex-M, RISC-V microcontrollers
- IoT sensor nodes and actuators
- Safety-critical embedded systems
- Replacing C/C++ with memory-safe Rust

## Validation
1. `cargo build --target thumbv7em-none-eabihf` compiles without std
2. Firmware flashes to device and runs (LED blinks)
3. UART/sensor output matches expected values
4. Binary size fits within target flash memory
