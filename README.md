# People Counting
This repository was created as part of a technical assessment for estimating the number of people in a video frame using computer vision.

## Prediction Results:
* Average number of people detected per frame (0:18 to 0:19 time window): **172**
* Estimated total number of people on the bridge: **2,111**

All predicted results, including images with bounding boxes and labels, can be found in the `results` directory.

## Installation
First, install the necessary dependencies:
```bash
sudo apt install ffmpeg
pip install -r requirements.txt
```

## Data processing
To fetch the video from YouTube and extract frames between 0:14 and 0:32, run the following:
```bash
python data_processing.py \
  "https://www.youtube.com/watch?v=y2zyucfCyjM" \
  "data/video/" \
  "data/video/Drone Footage of Canberras HISTORIC Crowd.mp4" \
  "data/frames/output_%04d.png" \
  14 \
  32
```
### Select the images
To select frames from the 0:18 to 0:19 interval (frames 100 to 125) for model inference:
```bash
mkdir data/selected_frames
for i in {0100..0125}; do cp  data/frames/output_$i.png data/selected_frames/; done
```

## Model Setup
Prepare the YOLO-CROWD model and set up the environment:
```bash
mkdir model
cd model
git clone https://github.com/bytebarde/YOLO-CROWD.git
cd YOLO-CROWD
pip install -r requirements.txt
```

### Inference
Run the model on the selected frames (note that the model weights are included in the repository for convenience):
```bash
python detect.py --weights yolo-crowd.pt --source /home/erwan2/Projects/people_counting/data/selected_frames
```
The predicted results will be saved at `model/YOLO-CROWD/runs/detect/exp`.
