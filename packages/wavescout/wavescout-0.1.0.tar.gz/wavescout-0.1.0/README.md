
# WaveScout

WaveScout is a lightweight Python library for quickly analyzing the tempo and key of audio files and slicing them into smaller segments based on measures.

## Features

- Analyzes tempo (BPM) and key of audio files
- Generates beat maps for audio files
- Slices audio files into smaller segments based on measures
- Exports plaintext beat map files and audio slices as a zip file
- Supports processing multiple audio files in a directory

## Installation

You can install WaveScout using pip:

```bash
pip install wavescout
```

## Dependencies

- numpy
- aubio
- pydub

## Usage

Here's a simple example of using WaveScout:

```python
from wavescout import WaveScout

# Analyze the audio file
scout = WaveScout("path/to/your/audio_file.mp3")

# Export the beat map to a plaintext file
scout.export("beat_map.txt")

# Export the audio slices to a zip file
scout.export("slices.zip", export_slices=True)
```

You can also use WaveScout to analyze and process multiple audio files in a directory:

```python
from wavescout import WaveScoutFactory

factory = WaveScoutFactory("path/to/your/audio_files_directory")
maps = factory.create_maps()

for map in maps:
    map.export(f"{map.input_file_basename}_beat_map.txt")
    map.export(f"{map.input_file_basename}_slices.zip", export_slices=True)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
