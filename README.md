# **Link website: https://hammerspace.adaptable.app/**

## Cara saya mengimplementasikan _checklist - checklist_ di ketentuan tugas:

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
  
