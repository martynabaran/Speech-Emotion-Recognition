import os
import json
import csv

from collections import defaultdict

emotion_map = {"N": "Neutral",
               "A": "Angry",
               "S": "Sad", 
               "H": "Happy",
               "U": "Suprise",
               "F": "Fear",
               "D": "Disgust",
               "C": "Contempt",
               "O": "Other",
               "X": "No agreement"}

# Paths to files and folders
base_path = "C:\\Users\\Martyna\\Desktop\\inzynoerka\\emocje"  # <-- change this
labels_path = os.path.join(base_path, "Labels", "labels_consensus.json")
detailed_labels_path = os.path.join(base_path, "Labels", "labels_detailed.json")
partition_path = os.path.join(base_path, "Partitions.txt")
speaker_path = os.path.join(base_path, "Speaker_ids.txt")
transcripts_folder = os.path.join(base_path, "Transcripts")
audio_folder = os.path.join(base_path, "Audios")

# Load partition info
partition_map = {}
with open(partition_path, "r") as f:
    for line in f:
        if ";" not in line:
            continue
        part, filename = line.strip().split(";")
        file_id = filename.replace(".wav", "")
        partition_map[file_id] = part.strip().lower()


# Load emotion labels
with open(labels_path, "r") as f:
    labels_data = json.load(f)

with open(detailed_labels_path, "r") as f:
    detailed_labels = json.load(f)
    
# Build the final dataset (excluding audio array for now)
dataset_entries = []

for audio_filename, entry in labels_data.items():
    # audio_filename = entry.key
    name = audio_filename.split(".")[0]
    transcript_path = os.path.join(transcripts_folder, f"{name}.txt")

    # Load transcript text
    try:
        with open(transcript_path, "r") as tf:
            transcript = tf.read().strip()
    except FileNotFoundError:
        transcript = ""
        
        
    secondary_emotions = set()
    detailed_entry = detailed_labels.get(audio_filename, {})
    for annotator_data in detailed_entry.values():
        emo_second = annotator_data.get("EmoClass_Second", "")
        emotions = [e.strip() for e in emo_second.split(",") if e.strip()]
        secondary_emotions.update(emotions)
        
    speaker_id = entry.get("SpkrID", "").strip()
    gender = entry.get("Gender", "").strip()
    
    dataset_entry = {
        "file": os.path.join(audio_folder, audio_filename),
        "emotion_primary": emotion_map.get(entry.get("EmoClass", ""), ""),
        "emotion_primary_code": entry.get("EmoClass", ""),
        "arousal": float(entry.get("EmoAct", 0.0)),
        "valence": float(entry.get("EmoVal", 0.0)),
        "dominance": float(entry.get("EmoDom", 0.0)),
        "emotion_secondary":list(secondary_emotions),
        "transcript": transcript,
        "speaker_id": speaker_id,
        "gender": gender,
        "partition": entry["Split_Set"] if entry["Split_Set"] != "" else partition_map.get(file_id, ""),
    }

    dataset_entries.append(dataset_entry)

# Save to file for inspection (optional)
import json
with open("msp_podcast_metadata.json", "w") as f:
    json.dump(dataset_entries, f, indent=2)
