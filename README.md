# Deep Q Learner in TensorFlow


* Create virtual environment
* Install core dependencies
```
$ cd ~/Python34/Environments/dqn_demo/bin/
$ source activate
(dqn_demo) $ pip3 install jupyter-client
(dqn_demo) $ pip3 install ipykernel
(dqn_demo) $ pip3 install numpy
(dqn_demo) $ pip3 install pandas
(dqn_demo) $ pip3 install matplotlib
(dqn_demo) $ pip3 install blosc
```
* Install TensorFlow Python bindings
```
(dqn_demo) $ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.0rc0-cp34-cp34m-linux_x86_64.whl
(dqn_demo) $ pip3 install --upgrade $TF_BINARY_URL
```
* Install the Arcade Learning Library (ALE)
```
sudo apt-get install libsdl-gfx1.2-dev libsdl-image1.2-dev libsdl1.2-dev cmake
```
```
git clone https://github.com/mgbellemare/Arcade-Learning-Environment.git
cd Arcade-Learning-Environment
cmake -DUSE_SDL=ON -DUSE_RLGLUE=OFF -DBUILD_EXAMPLES=ON
make -j 4
sudo make install
sudo pip3 install .
```
* Install
