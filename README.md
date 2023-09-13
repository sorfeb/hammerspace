# **Link website: https://hammerspace.adaptable.app/main/**

## Cara saya mengimplementasikan _checklist - checklist_ di ketentuan tugas:
  1. Pertama-tama, buatlah direktori baru bernama hammerspace yang berisi _virtual environment_ baru.
  2. Selanjutnya isi direktori tersebut dengan berbagai file esensial yang dibutuhkan seperti .gitignore, requirements, dan juga file-file project linenya dengan command startproject. Jika semua instalasi dan konfigurasi sudah selesai, lanjut dengan mengupload direktori ke GitHub.
  3. Buat aplikasi baru bernama _main_ dalam proyek hammerspace yang berisi file template (html), model, view, dan file-file lainnya dan mendaftarkannya ke dalam proyek.
  4. Template html diisi dengan kode agar dapat menampilkan halaman yang sesuai dengan kemauan.
  5. Hubungkan view dengan template untuk me-render tampilan HTML dengan data yang diberikan.
  6. Routing URL aplikasi dalam berkas baru urls.py dalam direktori aplikasi untuk mengatur URL proyek.
  7. Menyesuaikan models.py dengan soal: membuat variable-variabel _name_, _amount_, _description_ sesuai dengen tipe datanya yaitu models.CharField, models.IntegerField, dan models.TextField. Tidak 
     lupa juga menambahkan nama, kelas, dan nama aplikasi dengan tipe data yang sama pada ketiganya yaitu models.CharField.
  8. Jangan lupa menyesuaikan kode pada views.py agar dapat merender variabel yang telah dibuat dan juga main.html agar memiliki template variables untuk data-data tersebut (cth: {{ name }}).
  9. Selanjutnya deploy aplikasi ini pada Adaptable menggunakan template Python App Template dan juga basis data PostgreSQL. Terakhir, setting launch command diisi dengan **python manage.py migrate && gunicorn hammerspace.wsgi**
      
## Mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment berfungsi untuk mengisolasi package serta dependencies aplikasi tersebut agar tidak menimbulkan konflik dengan versi-versi lain yang ada di komputer lokal.
Ya, kita masih dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi hal tersebut bukanlah kebiasaan yang baik karena mengisolasikan proyek dari versi-versi Python yang ada di dalam komputer untuk mencegah ketidaksengajaan modifikasi dan konflik instalasi antar proyek lain merupakan _best practice_ dalam mengembangkan sebuah proyek aplikasi berbasis web.

## Apakah itu MVC, MVT, MVVM dan apa perbedaan dari ketiganya?
- **MVC** atau biasa disebut sebagai Model-View-Controller.
  Model:
  - mengatur dan mengelola data dari aplikasi.
  - mewakili struktur data dan logika aplikasi yang berada di belakang tampilan.     
  - menghubungkan aplikasi dengan basis data dan mengatur interaksi dengan data tersebut.
 
  View:
  - komponen yang menangani logika presentasi.
  - mengontrol bagaimana data yang dikelola oleh model akan ditampilkan kepada pengguna.
  - pengatur tampilan dan mengambil data dari model untuk disajikan kepada pengguna.

  Controller:
  - perantara antara model dan view.
  - input berasal dari view, memprosesnya, dan memperbarui view.

ASP.NET MVC dan Spring MVC menggunakan arsitektur MVC.

- **MVT** atau biasa disebut sebagai Model-View-Template
  Model:
  - sama dengan **model** pada arsitektur lainnya

  View:
  - sama dengan **view** pada arsitektur lainnya

  Template:
  -  mengatur tampilan atau antarmuka pengguna.
  -  memisahkan kode HTML dari logika aplikasi.
  -  merancang tampilan yang akan diisi dengan data dari model melalui view.

Arsitekturnya hampir sama dengan MVC, tetapi controller sudah diurus oleh template.
Memodifikasi dengan arsitektur ini relatif lebih mudah daripada memodifikasi pada model MVC.
Django menggunakan arsitektur MVT.

-**MVVM** atau biasa disebut sebagai Model-View-ViewModel
  Model: 
    - sama dengan **model** pada arsitektur lainnya.
    
  View:
    - sama dengan **view** pada arsitektur lainnya.
    
  ViewModel:
    -abstraksi dari view
    - terdiri dari model 
  
