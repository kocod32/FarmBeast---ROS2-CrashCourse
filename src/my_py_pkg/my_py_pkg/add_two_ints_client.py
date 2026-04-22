#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsClientNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")

        self.client_ = self.create_client(AddTwoInts, "/add_two_ints")

        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available, waiting again...")

        self.request_ = AddTwoInts.Request()
        self.request_.a = 5
        self.request_.b = 7

        self.future_ = self.client_.call_async(self.request_)
        self.future_.add_done_callback(self.response_callback)

        self.get_logger().info(
            f"Sent request: a={self.request_.a}, b={self.request_.b}"
        )

    def response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f"Result: {response.sum}")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClientNode()
    rclpy.spin(node)


if __name__ == "__main__":
    main()