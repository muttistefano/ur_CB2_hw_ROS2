cmake_minimum_required(VERSION 3.5)
project(ur_hardware_interface)

add_compile_options(-std=c++17)
add_compile_options(-Wall)
add_compile_options(-Wextra)
add_compile_options(-Wno-unused-parameter)

set(CMAKE_BUILD_TYPE Release)

find_package(ament_cmake REQUIRED)
find_package(controller_manager REQUIRED)
find_package(controller_manager_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(hardware_interface REQUIRED)
find_package(pluginlib REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_lifecycle REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(std_srvs REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)


include_directories(include)

set(THIS_PACKAGE_INCLUDE_DEPENDS
  controller_manager
  controller_manager_msgs
  geometry_msgs
  hardware_interface
  pluginlib
  rclcpp
  rclcpp_lifecycle
  std_msgs
  std_srvs
  tf2_geometry_msgs
)



add_library(cnr_ur_hardware_interface
  SHARED
  src/${PROJECT_NAME}/ur_hardware_interface.cpp
  src/${PROJECT_NAME}/ur_driver.cpp
  src/${PROJECT_NAME}/robot_state.cpp
  src/${PROJECT_NAME}/robot_state_RT.cpp
  src/${PROJECT_NAME}/ur_communication.cpp
  src/${PROJECT_NAME}/ur_realtime_communication.cpp
)


target_include_directories(
  cnr_ur_hardware_interface
  PRIVATE
  include
)
ament_target_dependencies(
  cnr_ur_hardware_interface
  ${${PROJECT_NAME}_EXPORTED_TARGETS}
  ${THIS_PACKAGE_INCLUDE_DEPENDS}
)

add_executable(ur_ros2_control_node src/ur_ros2_control_node.cpp)
target_include_directories(ur_ros2_control_node PUBLIC ${controller_manager_INCLUDE_DIRS})
target_link_libraries(ur_ros2_control_node ${controller_manager_LIBRARIES})
ament_target_dependencies(ur_ros2_control_node
  controller_interface
  hardware_interface
  rclcpp
)


pluginlib_export_plugin_description_file(hardware_interface hardware_interface_plugin.xml)

install(
  TARGETS  ur_ros2_control_node 
  DESTINATION lib/${PROJECT_NAME}
)


install(
  TARGETS cnr_ur_hardware_interface
  DESTINATION lib
)

install(
  DIRECTORY launch urdf config
  DESTINATION share/${PROJECT_NAME}
)


ament_export_libraries(
  cnr_ur_hardware_interface
)

ament_export_dependencies(
  hardware_interface
  pluginlib
  rclcpp
  rclcpp_lifecycle
  ${THIS_PACKAGE_INCLUDE_DEPENDS}
)

ament_package()