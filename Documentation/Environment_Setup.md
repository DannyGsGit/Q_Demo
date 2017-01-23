# Deep Q Learner in TensorFlow


* Create virtual environment (dqn_demo in this case)

* Install core dependencies
```
$ workon dqn_demo
(dqn_demo) $ pip3 install jupyter-client
(dqn_demo) $ pip3 install ipykernel
(dqn_demo) $ pip3 install numpy
(dqn_demo) $ pip3 install scipy
(dqn_demo) $ pip3 install pandas
(dqn_demo) $ pip3 install matplotlib
```

* Install OpenCV with Python 3 bindings ([Reference](http://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/)).


* Install TensorFlow Python bindings
```
(dqn_demo) $ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.0rc0-cp34-cp34m-linux_x86_64.whl
(dqn_demo) $ pip3 install --upgrade $TF_BINARY_URL
```
* Install the Arcade Learning Library (ALE). First, install dependencies for ALE:
```
(dqn_demo) $ sudo apt-get install libsdl-gfx1.2-dev libsdl-image1.2-dev libsdl1.2-dev cmake
```
Get ALE from Git repo and pip install:
```
(dqn_demo) $ git clone https://github.com/mgbellemare/Arcade-Learning-Environment.git
(dqn_demo) $ cd Arcade-Learning-Environment
(dqn_demo) $ cmake -DUSE_SDL=ON -DUSE_RLGLUE=OFF -DBUILD_EXAMPLES=ON .
(dqn_demo) $ make -j4
(dqn_demo) $ sudo make install
(dqn_demo) $ sudo -H pip3 install .
```
Add a symlink to ALE in the virtual environment:
```
(dqn_demo) $ ln -s ~/Python34/Frameworks/Arcade-Learning-Environment/ale_python_interface ~/.virtualenvs/dqn_demo/lib/python3.4/site-packages
```
Test that ALE is installed properly:
```
(dqn_demo) $ python3
>>> from ale_python_interface import ALEInterface
```
If the command does not produce an *error*, ALE is installed properly.
