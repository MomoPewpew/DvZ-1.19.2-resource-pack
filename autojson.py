import os
import json

# Create an empty dictionary to store the JSON data
data = {}

# Traverse the working directory and its subdirectories to find all the .ogg files
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".ogg"):
            # Get the filename without the extension and split it into parts
            name_parts = os.path.splitext(file)[0].split("/")
            filename = name_parts[-1]

            # Create nested dictionaries based on the filename parts
            nested_dict = data
            for part in name_parts[:-1]:
                nested_dict = nested_dict.setdefault(part, {})

            # Construct the "name" value by joining the last parts of the path and filename
            sound_path = os.path.relpath(root, start="sounds")
            sound_name = os.path.join(sound_path, filename).replace("\\", "/")

            # Remove the "../" from the start of the sound name
            if sound_name.startswith("../"):
                sound_name = sound_name[3:]

            # Get the size of the file in bytes
            file_size = os.path.getsize(os.path.join(root, file))

            # Determine whether to include the "stream" value based on the file size
            stream_value = file_size > 20_000

            # Update the data dictionary with the nested dictionaries and sound data
            sound_data = {"name": sound_name, "category": "sound"}
            if stream_value:
                sound_data["stream"] = True
            if "sounds" not in nested_dict.setdefault(filename, {}):
                nested_dict[filename]["sounds"] = []
            nested_dict[filename]["sounds"].append(sound_data)

# Write the dictionary to a .json file
with open("file_data.json", "w") as outfile:
    json.dump(data, outfile, indent=4)