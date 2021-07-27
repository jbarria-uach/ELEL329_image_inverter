#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image

frame_counter = 0


def on_new_image(image):
    global frame_counter
    frame_counter += 1
    rospy.loginfo_throttle(1, f"New image received of type: {type(image)}, "
                              f"Received frames: {frame_counter}")


def process_frames():
    rospy.init_node('elel329_image_inverter')
    rospy.Subscriber("rpi_usb_cam/image_raw", Image, on_new_image)
    rospy.spin()


if __name__ == '__main__':
    process_frames()
