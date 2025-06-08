import json
import csv
import os

# Plik z Twoimi metadanymi JSON
input_json = "msp_podcast_metadata.json"  # <- Zmień na właściwą nazwę pliku JSON
data_root = os.path.abspath("C:/Users/Martyna/Desktop/inzynoerka/emocje/data")

# Wczytaj dane
with open(input_json, "r", encoding="utf-8") as f:
    data = json.load(f)

# Przygotuj listy
train_rows = []
test_rows = []

# Przetwórz dane
for item in data:
    file_path = item["file"]
    file_name = os.path.basename(file_path)
    
    # Stosunkowo względem katalogu data/
    partition = item["partition"]
    if partition == "Train":
        rel_path = os.path.join("data", "train", file_name)
    elif partition == "Development":
        rel_path = os.path.join("data", "test", file_name)
    else:
        rel_path = os.path.join("data", "test3", file_name)
    
    
    row = {
        "file_name": file_name,
        "original_full_path": rel_path.replace("\\", "/"),  # Upewnij się, że masz UNIX-style path
        "category": item["emotion_primary"],
        "arousal": item["arousal"],
        "valence": item["valence"],
        "dominance": item["dominance"],
        "emotion_secondary": json.dumps(item["emotion_secondary"]),  # zapis jako string
        "transcript": item["transcript"],
        "speaker_id": item["speaker_id"],
        "gender": item["gender"],
    }

    if partition == "Train":
        train_rows.append(row)
    elif partition == "Development":
        test_rows.append(row)
    else:
        # np. Test3 lub inne
        test_rows.append(row)

# Funkcja pomocnicza do zapisu CSV
def save_to_csv(rows, output_file):
    if not rows:
        return
    keys = rows[0].keys()
    with open(output_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)

# Zapisz pliki CSV
save_to_csv(train_rows, "train_metadata.csv")
save_to_csv(test_rows, "test_metadata.csv")

print("✅ Pliki zapisane: train_metadata.csv i test_metadata.csv")
