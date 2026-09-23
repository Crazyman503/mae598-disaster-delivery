import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class TaskManager(Node):
    def __init__(self):
        super().__init__('task_manager')

        self.subscription = self.create_subscription(String, 'delivery_requests', self.request_callback, 10)

        self.get_logger().info("delivery task manager started")
    
    def request_callback(self, msg):
        self.get_logger().info(f'Recived delivery request: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    task_manager = TaskManager()
    rclpy.spin(task_manager)
    task_manager.destroy_node()
    rclpy.shutdown()

    if __name__ == '__main__':
        main()

