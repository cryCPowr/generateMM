import os

def buatFolder(namaFolder):
    os.makedirs(namaFolder, exist_ok=True)
    return namaFolder

def save_to_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)

def append_to_file(file_path, content):
    with open(file_path, "a") as f:
        f.write(content)

def rapihkan(namaFolder, namaFile):
    return os.path.join(namaFolder, namaFile)

def cekNamaFile(file_path):
    if os.path.exists(file_path):
        print("File dengan nama tersebut sudah ada. Silakan pilih nama file yang lain.")
        return False
    else:
        return True

def namaFile():
    return input("Masukkan nama file untuk menyimpan akun Ethereum: ") + ".txt"

