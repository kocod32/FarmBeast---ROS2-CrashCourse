#!/usr/bin/env python3  
  
import rclpy  
from rclpy.node import Node  
from std_msgs.msg import Int32

  
class PublisherNodeInt32(Node):  
    def __init__(self):  
        super().__init__("publisher_int32")  
        self.pub_num_ = 2  
  
        self.publisher_ = self.create_publisher(Int32, "/number", 10)  
        self.timer_ = self.create_timer(1.0, self.publish_message)  
  
        self.get_logger().info("PublisherInt32 node has started.")  
  
    def publish_message(self):  
        msg = Int32()  
        msg.data = self.pub_num_
        self.publisher_.publish(msg)  
        self.get_logger().info(f"Publishing: {msg.data}")  
  
  
def main(args=None):  
    rclpy.init(args=args)  
    node = PublisherNodeInt32()  
    rclpy.spin(node)  
    rclpy.shutdown()  
  
  
if __name__ == "__main__":  
    main()