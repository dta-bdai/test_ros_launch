cmake_minimum_required(VERSION 3.8)
project(my_package)

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

# Install Python modules
ament_python_install_package(my_package)

# Install Python executables
install(PROGRAMS
  my_package/simple_node.py
  my_package/simple_node_ros_args.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch files.
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
