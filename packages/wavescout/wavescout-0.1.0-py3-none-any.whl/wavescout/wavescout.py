import logging
import os
import zipfile
from dataclasses import dataclass, field

import aubio
import numpy as np
from pydub import AudioSegment
import essentia.standard as es


@dataclass
class BeatMap:
    beats: list = field(default_factory=list)
    bpm: int = 0
    key: str = ''
    key_confidence: float = 0.0

class WaveScout:
    def __init__(self, input_file):
        """
        Initialize the WaveScout with the input file and analyze its tempo and beats.
        """
        if not os.path.isfile(input_file):
            raise ValueError(f"File not found: {input_file}")

        self.input_file = input_file
        self.beat_map = BeatMap()
        self._analyze_tempo_and_beats()
        self._analyze_key()

    def _analyze_tempo_and_beats(self):
        """
        Analyze the tempo and beats of the input audio file.
        """
        win_s = 512
        hop_s = win_s // 2
        src = aubio.source(self.input_file, hop_size=hop_s)
        samplerate = src.samplerate
        tempo = aubio.tempo("default", win_s, hop_s, samplerate)
        total_frames = 0
        beats = []

        while True:
            samples, read = src()
            is_beat = tempo(samples)
            if is_beat:
                beats.append(total_frames / float(samplerate))
            total_frames += read
            if read < hop_s:
                break

        self.beat_map.bpm = int(tempo.get_bpm())
        self.beat_map.beats = beats
        logging.info(f"BPM: {self.beat_map.bpm}")
        logging.info(f"Beats: {self.beat_map.beats}")


    def _analyze_key(self):
        # Load the audio file using Essentia's MonoLoader
        loader = es.MonoLoader(filename=self.input_file)
        audio = loader()

        # Instantiate the KeyExtractor algorithm
        key_extractor = es.KeyExtractor()

        # Analyze the key and scale
        key, scale, key_strength = key_extractor(audio)

        # Store the results in the BeatMap
        self.beat_map.key = f"{key} {scale}"
        self.beat_map.key_confidence = key_strength


    def export(self, output_file, export_slices=False, measures_per_slice=16, beats_per_measure=4):
        """
        Export the beat map to a plaintext file and, if export_slices is True, export audio slices to a zip file.
        """
        with open(output_file, "w") as f:
            for beat in self.beat_map.beats:
                f.write(f"{beat}\n")

        if export_slices:
            zip_filename = os.path.splitext(output_file)[0] + ".zip"
            self._save_slices_to_zip(zip_filename, measures_per_slice, beats_per_measure)

    def _save_slices_to_zip(self, zip_filename, measures_per_slice, beats_per_measure):
        """
        Save the input audio file cut into slices to a zip file.
        """
        beats_per_slice = measures_per_slice * beats_per_measure
        audio = AudioSegment.from_file(self.input_file)
        beat_duration_ms = (60 / self.beat_map.bpm) * 1000

        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for i in range(0, len(self.beat_map.beats) - beats_per_slice, beats_per_slice):
                start_ms = self.beat_map.beats[i] * 1000
                end_ms = self.beat_map.beats[i + beats_per_slice] * 1000
                slice_audio = audio[start_ms:end_ms]

                temp_filename = f"slice_{i // beats_per_slice}.mp3"
                slice_audio.export(temp_filename, format="mp3")

                zipf.write(temp_filename, os.path.basename(temp_filename))
                os.remove(temp_filename)

                logging.info(f"Saved slice {i // beats_per_slice} to {zip_filename}")

class WaveScoutFactory:
    def __init__(self, directory):
        """
        Initialize the WaveScoutFactory with the target directory.
        """
        if not os.path.isdir(directory):
            raise ValueError(f"Directory not found: {directory}")

        self.directory = directory

    def get_audio_slicers(self, extensions=("mp3", "wav")):
        """
        Return a list of WaveScout instances for all valid files in the target directory.
        """
        audio_slicers = []

        for file in os.listdir(self.directory):
            if file.lower().endswith(extensions):
                input_file = os.path.join(self.directory, file)
                try:
                    slicer = WaveScout(input_file)
                    audio_slicers.append(slicer)
                except Exception as e:
                    logging.error(f"Error processing file {input_file}: {e}")

        return audio_slicers
