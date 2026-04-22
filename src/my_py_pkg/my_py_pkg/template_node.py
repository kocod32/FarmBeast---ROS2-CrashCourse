#!/usr/bin/env python3  
  
import rclpy  
from rclpy.node import Node  
  
  
class XXXXXXXXX(Node):  
    def __init__(self):  
        super().__init__("XXXXXXXXX")  
    
  
def main(args=None):  
    rclpy.init(args=args)  
    node = XXXXXXXXX()  
    rclpy.spin(node)  
    rclpy.shutdown()  
  
  
if __name__ == "__main__":  
    main()