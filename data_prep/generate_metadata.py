import os
import csv

# Ścieżka do folderu z transkrypcjami
folder_path = 'Transcripts/Transcripts'

# Ścieżka do pliku wynikowego CSV
output_csv = 'metadata.csv'

# Lista do przechowywania danych
data = []

# Iteracja po plikach w folderze
for file in os.listdir(folder_path):
    if file.endswith('.txt'):
        txt_path = os.path.join(folder_path, file)
        with open(txt_path, 'r', encoding='utf-8') as f:
            transcription = f.read().strip()
        
        # Zmieniamy rozszerzenie z .txt na .wav
        wav_filename = os.path.splitext(file)[0] + '.wav'
        data.append([wav_filename, transcription])

# Zapis do pliku CSV
with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['filename', 'transcription'])
    writer.writerows(data)

print(f"Plik '{output_csv}' został utworzony z {len(data)} wpisami.")
