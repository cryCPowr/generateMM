from pybip39 import Mnemonic
from web3 import Web3
from eth_account import Account
from FF import buatFolder, save_to_file, rapihkan, namaFile, cekNamaFile

# Membuat folder untuk menyimpan file
namaFolder = buatFolder("EVM_accounts")

# Mengaktifkan fitur HD wallet Ethereum
Account.enable_unaudited_hdwallet_features()

# Membuat fungsi untuk membuat akun Ethereum
def buat_EVM(num_accounts):
    web3 = Web3()

    result = ""
    for i in range(num_accounts):
        mnemonic = Mnemonic()
        phrase = mnemonic.phrase
        account = web3.eth.account.from_mnemonic(phrase)
        result += f"Akun Ke {i + 1}\n"
        result += "Frase pemulihan: " + phrase + "\n"
        result += "Kunci privat: " + account._private_key.hex() + "\n\n"
        result += "Alamat Ethereum: " + account.address + "\n"

    return result

# Meminta input jumlah akun yang ingin dibuat
bobot_Akun = int(input("Berapa banyak akun yang ingin Anda buat? "))

# Mengatur nama file
nama_file = namaFile()

# Menggabungkan nama folder dan nama file
path_file = rapihkan(namaFolder, nama_file)

# Mengecek apakah file sudah ada, jika belum, menyimpan hasil pembuatan akun Ethereum ke dalam file
if cekNamaFile(path_file):
    result = buat_EVM(bobot_Akun)
    save_to_file(path_file, result)
    print("Hasilnya telah disimpan di:", path_file)
