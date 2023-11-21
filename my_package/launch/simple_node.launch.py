from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    ld = LaunchDescription([])
    ld.add_action(
        Node(
            package="my_package",
            executable="simple_node.py",
            output="screen",
            # ros_arguments=None,
            arguments=["--test_args", "10"],
        )
    )
    return ld
