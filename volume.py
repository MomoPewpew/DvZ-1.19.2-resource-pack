import os
import pydub

# define the directory where your .ogg files are located
directory = os.getcwd() + "\\assets\minecraft\sounds\\"

# define the maximum allowed peak volume in dBFS
max_volume = -6

# iterate over each file in the directory and its subdirectories
for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith('.ogg'):
            # load the audio file
            filepath = os.path.join(root, filename)
            audio = pydub.AudioSegment.from_ogg(filepath)

            # measure the peak volume of the audio file
            peak_volume = audio.max_dBFS

            # if the peak volume is higher than the maximum allowed,
            # reduce the volume by 6 dB
            if peak_volume > max_volume:
                print(f'modifying {filename}')
                audio = audio + (max_volume - peak_volume)

                # save the modified audio file
                audio.export(filepath, format='ogg')