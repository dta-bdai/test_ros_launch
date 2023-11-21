Simple package to show the importance of `--ros-args`

Steps:

```bash
    colcon build --packages-select my_package
    # This will fail.
    ros2 launch my_package simple_node.launch.py
    # This should work.
    ros2 launch my_package simple_node_ros_args.launch.py
``````
