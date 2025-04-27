# ros2-joysticks

Runs teleop_twist_joy node with a cutom launch file. 

Now ported for the diff_bot.

You can change the config file as needed or create a new one.

## Getting started
```bash
docker compose -f docker/docker-compose.yaml up
```

If you are not in University wifi to pull the image you can also build it locally as explained below.

## Build
```bash
docker compose -f docker/build.yml build
```

## Instructions

### Odrive botwheel controller
To run with odrive botwheel controller:

```bash
ros2 launch ros2_joysticks teleop_twist_joy_odrive_launch.py
```

### ROS2 Control example 2 (Diff_Bot)

TODO:

## External dependencies
 - [ROS2 Humble](https://docs.ros.org/en/humble/index.html)
 - [Docker](https://docs.docker.com/engine)

## Build dependencies
 - [Dockerfile](https://fbe-gitlab.hs-weingarten.de/prj-iki/barrob/robots/dumper/tins13_base/-/blob/main/docker/Dockerfile)

## Run dependencies
 - Docker

## Authors
 - David Grbac - _Main Contributor_ - @dg-224444
 - José Mendonça - diff_bot port
## License
 - To be determined.
