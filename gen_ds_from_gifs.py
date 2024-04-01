import numpy as np
import os
from PIL import Image, ImageSequence


# Parameters
input_dir = '/Users/brettyoung/Desktop/dev_24/tutorials/sdv/dataset'  # Directory containing the GIF files
output_dir = './extracted_frames_dataset'  # Directory to store the extracted frames
frame_skip = 2  # Number of frames to skip
frames_to_extract = 14  # Total number of frames to extract

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)



def extract_and_save_frames(gif_path, output_dir, frames_to_extract, frame_skip):
    with Image.open(gif_path) as img:
        # Check if the file is actually a GIF
        if img.format != 'GIF':
            print(f"Skipping non-GIF file: {gif_path}")
            return

        total_frames = img.n_frames  # Now safe to assume the file is a GIF

        # Check if GIF has enough frames
        required_frames = frames_to_extract * frame_skip
        if total_frames < required_frames:
            print(f"Warning: '{gif_path}' does not have enough frames for extraction. Required: {required_frames}, Found: {total_frames}")
            return  # Skip this GIF

        start_frame = (total_frames - frames_to_extract * frame_skip) // 2
        end_frame = start_frame + frames_to_extract * frame_skip

        frame_ids = range(start_frame, end_frame, frame_skip)
        for i, frame_id in enumerate(frame_ids):
            img.seek(frame_id)
            frame = img.convert('RGB')
            
            frame_filename = f'frame_{i:03d}.png'
            frame.save(os.path.join(output_dir, frame_filename))

# Iterate over all GIFs in the input directory
for gif_filename in os.listdir(input_dir):
    if gif_filename.lower().endswith('.gif'):
        gif_path = os.path.join(input_dir, gif_filename)
        
        # Create a directory for extracted frames of this GIF
        video_dir_name = gif_filename[:-4]  # Remove .gif extension for directory name
        video_dir = os.path.join(output_dir, video_dir_name)
        if not os.path.exists(video_dir):
            os.makedirs(video_dir)
        
        # Extract and save frames
        extract_and_save_frames(gif_path, video_dir, frames_to_extract, frame_skip)

print(f'Frames extracted to {output_dir}')
