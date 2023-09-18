![image](https://github.com/sorfeb/hammerspace/assets/112263712/437e8278-6823-4540-b737-cc8e8f6275a9)# **Link website: https://hammerspace.adaptable.app/main/** 
Tampilan pada web belum tentu selaras dengan template main.html karena kemungkinan deployment masih dalam queue

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

*Selain unit testing pengecekan berjalannya URL di aplikasi dan penggunaan template yang sesuai, saya juga menambahkan 2 test baru pada tests.py: 
  - **test_model_creation** yang berfungsi untuk menguji apakah pembuatan object dan atribut 'Product' sudah tepat.
  - **test_show_main_view** yang berfungsi untuk simulasi HTTP GET request ke URL untuk menguji apakah request HTTP dan render template sudah berjalan dengan baik atau belum.


## Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
![image](https://github.com/sorfeb/hammerspace/assets/112263712/1a1fa9cf-15be-424b-a748-8a61cf7c4960)

Arsitektur framework yang digunakan di bagan di atas adalah MVT, atau Model-View-Template.
1. Pertama-tama client mengakses website kita dari URL web yang ia masukkan di web browser client sendiri. Ini mengakibatkan client menginisiasi request ke controller (dalam konteks ini, Django sendiri bertindak sebagai controller) yang ada di antara Client dan View. Controller akan cek apakah resource website _available_ atau tidak.
2. urls.py akan melakukan URL routing yang mengarahkan ke fungsi atau class View yang mana yang akan digunakan dan menentukan View yang mana yang akan meng_handle_ request HTTP berdasarkan request dari client. 
3. Selanjutnya, views.py yang bertindak sebagai komponen View akan menghandle request yang berguna untuk mengambil(fetch) data dari database melalui komponen Models, memproses input, dan juga menampilkan respons.
4. models.py sebagai komponen Model akan menjadi perantara antara views dan database jika View memperlu berinteraksi dengan data yang ada di dalam database (read/write)
5. berkas html yang ada di dalam komponen Template dan berisi tampilan webpage dengan placeholder yang dapat dimasukkan data akan dirender oleh View jika View mau menampilkan data ke client dalam bentuk webpage dalam konteks ini.
6. Setelah semua sudah diproses, View akan mengembalikan HTTP response object yang berisi HTML yang sudah berisi data-data yang client sudah request.
7. Akhirnya client menerima data melalui tampilan yang dikeluarkan oleh web browser client.
      
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


- **MVVM** atau biasa disebut sebagai Model-View-ViewModel
  
  Model: 
    - sama dengan **model** pada arsitektur lainnya.
    
  View:
    - hampir sama dengan **view** pada arsitektur lainnya, tetapi lebih pasif daripada view pada arsitektur yang lain karena cenderung hanya lebih fokus menampilkan data ke client dan me_render_ user         interface. Pada arsitektur ini, logika lebih banyak diproses oleh ViewModel
    
  ViewModel:
    - abstraksi dari view
    - terdiri dari model
    - mengurus logika presentasi dan state 

  MVVM memerlukan kode yang banyak
  MVVM lebih mudah dalam _unit testing_ karena kode yang _event driven_
  Titik masuk ke aplikasi seperti arsitektur MVT, yaitu pada View, tidak seperti MVC.
  Data dalam MVVM mengalir dalam satu arah: Model->ViewModel->View

## Apa perbedaan antara form POST dan form GET dalam Django?

  **POST**:
    - Digunakkan untuk _request_ yang dapat mengubah _state_ dari sistem (Cth: Membuat perubahan dalam _database_.
    - Tidak dapat di_bookmark_
    - Lebih aman daripada **GET**
    - Contoh: Django login form

  **GET**:
    - Digunakkan untuk _request_ yang menerima data dari server tanpa membuah perubahan dalam _database_.
    - Dapat di_bookmark_
    - Tidak lebih aman daripada **POST**
    - Jangan gunakkan GET untuk data sensitif seperti detail _login_ karena data terlihat di URL sehingga gampang untuk di_intercept_.
    
## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

**XML**
 - Lebih aman daripada JSON

**JSON**
 - Lebih cepat daripada XML karena beban yang lebih sedikit dan sintaks yang _straightforward_
 - 
## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
