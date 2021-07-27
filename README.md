# Image Inverter ROS Package

This ROS Package subscribes to a specific *sensor_msgs/Image* topic to capture frames, flips them vertically and then publishes this "flipped" frame on a new topic.

This was made in the context of an assignment corresponding to the master's course *ELEL329* at Universidad Austral de Chile.

To demonstrate its functionality an [usb_cam launch file](https://github.com/jbarria-uach/ELEL329_cam_src_pub) was created. In this project the camera was connected to a Raspberry Pi 3B and the image inverter node was running on a laptop.

