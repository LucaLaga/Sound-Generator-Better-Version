# Sound Generator - Better Version

## Overview

The Sound Generator - Better Version is a project designed to create and manipulate sound waves programmatically. It allows users to generate various types of sounds, modify their properties, and play them back in real-time. This project is ideal for developers interested in audio programming, sound design, and interactive applications.

## Features

* Generate different types of sound waves (sine, square, triangle, sawtooth).
* Control frequency, amplitude, and duration of the sounds.
* Real-time playback of generated sounds.
* User-friendly interface for sound manipulation.

## Requirements

* Python 3.x
* Required libraries: `numpy`, `pyaudio`

## Installation

To set up the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/LucaLaga/Sound-Generator-Better-Version.git
    ```
2. Navigate to the project directory:

    ```bash
    cd Sound-Generator-Better-Version
    ```
3. Install the required libraries:

    ```bash
    pip install numpy pyaudio
    ```

## Usage

To use the Sound Generator, run the main script:

```bash
python main.py
```

### Generating Sounds

You can generate sounds by calling the appropriate functions. Here are some examples:

```python
from sound_generator import SoundGenerator

# Create an instance of SoundGenerator
sound_gen = SoundGenerator()

# Generate a sine wave at 440 Hz for 2 seconds
sound_gen.play_sine_wave(frequency=440, duration=2)

# Generate a square wave at 523 Hz for 1 second
sound_gen.play_square_wave(frequency=523, duration=1)
```

### Modifying Sound Properties

You can modify the properties of the sounds generated:

```python
# Set amplitude and frequency
sound_gen.set_amplitude(0.5)
sound_gen.set_frequency(440)

# Play the modified sound
sound_gen.play_sine_wave(duration=2)
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

* [numpy](https://numpy.org/) for numerical operations.
* [pyaudio](https://people.csail.mit.edu/hubert/pyaudio/) for audio playback capabilities.
