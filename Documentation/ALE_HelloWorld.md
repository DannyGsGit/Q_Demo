* ALE Introduction

* Startup the virtual environment and open python3
```
$ workon dqn_demo
(dqn_demo) $ python3
```

* Start ALE from within python
```
from ale_python_interface import ALEInterface

ale = ALEInterface()

ale.setInt(b"frame_skip", 4)
ale.loadROM(b"freeway.bin")
```
