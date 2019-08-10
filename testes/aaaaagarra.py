#!/usr/bin/env python3
from ev3dev.ev3 import *
from threading import *
import time
import math

m1 = LargeMotor('outD')
m2 = LargeMotor('outC')
m3 = MediumMotor('outB')
#cor = ColorSensor('in2')
#cor2 = ColorSensor('in4')
ir = InfraredSensor('in1')
#us2 = UltrasonicSensor('in3')

#cor.mode = 'COL-COLOR'
#cor2.mode = 'COL-COLOR'
ir.mode = 'IR-PROX'
#us2.mode = 'US-DIST-CM'

while True:
    if ir.value() > 20:
        m1.run_to_rel_pos(position_sp=50, speed_sp=200)
        m2.run_to_rel_pos(position_sp=50, speed_sp=200)
    else:
        m1.stop(stop_action="brake")
        m2.stop(stop_action="brake")
        m3.run_to_rel_pos(position_sp=50, speed_sp=200)
        time.sleep(1)
        while ir.value() != 0:
            m1.run_to_rel_pos(position_sp=250, speed_sp=200)
            m2.run_to_rel_pos(position_sp=250, speed_sp=200)
        m1.stop(stop_action="brake")
        m2.stop(stop_action="brake")
        m3.run_to_rel_pos(position_sp=-250, speed_sp=200)
        time.sleep(10)


