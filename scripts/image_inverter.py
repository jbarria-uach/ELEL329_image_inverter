#!/usr/bin/env python
import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

bridge = CvBridge()
publisher = rospy.Publisher('inverted_rpi_usb_cam/image_raw', Image,
                            queue_size=20)
frame_counter = 0


def on_new_image(image):
    global frame_counter
    cv_image = bridge.imgmsg_to_cv2(image, desired_encoding="bgr8")
    cv_image = cv2.flip(cv_image, 0)  # The image is now vertically flipped.
    image_msg = bridge.cv2_to_imgmsg(cv_image, encoding="bgr8")
    publisher.publish(image_msg)
    frame_counter += 1
    rospy.loginfo_throttle(1, f"Number of frames processed: {frame_counter}")


def process_frames():
    rospy.init_node('elel329_image_inverter')
    rospy.Subscriber("rpi_usb_cam/image_raw", Image, on_new_image)
    rospy.spin()


if __name__ == '__main__':
    process_frames()
