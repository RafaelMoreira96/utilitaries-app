import sys
import requests
import time
import csv
import os
from tqdm import tqdm
from urllib.parse import unquote  

def download_file(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status() 

        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192

        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=save_path)

        with open(save_path, 'wb') as file:
            start_time = time.time()
            downloaded_size = 0  

            for chunk in response.iter_content(chunk_size=block_size):
                if chunk:
                    file.write(chunk)
                    downloaded_size += len(chunk)
                    progress_bar.update(len(chunk))

                    elapsed_time = time.time() - start_time
                    if elapsed_time > 0:
                        speed = downloaded_size / elapsed_time 
                        speed_mb = speed / (1024 * 1024)  
                        progress_bar.set_postfix(speed=f"{speed_mb:.2f} MB/s")

        progress_bar.close()  

        if total_size != 0 and progress_bar.n != total_size:
            raise Exception("Erro: O download pode estar incompleto.")
        else:
            print(f"Download concluído! Arquivo salvo em: {save_path}")

    except Exception as e:
        raise Exception(f"Erro ao fazer o download: {e}")

if len(sys.argv) != 2:
    print("Uso: python main.py <caminho_do_csv>")
    sys.exit(1)

csv_path = sys.argv[1]

download_folder = os.path.join(os.getcwd(), 'download')
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

log_file_path = os.path.join(os.getcwd(), 'log_erros.csv')
with open(log_file_path, 'w', newline='', encoding='utf-8') as log_file:
    log_writer = csv.writer(log_file)
    log_writer.writerow(['Linha', 'Erro']) 

with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)  
    
    for row_number, row in enumerate(reader, start=2):  
        try:
            if len(row) == 2:  
                name_course, url = row
                filename = unquote(url.split('/')[-1])
                full_path = os.path.join(download_folder, filename)
                download_file(url, full_path)
            else:
                raise Exception(f"Formato inválido: a linha deve conter exatamente 2 colunas.")
        
        except Exception as e:
            with open(log_file_path, 'a', newline='', encoding='utf-8') as log_file:
                log_writer = csv.writer(log_file)
                log_writer.writerow([row_number, str(e)]) 
            print(f"Erro na linha {row_number}: {e}")