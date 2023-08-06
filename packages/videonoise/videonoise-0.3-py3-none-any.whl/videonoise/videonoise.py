#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
from pathlib import Path
import argparse
import numpy as np
from pydub import AudioSegment
from pydub.utils import which
from moviepy.editor import AudioFileClip, VideoClip


AUDIO_SAMPLE_RATE = 44100


def generate_white_noise_video(output, width, height, fps, duration, quiet=False):
    if not which("ffmpeg"):
        raise SystemExit('Can\'t find encoder "ffmpeg"')
    output_path = Path(output).absolute()
    audio_without_video = output_path.with_name(output_path.stem + "_without_video.mp3")
    temp_audiofile = output_path.with_name(output_path.stem + "_audio_tmp.mp4")
    if output_path.exists():
        raise SystemExit(f"File {output_path} already exists.")

    # Create white noise video
    def make_frame(t):
        return np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

    video = VideoClip(make_frame, duration=duration)
    video = video.set_fps(fps)

    # Create white noise audio
    audio_data = np.random.uniform(-1, 1, size=(duration * AUDIO_SAMPLE_RATE,)) * 32767
    audio_data = audio_data.astype(np.int16)

    audio_segment = AudioSegment(audio_data.tobytes(), frame_rate=AUDIO_SAMPLE_RATE, sample_width=2, channels=1)
    try:
        audio_segment.export(str(audio_without_video), format="mp3")
    except KeyboardInterrupt:
        audio_without_video.unlink(missing_ok=True)
        raise SystemExit("Interrupted by user.")

    # Combine video and audio
    audio = AudioFileClip(str(audio_without_video))
    final_video = video.set_audio(audio)
    logger = "bar" if not quiet else None
    try:
        final_video.write_videofile(str(output_path), temp_audiofile=str(temp_audiofile),
                                    codec='libx264', audio_codec='aac', logger=logger)
    except KeyboardInterrupt:
        temp_audiofile.unlink()
        audio_without_video.unlink()
        output_path.unlink(missing_ok=True)
        raise SystemExit("Interrupted by user.")

    # Clean up temporary files
    audio_without_video.unlink()


def main():
    parser = argparse.ArgumentParser(description="Generate a white noise video with audio.")
    parser.add_argument("output", type=str, help="Output video file path.")
    parser.add_argument("-w", "--width", type=int, default=640, help="Video width.")
    parser.add_argument("-t", "--height", type=int, default=480, help="Video height.")
    parser.add_argument("-f", "--fps", type=int, default=30, help="Video frames per second.")
    parser.add_argument("-d", "--duration", type=int, default=10, help="Video duration in seconds.")
    parser.add_argument("-q", "--quiet", action="store_true", help="Give less output.")

    args = parser.parse_args()

    generate_white_noise_video(args.output, args.width, args.height, args.fps, args.duration, args.quiet)


if __name__ == "__main__":
    try:
        main()
    except SystemExit as sys_exit:
        print(sys_exit, file=sys.stderr)
        sys.exit(1)
