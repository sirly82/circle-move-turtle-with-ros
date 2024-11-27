# CREATE CIRCLE MOVE TURTLE WITH ROS

# Create New Package
```
$ cd ~/catkin_ws/src
$ catkin_create_pkg turtlesim_circle rospy geometry_msgs std_msgs
```

If done, change to the turtlesim_circle directory
```
$ cd turtlesim_circle
```

# Clone This Repository
```
$ mkdir scripts
$ git clone https://github.com/sirly82/circle-move-turtle-with-ros.git
```

# Replace The File
```
$ cd circle-move-turtle-with-ros
$ mv circle_turtle.py scripts
$ cd ..
```

# Giving Access
```
$ chmod +x scripts/circle_turtle.py
```
# Before Runing The Program BELOW
Open other terminal first, run this code
```
$ roscore
```
Just let the terminal runing, don't close it and open other terminal
```
$ rosrun turtlesim turtlesim_node
```

# Run
Open the first terminal, then follow the instruction BELOW
```
$ cd ~/catkin_ws
$ source devel/setup.bash
$ rosrun turtlesim_circle circle_turtle.py
```


