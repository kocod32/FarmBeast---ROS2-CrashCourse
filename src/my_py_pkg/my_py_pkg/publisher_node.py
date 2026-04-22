#!/usr/bin/env python3  
  
import rclpy  
from rclpy.node import Node  
from std_msgs.msg import String  
  
  
class PublisherNode(Node):  
    def __init__(self):  
        super().__init__("publisher_node")  
        self.counter_ = 0  
  
        self.publisher_ = self.create_publisher(String, "/hello", 10)  
        self.timer_ = self.create_timer(1.0, self.publish_message)  
  
        self.get_logger().info("Publisher node has started.")  
  
    def publish_message(self):  
        self.counter_ += 1  
        msg = String()  
        msg.data = f"Hello {self.counter_}"  
        self.publisher_.publish(msg)  
        self.get_logger().info(f"Publishing: {msg.data}")  
  
  
def main(args=None):  
    rclpy.init(args=args)  
    node = PublisherNode()  
    rclpy.spin(node)  
    rclpy.shutdown()  
  
  
if __name__ == "__main__":  
    main()