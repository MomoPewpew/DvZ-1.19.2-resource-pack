import os
import subprocess
from PIL import Image
import json
import shutil

# Get the first WebM file in the working directory
webm_file = next(file for file in os.listdir('.') if file.endswith('.webm'))
video_name = os.path.splitext(webm_file)[0]

# Create the output directory if it doesn't exist
frames_dir = 'frames'
if os.path.exists(frames_dir):
    if os.path.isdir(frames_dir):
        shutil.rmtree(frames_dir)
os.makedirs(frames_dir, exist_ok=True)
output_dir = f'assets/dvz/textures/font/{video_name}'
os.makedirs(output_dir, exist_ok=True)

# Define ffprobe command to get video information
ffprobe_command = [
    'ffprobe',
    '-v', 'error',
    '-select_streams', 'v:0',
    '-show_entries', 'stream=avg_frame_rate',
    '-of', 'default=noprint_wrappers=1:nokey=1',
    webm_file
]

# Execute ffprobe command and capture output
ffprobe_output = subprocess.check_output(ffprobe_command).decode().strip()

# Parse the output to obtain the average frame rate
current_fps = eval(ffprobe_output)

# Calculate the target frame rate
if current_fps >= 20:
    target_fps = 20
else:
    target_fps = max(1, math.ceil(20 / (20 // current_fps)))

# Run the ffmpeg command to extract frames
command = [
    'ffmpeg',
    '-codec:v', 'libvpx',
    '-i', webm_file,
    '-vf', f'fps={target_fps}',
    f'{frames_dir}/%03d.png'
]

subprocess.run(command)

# Counter for resized frames
counter = 0

# List to store provider dictionaries
providers_title = []
providers_subtitle = []
providers_actionbar = []

# Iterate over images in the "frames" folder
for frame_file in os.listdir(frames_dir):
    if frame_file.endswith('.png'):
        # Check if the counter has reached the limit
        if counter >= 999:
            break
    
        frame_path = os.path.join(frames_dir, frame_file)
        
        # Open the image
        image = Image.open(frame_path)
        
        # Resize the image while maintaining aspect ratio
        image.thumbnail((256, 256), Image.ANTIALIAS)
        
        # Create a new blank image with transparency
        new_image = Image.new("RGBA", (256, 256), (0, 0, 0, 0))  # Initialize with transparent black

        # Set the four outer corners to white with 1% alpha
        corner_pixels = [(0, 0), (255, 0), (0, 255), (255, 255)]
        for pixel in corner_pixels:
            new_image.putpixel(pixel, (255, 255, 255, 1))  # Set white pixel with 1% alpha
        
        # Calculate the position to paste the resized image
        x_offset = (256 - image.width) // 2
        y_offset = (256 - image.height) // 2
        
        # Paste the resized image onto the new blank image
        new_image.paste(image, (x_offset, y_offset))
        
        # Save the resized image to the output directory while preserving transparency
        output_file = os.path.join(output_dir, f'{counter:03}.png')
        new_image.save(output_file)
        
        # Generate provider dictionary
        provider_title = {
            "type": "bitmap",
            "file": f"dvz:font/{video_name}/{counter:03}.png",
            "ascent": 125,
            "height": 256,
            "chars": [f"\\uE{counter:03}"]
        }
        provider_subtitle = {
            "type": "bitmap",
            "file": f"dvz:font/{video_name}/{counter:03}.png",
            "ascent": 141,
            "height": 256,
            "chars": [f"\\uE{counter:03}"]
        }
        provider_actionbar = {
            "type": "bitmap",
            "file": f"dvz:font/{video_name}/{counter:03}.png",
            "ascent": 202,
            "height": 256,
            "chars": [f"\\uE{counter:03}"]
        }
        providers_title.append(provider_title)
        providers_subtitle.append(provider_subtitle)
        providers_actionbar.append(provider_actionbar)
        
        # Increment the counter
        counter += 1

# Generate JSON object
json_data_title = {
    "providers": providers_title
}
json_data_subtitle = {
    "providers": providers_subtitle
}
json_data_actionbar = {
    "providers": providers_actionbar
}

# Determine the JSON file path
json_file_path_title = os.path.join("assets", "dvz", "font", f"{video_name}_title.json")
json_file_path_subtitle = os.path.join("assets", "dvz", "font", f"{video_name}_subtitle.json")
json_file_path_actionbar = os.path.join("assets", "dvz", "font", f"{video_name}_actionbar.json")

# Create the directory if it doesn't exist
os.makedirs(os.path.dirname(json_file_path_title), exist_ok=True)
os.makedirs(os.path.dirname(json_file_path_subtitle), exist_ok=True)
os.makedirs(os.path.dirname(json_file_path_actionbar), exist_ok=True)

# Convert JSON object to string
json_string_title = json.dumps(json_data_title, indent=4)
json_string_subtitle = json.dumps(json_data_subtitle, indent=4)
json_string_actionbar = json.dumps(json_data_actionbar, indent=4)

# Replace double backslashes with single backslashes
json_string_title = json_string_title.replace('\\\\', '\\')
json_string_subtitle = json_string_subtitle.replace('\\\\', '\\')
json_string_actionbar = json_string_actionbar.replace('\\\\', '\\')

# Write JSON string to file
with open(json_file_path_title, 'w') as json_file_title:
    json_file_title.write(json_string_title)

with open(json_file_path_subtitle, 'w') as json_file_subtitle:
    json_file_subtitle.write(json_string_subtitle)

with open(json_file_path_actionbar, 'w') as json_file_actionbar:
    json_file_actionbar.write(json_string_actionbar)

print(f"Image resizing and saving completed. Total resized frames: {counter}")
print(f"JSON file '{json_file_path}' generated successfully.")