#!/usr/bin/env python3  
  
import rclpy  
from rclpy.node import Node  
  
  
class TimerNode(Node):  
    def __init__(self):  
        super().__init__("timer_node")  
        self.counter_ = 0  
        self.get_logger().info("My first ROS 2 node has started.")  
  
        self.timer_ = self.create_timer(1.0, self.timer_callback)  
  
    def timer_callback(self):  
        self.counter_ += 1  
        self.get_logger().info(f"Hello {self.counter_}")  
  
  
def main(args=None):  
    rclpy.init(args=args)  
    node = TimerNode()  
    rclpy.spin(node)  
    rclpy.shutdown()  
  
  
if __name__ == "__main__":  
    main()