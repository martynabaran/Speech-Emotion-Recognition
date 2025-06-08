import os
import shutil

# Ścieżki
audio_dir = "Audios"
partition_file = "partitions.txt"
output_base_dir = "data"

# Mapa do folderów
partition_map = {
    "Train": "train",
    "Development": "test",
}

# Utwórz foldery docelowe
for folder in ["train", "test", "test3"]:
    os.makedirs(os.path.join(output_base_dir, folder), exist_ok=True)

# Przetwarzanie partition.txt
with open(partition_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        split_label, filename = line.split(";")
        split_label = split_label.strip()
        filename = filename.strip()

        # Ścieżka źródłowa
        src_path = os.path.join(audio_dir, filename)

        # Wyznacz folder docelowy
        if split_label in partition_map:
            dest_folder = partition_map[split_label]
        else:
            dest_folder = "test3"

        # Ścieżka docelowa
        dest_path = os.path.join(output_base_dir, dest_folder, filename)

        # Kopiowanie (zmień na shutil.move, jeśli chcesz przenieść)
        if os.path.exists(src_path):
            shutil.copy2(src_path, dest_path)
            print(f"✅ {filename} → {dest_folder}")
        else:
            print(f"⚠️ Plik nie istnieje: {src_path}")
