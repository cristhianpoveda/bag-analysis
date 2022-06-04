#!/usr/bin/env python3

import rosbag

bag = rosbag.Bag('./packages/my_package/example_rosbag_H3.bag')
for topic, msg, t in bag.read_messages():
    print(msg)
bag.close()