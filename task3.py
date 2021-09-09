from robot_control_class import RobotControl
rc = RobotControl()

class ExamControl:
    def __init__(self,dist,speed):
        print("The robot starts is getting ready...")
        print("...The robot is checking the front-laser only")
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



    def get_laser_readings(self):
        global l_laser, r_laser 
        l_laser = rc.get_laser(719)
        r_laser = rc.get_laser(0)
        #print("left laser reading = ",left_laser)
        #print("right laser reading = ",right_laser)

    def main(self):
        print("The robot starts to move out...")
        print("...The robot is checking the lasers - left and right")
        self.get_laser_readings()
        rlaser_max = r_laser
        while (r_laser<=rlaser_max):
            rc.move_straight()
            self.get_laser_readings()

        rc.stop_robot()


inst = ExamControl(1,0.3)
inst.move()
print("Now the robot will move out")
inst.main()
print("The robot is free...")
