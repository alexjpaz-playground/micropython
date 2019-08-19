# micropython

## Setup (OSX)

### Install AMPY

```
brew install ampy
```

### Micropython UNIX

```
brew install micropythong
```

### ESP32

1. Install the drivers

https://github.com/espressif/arduino-esp32/issues/1084
https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers

#### AMPY

```
export AMPY_PORT=/dev/tty.SLAB_USBtoUART
```

#### REPL

```
screen /dev/tty.SLAB_USBtoUART 115200
```
