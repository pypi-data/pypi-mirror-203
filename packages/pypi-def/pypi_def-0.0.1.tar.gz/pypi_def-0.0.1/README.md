# Pypi for Def

Library ini disusun dengan menggunakan struktur direktori yang terorganisir dan mengimplementasikan penggunaan define (def) secara penuh untuk modularitas dan fleksibilitas.

### Fitur Utama
- Struktur direktori yang terorganisir dengan subfolder untuk modul-modul terkait.
- Penggunaan define (def) untuk memisahkan fungsionalitas menjadi bagian-bagian yang terpisah dan dapat digunakan secara mandiri.
- Dokumentasi lengkap dan contoh penggunaan yang disertakan dalam setiap modul.
- Dukungan untuk Python 3.6, 3.7, 3.8, 3.9, dan 3.10.

### Struktur Direktori

```bash
pypi-def
├── __init__.py
├── module1.py
├── module2.py
├── subpackage1
│   ├── __init__.py
│   ├── module3.py
│   └── module4.py
├── subpackage2
│   ├── __init__.py
│   └── module5.py
├── LICENSE
├── README.md
└── setup.py
```

### Penggunaan

#### 1. Install library:

```bash
pip install pypi-def
```

#### 2. Menggunakan from import:

```python
from pypi_def import module1, module2
from pypi_def.subpackage1 import module3, module4
from pypi_def.subpackage2 import module5

module1.greet()
module2.calculate()
module3.greet()
module4.calculate()
module5.greet()
```

Untuk informasi lebih lanjut dan contoh penggunaan, silakan eksplorasi sendiri.

### Lisensi:
**Pypi-def** dikeluarkan di bawah Lisensi MIT.

Harap diingat bahwa contoh ini hanya sebagai referensi dan Anda perlu menggantikan informasi yang diberikan, seperti nama library, struktur direktori, nama modul, kelas, metode, dan atribut sesuai dengan kebutuhan dan implementasi proyek Anda sendiri.