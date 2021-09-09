from robot_control_class import RobotControl
rc = RobotControl(robot_name="summit")

class moverobot:
    def __init__(self,motion, clockwise,speed, time):
        self.rc = RobotControl(robot_name="summit")
        self.motion = motion
        self.clockwise = clockwise
        self.speed = speed
        self.time = time
        self.time_turn = 2.1/self.speed   # This value should change with the speed
                                          # to rotate the robot by 90 degrees

    def my_square(self):
        i = 0
        
        while (i<4):
            self.move_straight()
            self.turn()
            i+=1

    def move_straight(self):
        self.rc.move_straight_time(self.motion, self.speed, self.time)

    def turn(self):
        self.rc.turn(self.clockwise, self.speed, self.time_turn)



my_obj = moverobot("forward", "clockwise", 0.5, 8)
my_obj.my_square()
