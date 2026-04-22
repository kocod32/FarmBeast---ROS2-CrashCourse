#!/usr/bin/env python3  
import rclpy  
from rclpy.node import Node  
from std_msgs.msg import Int32  
  
  
class SubscriberNode(Node):  
    def __init__(self):  
        super().__init__("subscriber_int32")  
        self.sum_  = 0
        self.subscription_ = self.create_subscription(Int32 ,"/number",self.listener_callback,10)  
  
        self.get_logger().info("SubscriberInt32 node has started.")  
  

    def listener_callback(self, msg):
        self.sum_ += msg.data
        self.get_logger().info(f"{self.sum_}")  

  
def main(args=None):  
    rclpy.init(args=args)  
    node = SubscriberNode()  
    rclpy.spin(node)  
    rclpy.shutdown()  
  
  
if __name__ == "__main__":  
    main()