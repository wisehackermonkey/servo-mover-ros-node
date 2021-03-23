// File: trajectory_msgs/JointTrajectoryPoint.msg

points = {
    names: ["pan_servo", "tilt_servo", "r_antenna", "l_antenna"],
    points: [
        { positions: [1.5, 1.5] },
        { positions: [1.5, 1.5] },
        { positions: [1.5, 1.5] },
    ]
}

s = { points: [{ positions: [1.5, 1.5] }] }
s = {
    points:
        [
            { positions: [1.5, 1.5] },
            { positions: [0.8, 1.2] }, { positions: [0.7, 0.6] },
            { positions: [0.3, 0.1] }
        ]
}