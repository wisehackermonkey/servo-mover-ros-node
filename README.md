# servo-mover-ros-node
----
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<!-- <img src="assets/NNNNNNNNNNNNN" width="400"> -->
<h2 align="center">creates a simple ros node that controls two hoby servo motor's from a arduino</h2>

<!-- <h4 align="center">________________________</h4> -->


# Quick start
### __________________
<!-- 
##### __________________________
```bash
``` 
-->

# Summary
<!-- ### -  *[Quick start](#Quick-start)*
### -  *[Installation](#Installation)*
### -  *[For developers](#For-developers)* -->
### -  *[Contributors](#Contributors)*
### -  *[License](#License)*




<!-- # Installation
```bash
```
 -->
<!-- ----------------- -->
<!-- # Screenshots -->
<!-- - <img src="assets/_____________" width="400">  -->
<!-- -  -->



<!-- SETUP -->
-----------------
# For developers
### 
```bash
 180  curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
  181  cd bin/
  182  ls
  183  arduino-cli
  184  export PATH="$HOME/bin:$PATH"
  185  arduino-cli
  186  cd ~/github/
  187  ls
  188  cd servo-mover-ros-node/
  189  ls
  190  arduino-cli config init
  191  cd arduino/
  192  arduino-cli sketch new Servo_control_v1
  193* /
  194  ls
  195  arduino-cli sketch new ServoControl_v1
  196  arduino-cli sketch new ServoControl_v2
  197  ls
  198  cd ServoControl_v
  199  cd ServoControl_v1
  200  ls
  201  arduino-cli core update-index
  202  arduino-cli board list
  203  arduino-cli board listall arduino:avr:uno
  204  arduino-cli board listall 
  205  arduino-cli core install arduino:avr
  206  arduino-cli board list
  207  arduino-cli board listall 
  208  $ arduino-cli compile --fqbn arduino:samd:mkr1000 MyFirstSketch
  209  arduino-cli compile --fqbn arduino:avr:uno ServoControl_v1.ino 
  210  arduino-cli lib search ServoControl_v1.ino 
  211  arduino-cli lib search Servo
  212  arduino-cli lib search Servo |less
  213  arduino-cli lib search Servo | less
  214  arduino-cli lib search Servo | more
  215  arduino-cli lib search Servo.h
  216  arduino-cli compile --fqbn arduino:avr:uno ServoControl_v1.ino 
  217  wget https://peppe8o.com/download/arduino_lib/Servo.zip
  218  ls
  219  unzip Servo.zip 
  220  ls
  221  arduino-cli compile --fqbn arduino:avr:uno ServoControl_v1.ino 
  222  arduino-cli compile --fqbn arduino:avr:uno hello.ino 
  223  cd ..
  224  arduino-cli compile --fqbn arduino:avr:uno hello
  225* arduino-cli config dump[B
  226  history
  227  arduino-cli compile --fqbn arduino:avr:uno hello
  228  arduino-cli compile --fqbn arduino:avr:uno ServoControl_v1
  229  arduino-cli lib search ros
  230  arduino-cli lib search ros serial
  231  arduino-cli lib search rosserial
  232  arduino lib install rosserial@0.7.9
  233  arduino-cli lib install rosserial@0.7.9
  234  arduino-cli lib install "Rosserial Arduino Library"@0.7.9
  235  ls
  236  arduino-cli compile --fqbn arduino:avr:uno ServoControl_v1
  237  history
```
### 
```bash
roscore -v
rostopic 
```
### setup ros node
```bash


cd ~/catkin_ws/src
catkin_create_pkg servo-mover-ros-node rospy std_msgs
cd ~/catkin_ws
catkin_make
source devel/setup.bash
rospack profile
roscd servo-mover-ros-node
mkdir scripts

roscd servo-mover-ros-node/scripts
touch servo_control.py
chmod +x servo_control.py
```
### install rosserial-arduino
```bash
sudo apt-get install ros-noetic-rosserial-arduino
sudo apt-get install ros-noetic-rosserial
```

```bash
rosrun  servo-mover-ros-node servo_control.py
ERROR : 

```
### fix error
#### "CMakeLists.txt"
```cmake
catkin_install_python(PROGRAMS scripts/servo_control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

### Window 1
```bash
cd ~/catkin_ws
catkin_make
rosrun  servo-mover-ros-node servo_control.py
```

### Window 2
```bash
rostopic list
----------------
ubuntu@reachy:~/catkin_ws$ rostopic list
/head_servo_position
/rosout
/rosout_agg
----------------
rostopic echo /head_servo_position
```
```bash
cd ~/github/servo-mover-ros-node/arduino/

```
-----------------
# Contributors

[![](https://contrib.rocks/image?repo=wisehackermonkey/servo-mover-ros-node)](https://github.com/wisehackermonkey/servo-mover-ros-node/graphs/contributors)

##### Made with [contributors-img](https://contrib.rocks).

-----------------
# License
#### MIT © wisehackermonkey
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
```bash
by oran collins
github.com/wisehackermonkey
oranbusiness@gmail.com
______________________
```

git config --global user.name "wisehackermonkey"
git config --global user.email oranbusiness@gmail.com














<!-- ---------------------------------- -->
<!-- FULL -->
<!-- ---------------------------------- -->

<!-- # servo-mover-ros-node -->
<!-- ---- -->
<!-- 
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<img src="assets/NNNNNNNNNNNNN" width="400">
<h2 align="center">____________________</h2>
<h4 align="center">________________________</h4>
 -->

<!-- 

# Quick start
### __________________
##### __________________________
```bash
```

 -->


<!-- 

# Summary
### -  *[Quick start](#Quick-start)*
### -  *[Live Demo](#Live-demo)*
### -  *[Installation](#Installation)*
### -  *[Screenshots](#Screenshots)*
### -  *[License](#License)*
### -  *[Features](#Features)*
### -  *[For developers](#For-developers)*
### -  *[Todo](#TODO)*
### -  *[Related](#Related)*
### -  *[Contributors](#Contributors)*
 -->



<!-- ----------------- -->
<!-- <img src="assets/KKKKKKKKKKK" width="400"> -->
<!-- # [Live Demo](https://www._____________.com) -->





<!-- 
# Installation
### 
```bash
``` 
-->




<!-- 

-----------------
# Screenshots
- <img src="assets/_____________" width="400"> 
- 
-->



<!-- 

# Features
- [x] ______
- [ ] ______

-->


<!-- 
-----------------
# For developers
### 
```bash
```
 -->





<!-- -----------------
# TODO
- [x] ___________
- [ ] ___________ 
-->

<!-- 
-----------------
# Built with
- #### ________________
-->





<!-- -----------------
# Related 
### [_________](https://www.____________.com)
 -->





<!-- 
-----------------
# Contributors

[![](https://contrib.rocks/image?repo=wisehackermonkey/servo-mover-ros-node)](https://github.com/wisehackermonkey/servo-mover-ros-node/graphs/contributors)

##### Made with [contributors-img](https://contrib.rocks).

-----------------
# License
#### MIT © wisehackermonkey
[![MIT](https://img.shields.io/github/license/wisehackermonkey/servo-mover-ros-node.svg)](https://github.com/wisehackermonkey/servo-mover-ros-node/blob/master/LICENSE)
-->

<!-- 
```bash
by oran collins
github.com/wisehackermonkey
oranbusiness@gmail.com
______________________
``` 
-->

<!-- ---------------------------------- -->
<!-- EXTRAS -->
<!-- ----------------------------------- -->
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<!-- 
[![Javascript](https://img.shields.io/badge/Javascript-Enabled-lightgreen.svg)](https://shields.io/) 
[![forthebadge made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![Python](https://img.shields.io/badge/Python-Enabled-<COLOR>.svg)
![P5.js](https://img.shields.io/badge/P5.js-Enabled-pink.svg)
[![Generic badge](https://img.shields.io/badge/<SUBJECT>-<STATUS>-<COLOR>.svg)](https://shields.io/)
[![GitHub release](https://img.shields.io/github/release/wisehackermonkey/servo-mover-ros-node.svg)](https://GitHub.com/wisehackermonkey/servo-mover-ros-node/releases/)
[![GitHub tag](https://img.shields.io/github/tag/wisehackermonkey/servo-mover-ros-node.svg)](https://GitHub.com/wisehackermonkey/servo-mover-ros-node/tags/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/wisehackermonkey/servo-mover-ros-node.svg)](https://GitHub.com/wisehackermonkey/servo-mover-ros-node/pull/)
[![Website perso.crans.org](https://img.shields.io/website-up-down-green-red/http/www.orancollins.com.svg)](http://www.orancollins.com/) 
    -->

<!-- 
# https://yuml.me/diagram/plain/activity/draw
### (start)->[AAAAAAAA]<aaaaa->(BBBBBB)->(end) 

# Diagram
## 
```bash
```
 -->

<!-- 

# List
- 
- 
- 



# Toggle List (NO FORMATTING)
<details><summary>AAAAAAAA</summary>
<details><summary>Hidden A</summary>
</details>
</details>

<details><summary>BBBBBBBBB</summary>
<details><summary>Hidden B</summary>
</details>
</details>

<details><summary>CCCCCCCCC</summary>
</details>



# Toggle list with formatting
<details><summary>Level 1</summary></details>

<details><summary>&emsp;BBBBBBBBB</summary></details>
<details><summary>&emsp;&emsp;CCCCCCCCC</summary></details>
<details><summary>&emsp;&emsp;&emsp;DDDDDDDDD</summary></details>


# Toggle list Nested
<details><summary>Level 1</summary>

<details><summary>&emsp;BBBBBBBBB</summary>
<details><summary>&emsp;&emsp;CCCCCCCCC</summary>
<details><summary>&emsp;&emsp;&emsp;DDDDDDDDD</summary>

</details></details></details></details></details></details></details></details></details></details></details></details></details></details></details></details></details></details>

# Keyboard Commnand
### <kbd>Command/ctrl + R</kbd> 

# Installation
### 
```bash
cd ~
git clone https://github.com/wisehackermonkey/servo-mover-ros-node.git
cd servo-mover-ros-node
pip install -r requirements.txt
npm install
```

# Docker
### Build
```bash
cd ~
git clone https://github.com/wisehackermonkey/servo-mover-ros-node.git
cd servo-mover-ros-node
docker build -t wisehackermonkey/servo-mover-ros-node:latest .  
```
### Run
```bash
docker run -it --rm --name wisehackermonkey/servo-mover-ros-node:latest  
```
### Docker-compose
```bash
docker-compose build
docker-compose up 
```



# Publish Docker Image
```bash
docker build -t wisehackermonkey/servo-mover-ros-node:latest .
docker login
docker push wisehackermonkey/servo-mover-ros-node:latest
```

 -->