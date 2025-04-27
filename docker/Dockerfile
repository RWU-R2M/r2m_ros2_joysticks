ARG BASE_IMAGE=fbe-dockerreg.rwu.de/prj-iki-ros2/orga/ros2-docker-base:jazzy
FROM $BASE_IMAGE as base

RUN apt update \
 && apt upgrade -y \
 && apt install -y \
    ros-$ROS_DISTRO-teleop-twist-joy \
    ros-$ROS_DISTRO-teleop-twist-keyboard \
    ros-$ROS_DISTRO-twist-mux \
 && rm -rf /var/lib/apt/lists/*

COPY ros2_joysticks /root/ros2_ws/src/prj-iki-ros2/utils/ros2_joysticks
COPY config /root/ros2_ws/src/prj-iki-ros2/utils/ros2_joysticks/config

FROM base as build
WORKDIR /root/ros2_ws
RUN source /opt/ros/$ROS_DISTRO/setup.bash \
 && colcon build --symlink-install

