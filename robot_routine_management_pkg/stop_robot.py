# stop_robot.py
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import socket

class StopRobot(Node):

    def __init__(self, robot_id):
        super().__init__('stop_robot')
        topic = f'/{robot_id}/diffbot_base_controller/cmd_vel_unstamped'
        self.publisher_ = self.create_publisher(Twist, topic, 10)
        self.stop_robot()

    def stop_robot(self):
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.get_logger().info('Stop command sent to the robot.')

def main(args=None):
    rclpy.init(args=args)
    hostname = socket.gethostname()
    if hostname == 'rpirobot1':
        robot_id = 'robot_1'
    elif hostname == 'rpirobot2':
        robot_id = 'robot_2'
    elif hostname == 'robot-gym-vm':
        robot_id = 'robot_1'
    else:
        ValueError(f"Hostname: {hostname} invalid, doesn't belong to any robot.")

    node = StopRobot(robot_id=robot_id)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
