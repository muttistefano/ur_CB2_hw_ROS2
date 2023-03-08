import os
from os import environ
from os import pathsep
import sys

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, TimerAction
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from launch.actions import OpaqueFunction
from ament_index_python import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.actions import GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from scripts import GazeboRosPaths


def generate_launch_description():


    joy_teleop_file = PathJoinSubstitution(
        [FindPackageShare("ur_hardware_interface"), "config", "joy.yaml"]
    )


    joy_node = Node(
        package='joy',
        executable='joy_node',
        name='joy_node',
        parameters=[{
            'deadzone': 0.05,
            'autorepeat_rate': 20.0,
        }])

    joy_node_teleop = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        name='teleop_twist_joy_node',
        parameters=[joy_teleop_file],
        remappings={('/cmd_vel', 'imm/commands')},
        )

    nodes_to_start = [
        joy_node,
        joy_node_teleop,
    ]

    return LaunchDescription(nodes_to_start)


