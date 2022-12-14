# Clap-Activated-Light-Control
This Python program uses a microcontroller and sound sensor to control a light bulb. The program reads the input from the sound sensor and uses it to detect clapping. When a valid clapping pattern is detected, the program toggles the light on or off.

## Configuration
The program includes several configurable parameters that can be adjusted to change its behavior:

#### threshold: 
The minimum sound level required to detect a clap. This value should be adjusted based on the sensitivity of the sound sensor and the distance between the sensor and the clapper.
#### last_noise_time: 
The time when the last clap was detected. This value is used to determine the timing of the clapping pattern.
#### last_light_change: 
The time when the light was last turned on or off. This value is used to prevent the light from being toggled multiple times in response to a single clapping pattern.

## License
This program is licensed under the MIT License. See the LICENSE file for more details.
