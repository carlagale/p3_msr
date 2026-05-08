from os.path import join
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import launch_ros.descriptions

def generate_launch_description():
    # Declare arguments
    description_file = LaunchConfiguration("description_file", default="robot.urdf.xacro")
    prefix = LaunchConfiguration("prefix", default="")
    use_sim_time = LaunchConfiguration('use_sim_time' , default='true')


    robot_description_content = Command([
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution([FindPackageShare("rover_description"), "robots", description_file]),
    ])

    robot_description_param = launch_ros.descriptions.ParameterValue(robot_description_content, value_type=str)

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        #namespace=robot_id,
        output='screen',
        parameters=[{
          'use_sim_time': use_sim_time,
          'robot_description': robot_description_param,
          'publish_frequency': 100.0,
          'frame_prefix': prefix,
        }],
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui'
    )

    # Rviz config and launching
    rviz_config_file = PathJoinSubstitution(
        [FindPackageShare("rover_description"), "config", "robot.rviz"]
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=["-d", rviz_config_file],
    )

    ld = LaunchDescription()
    ld.add_action(robot_state_publisher_node)
    ld.add_action(joint_state_publisher_gui_node)
    ld.add_action(rviz_node)
    return ld