robot_location = 30
ball_location = 35
goal_location = 20
have_ball = False

# if robot location is less than ball location it is almost at the ball
if robot_location < ball_location:
    print("Almost at the ball")

# if robot location is greater than goal location, it is beyond the goal.
if robot_location > goal_location:
    print("You are beyond the goal.")

# if the robot location is same as goal location it is in the goal
if robot_location == goal_location:
    print("The robot is at the goal.")

robot_location += 5

if robot_location == goal_location:
    print("At the goal.")

# if robot location is at ball location it picks up the ball
if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 15

# if robot location is less than goal location, robot went too far
if robot_location < goal_location:
    print("You went too far.")

# if robot location is same as goall location and has ball, robot scores goal
if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False

#2 purpose of indenting is to store instructions under an if statement. You can tell if the code is enclosed in an if branch if it is on the same line as the first indent after the if statement.
#4 the operators add or subtract to the current value of the variable