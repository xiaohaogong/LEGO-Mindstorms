# Technical Issues

PyBricks
- [EV3 Color Sensor Mode Switch Latency](https://github.com/pybricks/support/issues/14)
- [Delay between different Infrared Sensor modes](https://github.com/pybricks/support/issues/62)
- [OSError when using MultiProcessing in PyBricks](https://github.com/pybricks/support/issues/80)

EV3Dev
- [LEGO EV3 UART sensors return stale values after mode switch](https://github.com/ev3dev/ev3dev/issues/1401)
- [`ValueError: invalid literal for int() with base 10: ''` when using InfraredSensor in Threading](https://github.com/ev3dev/ev3dev-lang-python/issues/746)
  - similar: [GyroSensor angle for GYRO-ANG sometimes returns empty string instead of integer](https://github.com/ev3dev/ev3dev/issues/1269)
  - related: [Device objects not thread safe](https://github.com/ev3dev/ev3dev-lang-python/issues/704)
  - possibly related: [sensors stop working](https://github.com/ev3dev/ev3dev/issues/1083)
- [Threading error when 2 Threads may control the same Motor. Errors encountered in EV3Dev2 with different error messages on MicroPython vs Python3. No such errors encountered in EV3Dev(1) and PyBricks.](https://github.com/ev3dev/ev3dev-lang-python/issues/750)
  - related: [OSError exception [Errno 4] EINTR when running motors in EV3](https://github.com/ev3dev/ev3dev-lang-python/issues/727)
    - related: [MicroPython: implement PEP 475](https://github.com/micropython/micropython/pull/5723)

MicroPython
- [Multiple-Inheritance Issues](https://github.com/micropython/micropython/search?q=%22multiple+inheritance%22&state=open&type=Issues)
  - [Differences vs. CPython](https://docs.micropython.org/en/latest/genrst/core_language.html#classes)


## Resolved

EV3Dev
- [Difference between stopping the program with EV3 Brick's physical Back/Stop button vs. stopping by VSCode stop button](https://github.com/ev3dev/vscode-ev3dev-browser/issues/103)
  - related: [Sometimes not all child processes are ended by `conrun-kill`](https://github.com/ev3dev/ev3dev/issues/1422)
