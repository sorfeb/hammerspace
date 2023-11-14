# **Link website: http://soros-febriano-tugas.pbp.cs.ui.ac.id/** 
Tampilan pada web belum tentu selaras dengan template main.html karena kemungkinan deployment masih dalam queue

# TUGAS 2
## Cara saya mengimplementasikan _checklist - checklist_ di ketentuan tugas: #1
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

### BONUS #1
*Selain unit testing pengecekan berjalannya URL di aplikasi dan penggunaan template yang sesuai, saya juga menambahkan 2 test baru pada tests.py: 
  - **test_model_creation** yang berfungsi untuk menguji apakah pembuatan object dan atribut 'Product' sudah tepat.
  - **test_show_main_view** yang berfungsi untuk simulasi HTTP GET request ke URL untuk menguji apakah request HTTP dan render template sudah berjalan dengan baik atau belum.


## Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
<p align="center"> 
  <img src= "https://github.com/sorfeb/hammerspace/assets/112263712/1a1fa9cf-15be-424b-a748-8a61cf7c4960">
</p>

Arsitektur framework yang digunakan di bagan di atas adalah MVT, atau Model-View-Template.
  1. Pertama-tama client mengakses website kita dari URL web yang ia masukkan di web browser client sendiri. Ini mengakibatkan client menginisiasi request ke controller (dalam konteks ini, Django           sendiri bertindak sebagai controller) yang ada di antara Client dan View. Controller akan cek apakah resource website _available_ atau tidak.
  2. urls.py akan melakukan URL routing yang mengarahkan ke fungsi atau class View yang mana yang akan digunakan dan menentukan View yang mana yang akan meng_handle_ request HTTP berdasarkan request        dari client. 
  3. Selanjutnya, views.py yang bertindak sebagai komponen View akan menghandle request yang berguna untuk mengambil(fetch) data dari database melalui komponen Models, memproses input, dan juga             menampilkan respons.
  4. models.py sebagai komponen Model akan menjadi perantara antara views dan database jika View memperlu berinteraksi dengan data yang ada di dalam database (read/write)
  5. Berkas html yang ada di dalam komponen Template dan berisi tampilan webpage dengan placeholder yang dapat dimasukkan data akan dirender oleh View jika View mau menampilkan data ke client dalam         bentuk webpage dalam konteks ini.
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

# TUGAS 3
## Apa perbedaan antara form POST dan form GET dalam Django?

  **POST**:
  - Digunakan untuk _request_ yang dapat mengubah _state_ dari sistem (Cth: Membuat perubahan dalam _database_.
  - Tidak dapat di_bookmark_
  - Lebih aman daripada **GET**
  - Contoh: Django login form

  **GET**:
  - Digunakan untuk _request_ yang menerima data dari server tanpa membuah perubahan dalam _database_.
  - Dapat di_bookmark_
  - Tidak lebih aman daripada **POST**
  - Jangan gunakkan GET untuk data sensitif seperti detail _login_ karena data terlihat di URL sehingga gampang untuk di_intercept_.
    
## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

**XML** (Extensible Markup Language):
 - Digunakan untuk merepresentasikan data dengan cara yang dapat dibaca mesin
 - Lebih aman daripada JSON
 - lebih kompleks dibandingkan JSON


**JSON** (JavaScript Object Notation):
  - digunakan untuk menyimpan dan mengirimkan data
  - Lebih cepat daripada XML karena beban yang lebih sedikit dan sintaks yang _straightforward_
  - lebih kompleks dibandingkan dengan JSON dan lebih sering digunakan dalam konteks bisnis


**HTML** (Hypertext Markup Language):
  - adalah sebuah _markup_ language yang digunakan untuk membuat halaman web.
  - digunakan untuk menampilkan data secara visual di browser web.
  - Bukan untuk pertukaran data
    
## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
  1. JSON lebih mudah dibaca dan dimengerti manusia karena menggunakan sintaks yang lebih mudah dan struktur yang lebih simpel daripada XML.
  2. Native JavaScript sehingga lebih kompatibel dengan JavaScript.
  3. Ukuran _file_ yang lebih kecil daripada XML sehingga lebih cepat untuk mentransfer data.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step #2.
  1. Buat file **base.html** baru sebagai kerangka umum untuk halaman lainnya dalam web ini dan juga mendaftarkannya ke** settings.py** agar terdeteksi
  2. Membuat file baru **forms.py** untuk membuat struktur web form baru
  3. Membuat fungsi **create_item** pada views.py agar data produk otomatis bertambah ke database
  4. Membuat file **create_item.html** baru untuk menampilkan halaman form penambah item
  5. Selanjutnya, buat fungsi baru **show_xml** dan **show_json** untuk menyimpan hasil _query_ dari seluruh data Item yang terdaftar dan juga mereturn data berbentuk xml atau json
  6. Tambah path _url_ ke **urlpatterns** agar fungsi **show_xml** dan **show_json** dapat diakses
  7. Buka postman sebagai data viewer dan GET http://localhost:8000/xml atau http://localhost:8000/json untuk mengetes apakah data diterima dengan baik.
  8. Data dalam bentuk xml atau json sudah dapat terlihat di Postman setelah GET.
  
## Mengakses kelima URL di poin 2 menggunakan Postman
- XML:
![image](https://github.com/sorfeb/hammerspace/assets/112263712/3052a776-5e3d-4eaa-a8f3-b3cbd8368bc2)

- JSON:
![image](https://github.com/sorfeb/hammerspace/assets/112263712/37b116ce-9199-4084-8050-05e0612ba3ab)

- HTML:
![image](https://github.com/sorfeb/hammerspace/assets/112263712/f0cc2367-2466-4807-b8af-e3c43f9d3c78)

- XML by ID:
![image](https://github.com/sorfeb/hammerspace/assets/112263712/9f047990-3d47-4ae2-9bec-4ba3a7a6dbd0)

- JSON by ID:
![image](https://github.com/sorfeb/hammerspace/assets/112263712/ea6296ad-c61b-43f8-bf67-253849515681)

### BONUS #2

```python
def show_main(request):
    #Take all objects of Item from the database
    inventory = Item.objects.all() 

    #Display number of items saved
    total_amount = Item.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'nama': 'Soros Febriano',
        'kelas': 'PBP-A',
        'aplikasi': 'hammerspace',
        'items': inventory,
        'items_counter' : total_amount
    }
    return render(request, "main.html", context)
```
<p align="center"> 
  <img src= "https://github.com/sorfeb/hammerspace/assets/112263712/97e4d114-310e-433a-8c96-ef25558505b2">
</p>

# TUGAS 4
## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah form _built-in_ yang tersedia oleh Django yang juga berguna untuk membuat form registrasi pengguna.

  **Kelebihan**:
     - Django UserCreationForm menyediakan validasi bawaan seperti memvalidasi kekuatan dan penyocokan kata sandi agar akun pengguna lebih aman.
     - Jauh lebih praktis daripada membuat kode form dari awal.
     - Form dari Django ini terintegrasi dengan Django sehingga memodifikasi komponen-komponen pada form ini akan lebih mudah dan manajemen data pengguna lebih efektif.
  
  **Kekurangan**:
    - Secara _default_ form ini hanya menyediakan field _username_ dan _password_, maka pemrogram harus membuat form custom untuk menambahkan field lainnya sesuai kemauan pemrogram.
    - Secara _default_ form ini juga dirancangn dengan sistem autentikasi bawaan Django, maka pemrogram harus memodifikasi form tersebut lebih lanjut jika ingin sistem autentikasi form yang lebih canggih.
      
  
## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
**Autentikasi** adalah proses memverifikasi identitas pengguna yang biasa menggunakan _username_ dan _password_ untuk memastikan bahwa pengguna saat ini memiliki hak untuk mengakses aplikasi dan mencegah kebocoran data sensitif.

**Otorisasi** adalah proses menentukan apakah pengguna memiliki izin akses kepada suatu fitur atau aksi pada sebuah aplikasi untuk mencegah pengaksesan informasi sensitif yang tidak berizin pada suatu aplikasi.

Keduanya sangat penting untuk mencegah terjadinya pengaksesan informasi sensitif seperti _source code_ atau informasi pribadi pengguna lain dan juga mencegah manipulasi data yang tidak diinginkan.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah data kecil yang disimpan pada peramban pengguna oleh laman web dan berisi tentang informasi _session_ pengguna seperti informasi _login_ dan preferensi pengguna (Cth: bahasa yang digunakkan, _search history_, barang-barang dalam _shopping cart_, dll.). 

Django memanfaatkan cookies dengan mengidentifikasi ID _session_ spesial untuk mengidentifikasi peramban web yang digunakkan dan _session_ (sebenarnya data _session_ tersimpan di dalam server dan ID _session_ tersimpan pada cookie yang tersimpan di laptop/PC pengguna) yang sesuai dengan laman web saat ini. 

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan _cookies_ sebenarnya aman secara default karena data _session_ pengguna tersimpan dalam perangkat pengguna secara luring. Akan tetapi, pihak yang tidak bertanggung jawab dapat melakukan sebuah metode peretasan, yaitu "Cookie Hijacking", sebuah metode mengambil data dalam cookie komputer pengguna dengan memancing pengguna masuk ke dalam laman _login_ palsu. Saat pengguna tertipu, peretas dapat mengambil cookie yang berisi data-data sensitif dan juga melacak aktifitas pengguna pada laman web lainnya di masa depan. Metode ini juga dapat terlaksanakan saat pengguna menggunakan WiFi publik yang tidak aman untuk berselancar di internet.

**Sumber:** https://www.mcafee.com/blogs/privacy-identity-protection/what-are-browser-cookies-and-how-do-i-manage-them/#:~:text=Like%20a%20phishing%20attack%2C%20cookie,browser%20and%20impersonate%20you%20online.


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
  1. import modul bawaan UserCreationForm, redirect, dan messages dari django.
  2. Tambahkan potongan kode untuk fungsi baru ** _register_** agar pengguna dapat mendaftar akun baru dan jangan lupa redirect pengguna ke main.html setelah pendaftaran sukses.
  3. Buatlah berkas baru _**register.html*_* untuk halaman pendaftaran pengguna baru dan jangan lupa daftarkan ke **_urls.py_**.
  4. Buatlah fungsi baru bernama _**login**_ agar pengguna yang sudah terdaftar dapat masuk dalam laman web kembali.
  5. Tambahkan fungsi _**login_user**_ dalam **_views.py_** untuk mengautentikasi apakah username dan password sudah benar (redirect ke main.html) atau belum (print error message).
  6. Buatlah berkas baru **_login.html_** sebagai halaman untuk pengguna login dan jangan lupa daftarkan ke **_urls.py_**.
  7. Buatlah fungsi baru bernama _**logout**_ agar pengguna yang sudah masuk dapat mengeluarkan akun dari halaman web.
  8. Tambahkan tombol **_logout_** dalam main.html agar pengguna yang sudah masuk dapat menggunakan fungsi tersebut.
  9. Jangan lupa menambahkan restriksi pada halaman **_main_** agar yang dapat mengakses hanya pengguna yang mempunyai akun untuk mengakses.
  10. Tambahkan sebaris kode: @login_required(login_url='/login') di atas fungsi **_show_main_** untuk merestriksi.
  11. Buatlah _cookie_ dengan mengimpor HttpResponseRedirect, reverse, dan datetime dan menambahkan cookie ** _last_login_** di dalam fungsi **_login_user_** agar kita dapat melihat kapan terakhir kali pengguna _login_.
  12. Jangan lupa tambahkan 'last_login': request.COOKIES['last_login'] agar waktu terakhir login dapat muncul dalam main.html
  13. Jangan lupa juga untuk menambahkan kode response.delete_cookie('last_login') dalam fungsi **_logout_user_** agar _cookie_ dihapus saat pengguna _logout_.
  14. Asosiasi produk dengan USER agar setiap pengguna hanya memiliki akses pada _item_ yang sesuai ditambahkan oleh masing-masing USER.

## DUMMY DATAS
![image](https://github.com/sorfeb/hammerspace/assets/112263712/de5aee3a-ad76-4dc1-90d6-26d7bd992376)
![image](https://github.com/sorfeb/hammerspace/assets/112263712/3bd19b57-f030-4ea5-8d4f-ab61055d4c48)


# TUGAS 5
## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Element selector lebih cepat dan mudah digunakkan. Gunakkan element selector saat ingin mengaplikasikan CSS secara seragam pada banyak elemen seperti <p> (text)

## Jelaskan HTML5 Tag yang kamu ketahui.
  - **&lt;br&gt;**: Adalah single line break yang berguna untuk membagi dokumen dengan sebuah garis pembatas yang merentang layar.
  - **&lt;div&gt;**: Tag yang sangat berguna untuk mengelompokan elemen-elemen dalam HTML agar menjadi lebih runtut dan rapi.
  - **&lt;h1&gt;** to **&lt;h6&gt;**: Membuat text bersifat heading dari 1 (paling besar) sampai 6 (paling kecil).
  - **&lt;img&gt;**: Mendefinisi sebuah gambar (image).
  - **&lt;meta&gt;**: Mendefinisikan metadata dokumen HTML yang berguna untuk memberi informasi seperti: character  encoding, author, description, dan lain-lain (tidak terlihat oleh viewer).
  - **&lt;ul&gt;**: Mendefinisikan sebuah _unordered list_.
    
## Jelaskan perbedaan antara margin dan padding.
<p align="center"> 
  <img src= "https://i1.wp.com/www.differencebetween.com/wp-content/uploads/2014/12/Difference-Between-Margin-and-Padding.png">
</p>

**Margin**: - Merepresentasikan ruang yang di luar **border** elemen.
            - Digunakkan untuk membuat ruang antara elemen.
            - Tidak memengaruhi dimensi elemen.

**Padding**: - Merepresentasi ruang antara **content** elemen dan **border** elemen.
             - Digunakkan untuk membuat ruang antara dalam elemen
             - Memengaruhi dimensi elemen.

## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
1. Tailwind **bukan** sebuah UI kit, sedangkan Bootstrap **adalah** sebuah UI kit yang menyediakan template, buttons, tabs, dll. untuk mempercantik desain laman web.
2. Tailwind memperbolehkan pengguna untuk lebih fleksibel dalam berkustomisasi, sedangkan Bootstrap mempermudah pengguna dengan menyediakan komponen yang telah dibuat oleh Bootstrap.
3. Tailwind menggunakan utility-first approach, Bootstrap menggunakan component-based approach.

Sebaiknya gunakan Tailwind jika ingin mengkustomisasi laman sesuai kemauan sendiri secara detail, tetapi gunakkan Bootstrap jika ingin mempercantik laman dengan komponen yang telah disediakan dengan cepat.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    1. Tambahkan Bootstrap CSS dan juga JS ke aplikasi dengan menambahkan blok kode berikut ke base.html:
    
```python
    <head>
    {% block meta %}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    {% endblock meta %}
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
</head>
```

  2. Kustomisasi sesuai selera dari link template Bootstrap

# TUGAS 6
## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
  **Asychronous Programming**:
    - Proses dilakukan secara paralel, sehingga tidak perlu menunggu proses lain untuk selesai terlebih dahulu.
    - Lebih cepat dan mengurangi waktu _lag_.
    - Lebih mudah untuk _scaling_.

  **Synchronous Programming**:
    - Proses dilakukan secara berurut, sehingga perlu menunggu proses sebelumnya untuk selesai terlebih dahulu.
    - Lebih lambat daripada Asynchronous programming
    - Lebih mudah untuk dimengerti dan lebih praktis.
    
## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
  Event-driven programming adalah paradigma programming yang berfokus pada merespon _event_ pada saat _event_ tersebut terjadi dan biasanya diproses oleh _event handlers_, sehingga lebih fleksibel   untuk membuat halaman web yang responsif dan fungsional.
  
  Contoh penerapannya dalam tugas ini adalah:

```python
        function addProduct() {
        fetch("{% url 'main:add_item_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshProducts)

        document.getElementById("form").reset()
        return false
      }

      document.getElementById("button_add").onclick = addProduct
```
yang terhubung pada:

```html
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Product by AJAX</button>
```

Dalam kode tersebut, saat tombol "Add Product by AJAX" ditekan, maka sebuah _event_ akan di_trigger_ dan script yang terhubung pada tombol tersebut tanpa me-_reload_ halaman web sehingga proses ini sangat responsif.
    
## Jelaskan penerapan asynchronous programming pada AJAX.
AJAX atau Asynchronous JavaScript and XML dapat memungkinkan pengguna untuk menerima data dari server web tanpa menunggu halaman untuk reload dan mempebolehkan beberapa kode lain untuk berjalan sekaligus sehingga dapat dikatakan AJAX mengimplementasi asynchronous programming. Contoh dalam AJAX:

  **Event-Handling**
    AJAX menerapkan event handling yang menjalankan fungsi secara asynchronous di komputer user sehingga tidak perlu di_refresh_.

  **Event Listeners**
    AJAX menyediakan event-listeners yang dapat mendeteksi aksi yang dilakukan oleh user dan event yang terjadi di halaman. Contoh: on-click, onload, onerror, onreadystatechange.
    
    
## Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

**Fetch API**:
- Lebih baru dan native JavaScript
- Syntax lebih mudah dibaca dan ditulis
- Lebih _lightweight_
- Kompatibel dengan semua browser modern kecuali _Internet Explorer_
- tidak mempunyai built-in support untuk JSONP.
- Tidak akan reject request HTTP walaupun error status 404 atau 500
- Tidak akan menerima atau mengirim cookies dari server sehingga dapat terjadi request yang tidak terautentikasi.
- 
**jQuery**:
- Sudah ada lebih lama dan lebih populer
- built-in support untuk JSONP.
- Kompatibel dengan semua browser modern termasuk _Internet Explorer_

Menurut saya, Fetch API lebih baik untuk digunakan karena lebih lightweight dan syntax lebih mudah dimengerti sehingga lebih baik untuk belajar PBP.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
  1. Buat fungsi dalam views.py add_product_ajax dan get_product_json yang berfungsi untuk fetch data untuk cards dan juga menambah items
  2. Tambahkan kedua fungsi tersebut ke dalam urls.py
  3. Buat script yang berfungsi untuk menampilkan data dan disajikan dalam bentuk cards dari fungsi get_product_json yang telah dibuat
  4. Tambahkan script refresh agar tampilan produk dalam cards terbarui dengan memuat ulang string html pada main.
  5. Selanjutnya, tambahkan kode html untuk form add product menggunakan AJAX
  6. Buat script dengan addProduct() agar form yang telah dibuat dapat berfungsi sebagai pengganti add product biasa.
  7. Tambahkan juga fungsi on-click pada button Add Product
  8. Deploy pada SaaS PBP
