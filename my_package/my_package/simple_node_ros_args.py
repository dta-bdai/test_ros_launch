#!/usr/bin/env python

import argparse

import rclpy
from rclpy.node import Node


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test_args", type=int, required=True)

    # `ros2 launch my_package simple_node.launch.py` won't work without this.
    parser.add_argument("--ros-args", action="store_true")
    _ = parser.parse_args()

    rclpy.init()
    node = Node("my_node")
    node.get_logger().info("Spinning node")
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
