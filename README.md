# Deep Q Learner in TensorFlow


* Create virtual environment
* Install core dependencies
```
$ cd ~/Python34/Environments/dqn_demo/bin/
$ source activate
(dqn_demo) $ pip3 install jupyter-client
(dqn_demo) $ pip3 install ipykernel
(dqn_demo) $ pip3 install numpy
(dqn_demo) $ pip3 install scipy
(dqn_demo) $ pip3 install pandas
(dqn_demo) $ pip3 install matplotlib
(dqn_demo) $ pip3 install blosc
```
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
(dqn_demo) $ sudo pip3 install .
```
* Install OpenCV ([Reference](http://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/)).
  * First, setup the OS environment:
```
$ sudo apt-get install build-essential cmake git pkg-config
$ sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
$ sudo apt-get install libgtk2.0-dev
$ sudo apt-get install libatlas-base-dev gfortran
```
  * Next, setup Python OCV libraries (adjust for current OCV version, 3.2.0 at time of writing):
  ```
  $ cd ~
$ git clone https://github.com/Itseez/opencv.git
$ cd opencv
$ git checkout 3.2.0
  ```
  ```
  $ cd ~
$ git clone https://github.com/Itseez/opencv_contrib.git
$ cd opencv_contrib
$ git checkout 3.2.0
```
```
$ cd ~/opencv
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=OFF \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D BUILD_EXAMPLES=ON ..
  ```
Run the compiler. "4" sets the number of cores to use for compilation, adjust to an appropriate number for your CPU:
```
$ make -j4
```
Install OCV:
```
$ sudo make install
$ sudo ldconfig
```
Symlink OCV into our venv:
