FROM ros:jazzy

ARG ROS_DISTRO=jazzy
ARG ROS_WS=/root/ros2_ws

ENV ROS_DISTRO=${ROS_DISTRO}
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update \
 && apt upgrade -y \
 && apt install -y \
    ros-$ROS_DISTRO-teleop-twist-joy \
    ros-$ROS_DISTRO-teleop-twist-keyboard \
    ros-$ROS_DISTRO-twist-mux \
 && rm -rf /var/lib/apt/lists/*

COPY ros2_joysticks /root/ros2_ws/src/prj-iki-ros2/utils/ros2_joysticks
COPY config /root/ros2_ws/src/prj-iki-ros2/utils/ros2_joysticks/config

WORKDIR ${ROS_WS}

# Initialize rosdep and install dependencies
RUN apt-get update && \
    rosdep update && \
    rosdep install -y --ignore-src --from-paths src || true

# Build the workspace
WORKDIR /root/ros2_ws
# Using bash explicitly to run source command
RUN /bin/bash -c "source /opt/ros/$ROS_DISTRO/setup.bash && colcon build --symlink-install"