#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

from threading import Thread

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev2 import IRBeaconDriverMixin


class Ev3rstorm(IRBeaconDriverMixin):
    def __init__(
            self,
            left_foot_motor_port: str = OUTPUT_B, right_foot_motor_port: str = OUTPUT_C,
            bazooka_blast_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_foot_motor_port, right_motor_port=right_foot_motor_port, motor_class=LargeMotor,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.bazooka_blast_motor = MediumMotor(address=bazooka_blast_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.leds = Leds()
        self.speaker = Sound()


    # following method must be used in a parallel process in order not to block other operations
    def keep_detecting_objects_by_ir_sensor(self):
        while True:
            if self.ir_sensor.proximity < 25: 
                self.leds.animate_police_lights(
                    color1='ORANGE',
                    color2='RED',
                    group1='LEFT',
                    group2='RIGHT',
                    sleeptime=0.5,
                    duration=5,
                    block=False)
                
                self.speaker.play_file(
                    wav_file='/home/robot/sound/Object.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                self.speaker.play_file(                                  
                    wav_file='/home/robot/sound/Detected.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                self.speaker.play_file(
                    wav_file='/home/robot/sound/Error alarm.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            else:
                self.leds.all_off()


    # following method must be used in a parallel process in order not to block other operations
    def blast_bazooka_whenever_touched(self):
        while True:
            if self.touch_sensor.is_pressed:
                if self.color_sensor.ambient_light_intensity < 5:
                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Up.wav',
                        volume=100,
                        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                    self.bazooka_blast_motor.on_for_rotations(
                        speed=100,
                        rotations=-3,
                        brake=True,
                        block=True)

                else:
                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Down.wav',
                        volume=100,
                        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                    self.bazooka_blast_motor.on_for_rotations(
                        speed=100,
                        rotations=3,
                        brake=True,
                        block=True)

                self.touch_sensor.wait_for_released()
 
    
    def main(self):
        Thread(target=self.keep_detecting_objects_by_ir_sensor).start()

        Thread(target=self.blast_bazooka_whenever_touched).start()

        self.keep_driving_by_ir_beacon()


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()

    EV3RSTORM.main()
