#!/usr/bin/env python3

# Copyright 2023 Your Name
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TwistStamped
from std_msgs.msg import Header


class TwistToTwistStampedConverter(Node):
    """
    A ROS2 node that converts Twist messages to TwistStamped messages.
    
    This node subscribes to a topic publishing Twist messages and republishes
    the content as TwistStamped messages with the current timestamp.
    """

    def __init__(self):
        super().__init__('twist_to_twist_stamped_converter')
        
        # Create a subscription to the input Twist topic
        self.subscription = self.create_subscription(
            Twist,
            'twist_in',
            self.twist_callback,
            10)
            
        # Create a publisher for the output TwistStamped topic
        self.publisher = self.create_publisher(
            TwistStamped,
            'twist_stamped_out',
            10)
        
        self.get_logger().info('Twist to TwistStamped converter initialized')

    def twist_callback(self, twist_msg):
        """
        Convert incoming Twist messages to TwistStamped and publish them.
        
        Args:
            twist_msg (Twist): The incoming Twist message
        """
        twist_stamped_msg = TwistStamped()
        
        # Set header with current timestamp
        twist_stamped_msg.header = Header()
        twist_stamped_msg.header.stamp = self.get_clock().now().to_msg()
        twist_stamped_msg.header.frame_id = 'base_link'
        
        # Copy twist data
        twist_stamped_msg.twist = twist_msg
        
        # Publish the converted message
        self.publisher.publish(twist_stamped_msg)


def main(args=None):
    rclpy.init(args=args)
    
    converter = TwistToTwistStampedConverter()
    
    rclpy.spin(converter)
    
    converter.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()