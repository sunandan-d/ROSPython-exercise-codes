from robot_control_class import RobotControl
rc = RobotControl()

class turtle_move:
    def __init__(self,dist,speed):
        print("The movement straight starts now...")
        self.dist = dist
        self.speed = speed
        self.turn_time = 5 # to turn by 90 degrees

    def move(self):
        i = 0
        while (i<1):
            self.straight()
            self.turn_robot()
            i = i+1

    def straight(self):
        laser = rc.get_laser(360)

        while (laser>self.dist):
            rc.move_straight()
            laser = rc.get_laser(360)

        rc.stop_robot()

    def turn_robot(self):
        rc.turn("counter-clockwise",self.speed,self.turn_time)
        


inst = turtle_move(1,0.3)
inst.move()
