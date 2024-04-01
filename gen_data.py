import numpy as np
import pandas as pd
from PIL import Image
import os

# Parameters
num_videos = 10  # Number of different 'videos' (solid color image series) to create
frame_count = 14  # Number of frames per video
frame_size = (512, 320)  # Adjusted size of each frame to match the training configuration
output_dir = 'toy_dataset'  # Directory to store the generated images
default_motion_bucket_id = 127  # Default motion bucket ID

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for video_id in range(num_videos):
    # Create a directory for each video
    video_dir = os.path.join(output_dir, f'video_{video_id}')
    if not os.path.exists(video_dir):
        os.makedirs(video_dir)

    # Create a unique color for this 'video'
    color = tuple(np.random.choice(range(256), size=3))
    
    for frame_id in range(frame_count):
        # Generate a solid color image
        img = Image.new('RGB', frame_size, color=color)
        
        # Save the image in its respective video directory
        frame_filename = f'frame_{frame_id:03d}.png'  # Zero padding for consistent naming
        img.save(os.path.join(video_dir, frame_filename))

print(f'Dataset generated in {output_dir}')

