#!/usr/bin/env python3


from track3r_ev3dev1 import Track3r


class Track3rWithHammer(Track3r):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            medium_motor_port: str = OUTPUT_A):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            medium_motor_port=medium_motor_port)
        
        self.remote.on_beacon = self.hammer


    def hammer(self):
        # TODO
        ...

    
if __name__ == '__main__':
    TRACK3R_WITH_HAMMER = Track3rWithHammer()

    TRACK3R_WITH_HAMMER.main()
