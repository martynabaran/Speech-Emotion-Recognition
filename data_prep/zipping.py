# import tarfile
# import os

# # Folder źródłowy z plikami audio
# source_dir = "C:\\Users\\Martyna\\Desktop\\inzynoerka\\emocje\\data\\train1"

# # Ścieżka do folderu wynikowego i docelowy plik .tar.gz
# output_dir = "\\Users\\Martyna\\Desktop\\inzynoerka\\emocje\\audio\\train_files"
# output_tar_gz = os.path.join(output_dir, "train1.tar.gz")

# # Upewnij się, że folder docelowy istnieje
# os.makedirs(output_dir, exist_ok=True)

# # Tworzenie archiwum .tar.gz
# with tarfile.open(output_tar_gz, "w:gz") as tar:
#     for file in os.listdir(source_dir):
#         full_path = os.path.join(source_dir, file)
#         tar.add(full_path, arcname=file)  # dodaje tylko pliki, bez folderu nadrzędnego

# print(f" Spakowano folder '{source_dir}' do '{output_tar_gz}'")
import os
import pandas as pd
import tarfile

# --- Ustawienia ---
metadata_path = "C:\\Users\\Martyna\\Desktop\\inzynoerka\\emocje\\metadata\\train_metadata.csv"
source_dir = "C:\\Users\\Martyna\\Desktop\\inzynoerka\\emocje\\data\\train"
output_dir = "C:\\Users\\Martyna\\Desktop\\inzynoerka\\emocje\\audio\\train_files"
output_dir_v2 = "C:\\Users\\Martyna\\Desktop\\inzynoerka\\emocje\\metadata"
output_tar_gz = os.path.join(output_dir, "train3.tar.gz")
output_metadata_path = os.path.join(output_dir_v2, "train_metadata_v3.csv")
SEED = 42
TOTAL_SAMPLES = 40000

# --- Upewnij się, że folder wynikowy istnieje ---
os.makedirs(output_dir, exist_ok=True)

# --- Wczytaj metadane ---
df = pd.read_csv(metadata_path)

# --- Usunięcie braków kategorii i zliczenie klas ---
df = df[df['category'].notna()]
unique_categories = df['category'].unique()

# --- Zbieranie próbki zapewniającej obecność każdej kategorii ---
samples_per_category = []
for cat in unique_categories:
    subset = df[df['category'] == cat]
    sample = subset.sample(n=1, random_state=SEED)  # po jednej z każdej kategorii
    samples_per_category.append(sample)

# --- Łączenie z resztą losowych próbek ---
remaining_needed = TOTAL_SAMPLES - len(samples_per_category)
remaining_df = df.drop(pd.concat(samples_per_category).index)
random_rest = remaining_df.sample(n=remaining_needed, random_state=SEED)

# --- Finalna próbka ---
selected_df = pd.concat(samples_per_category + [random_rest])
selected_df = selected_df.reset_index(drop=True)

# --- Zapisz wybrane metadane ---
selected_df.to_csv(output_metadata_path, index=False)

# --- Tworzenie archiwum z wybranymi plikami audio ---
with tarfile.open(output_tar_gz, "w:gz") as tar:
    for file in selected_df['file_name']:
        full_path = os.path.join(source_dir, file)
        if os.path.exists(full_path):
            tar.add(full_path, arcname=file)

print(f" Zapisano {TOTAL_SAMPLES} metadanych do '{output_metadata_path}'")
print(f" Spakowano pliki do archiwum: '{output_tar_gz}'")
