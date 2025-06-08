import os
import json
from datasets import Dataset, Audio
import pickle 

# Step 1: Create the audio dataset
audio_folder = "C:\\Users\\Martyna\\Desktop\\inzynoerka\\emocje\\Audios"

audio_paths = [
    os.path.join(audio_folder, f)
    for f in os.listdir(audio_folder)
    if f.endswith(".wav")
]

# # Limit to 32 files for testing
audio_paths = audio_paths

audio_dict = {"audio": audio_paths}
audio_dataset = Dataset.from_dict(audio_dict).cast_column("audio", Audio())
audio_dataset = audio_dataset.with_format("python")
# Step 2: Create a mapping from normalized path to audio info
audio_info_map = {
    os.path.normpath(audio_dataset[i]["audio"]["path"]): audio_dataset[i]["audio"]
    for i in range(len(audio_dataset))
}

# Step 3: Load metadata dataset
with open("msp_podcast_metadata.json", "r") as f:
    metadata = json.load(f)

# Limit metadata to the same 32 files (ensure it's matching)
metadata = [entry for entry in metadata if os.path.normpath(entry["file"]) in audio_info_map]

# Step 4: Merge audio info into metadata
for entry in metadata:
    file_path = os.path.normpath(entry["file"])
    audio_info = audio_info_map.get(file_path)

    # audio_info["array"] = audio_info["array"].tolist()
    if audio_info:
        entry["audio"] = audio_info
    else:
        print(f"Audio not found for {file_path}")

# Step 5: Save final dataset
with open("final_dataset_with_audio_test.pkl", "wb") as f:
    pickle.dump(metadata, f, indent=2)

