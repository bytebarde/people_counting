"""
Module to complete the data processing pipeline, including fetching the video and extracting frames from it
"""

import subprocess
import os

import argparse
from pytubefix import YouTube
from pytubefix.cli import on_progress


def parse_args():
    parser = argparse.ArgumentParser(
        description="Fetch video from youtube and extract frames from it"
    )
    parser.add_argument(
        "url",
        type=str,
        help="URL of the youtube video",
        default="https://www.youtube.com/watch?v=y2zyucfCyjM",
    )
    parser.add_argument(
        "video_dir", type=str, help="Dir path to save the video", default="data/video/"
    )
    parser.add_argument(
        "video_path",
        type=str,
        help="Path to read the video", default="data/Drone Footage of Canberras HISTORIC Crowd.mp4",
    )
    parser.add_argument(
        "frame_save_pattern",
        type=str,
        help="Save pattern for the frames",
        default="data/frames/output_%04d.png",
    )
    parser.add_argument("start_time", type=int, help="Start time to extract the frames")
    parser.add_argument("end_time", type=int, help="End time to extract the frames")
    return parser.parse_args()


def fetch_video(url, path):
    yt = YouTube(url, on_progress_callback=on_progress)
    ys = yt.streams.get_highest_resolution()
    ys.download(path)


def extract_frame(video_path, frame_save_pattern, start_time, end_time):
    frame_save_path = os.path.dirname(frame_save_pattern)
    if not os.path.exists(frame_save_path):
        os.makedirs(frame_save_path)
        
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            video_path,
            "-vf",
            f"select=between(t\\,{start_time}\\,{end_time})",
            "-vsync",
            "vfr",
            frame_save_pattern,
        ]
    )


def main(url, video_dir, video_path, frame_save_pattern, start_time, end_time):
    fetch_video(url, video_dir)

    extract_frame(video_path, frame_save_pattern, start_time, end_time)


if __name__ == "__main__":
    args = parse_args()
    main(
        args.url,
        args.video_dir,
        args.video_path,
        args.frame_save_pattern,
        args.start_time,
        args.end_time,
    )
