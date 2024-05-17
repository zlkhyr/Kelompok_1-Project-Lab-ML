 # Klasifikasi Rambu Lalu Lintas menggunakan CNN 

<img src="https://blog.way.com/wp-content/uploads/2022/08/Traffic-Signs-and-Their-Meanings.jpg">

## Kelompok 1 :
- Zul akhyar (2008107010080)
- Muhammad Akbarul Ihsan (2108107010044)
- Muhammad Kemal Fasya (2108107010052)
- Rania Safia Khuzai (2008107010051)
- Teuku Tamam Al-Fatah (2008107010071)

## Dataset
Dataset yang digunakan merupakan dataset siap pakai yang telah diproses sebelumnya untuk Rambu Lalu Lintas yang disimpan kedalam file `.pickle` sebagai berikut :

- train. pickle
- valid.pickle
- test. pickle

Untuk pejelasan lebih lengkap tentang Dataset cek : [Dataset](https://www.kaggle.com/datasets/valentynsichkar/traffic-signs-preprocessed) 

## Setup
***Note***: `Python`,`Anaconda` atau `Miniconda` sudah terinstall

Clone Repositori ini ke Lokal :
```bash
git clone https://github.com/zlkhyr/Kelompok_1-Project-Lab-ML.git
```

Masuk ke Direktori Project :
```bash
cd Project-Lab-ML
```

## Python Environment

Setelah masuk ke direktori yang telah di clone sebelumnya, Buat `Python Environment` :

```bash
python -m venv nama_venv
```

Aktifkan Environment yang baru saja dibuat:

```bash
#Windows
nama_venv\scripts\activat

#macOS dan Linux
source nama_env/bin/activate
```

Install `requirements.txt` untuk menginstal library yang diperlukan untuk project:

```bash
pip install -r requirements.txt
```

Buka VsCode, gunakan perintah berikut:

```bash
code .
```
Setelah membuka VsCode pastikan memilih Environment atau kernel yang telah diinstall sebelumnya, Pilihan ada di pojok kanan atas VsCode. Jalankan sel-sel di notebook untuk menjalankan proyek machine learning.

## Conda Environment

Setelah masuk ke direktori yang telah di clone sebelumnya, Buat `Python Environment` :

```bash
conda create --name nama_venv
```

Aktifkan Environment yang baru saja dibuat:

```bash
conda activate nama_venv
```

Install `requirements.txt` untuk menginstal library yang diperlukan untuk project:

```bash
#Dengan Conda
conda install --yes --file requirements.txt

#Dengan Pip
pip install -r requirements.txt
```

Jalankan Jupyter Notebook:
```
jupyter notebook
```
Buka file proyek_machine_learning.ipynb di antarmuka Jupyter Notebook, Jalankan sel-sel di notebook untuk menjalankan proyek machine learning.
