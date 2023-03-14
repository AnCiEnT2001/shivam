from gpiozero import MotionSensor,LED
import time
pir = MotionSensor(4)
led=LED(6)
print("Waiting for PIR to settle")
pir.wait_for_no_motion()
while True:
    print("Ready")
    pir.wait_for_motion()
    led.on()
    print("Motion Detected!")
    time.sleep(3)
    led.off()
