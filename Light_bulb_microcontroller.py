import time
import gpiozero

# Set up the microphone, light bulb, and control pin
microphone = gpiozero.InputDevice(pin=A0)
light = gpiozero.LED(pin=7)
control = gpiozero.OutputDevice(pin=2)

# Set the threshold for detecting clapping
threshold = 30

# Set the debounce and timing parameters
last_noise_time = 0
current_noise_time = 0
last_light_change = 0

while True:
    # Read the sound level from the microphone
    sound_level = microphone.value

    if sound_level > threshold:
        # Update the current noise time
        current_noise_time = time.time()

        # If the sound level is high enough and the conditions for a valid clap are met,
        # toggle the light and update the last noise time and last light change time
        if (
            (current_noise_time > last_noise_time + 0.2) and
            (current_noise_time < last_noise_time + 0.4) and
            (current_noise_time > last_light_change + 1)
        ):
            light.toggle()
            last_noise_time = current_noise_time
            last_light_change = current_noise_time

        # Otherwise, activate the control pin to indicate that a noise was detected
        else:
            control.on()
            time.sleep(0.05)
            control.off()

    # Wait for a moment before checking
