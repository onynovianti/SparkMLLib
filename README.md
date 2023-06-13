# Big-Data
Tugas - Tugas Mata Kuliah Big Data

## Chapter
Spark MLLib

<hr/>

**0. Persiapan**
<table border="0">
<tr>
    <th colspan="2" align="center"><b>Menginstall PySpark dan Connect ke Google Drive</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/SparkMLLib/blob/7f3ad12d4b8a5c6bd081e77c942ef89bcac82e5d/copy_of_tugas_minggu_14_spark_mllib_ony.py#L15-L20</td>
    <td><img src="https://github.com/onynovianti/SparkMLLib/blob/aa69e0d9659c083cced75312ad0015bc266896a7/Image/0.%20Persiapan.png"></td>
 </tr>
</table><br>

**Movie Lens Recommendation**
<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Slide 30</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/SparkMLLib/blob/7f3ad12d4b8a5c6bd081e77c942ef89bcac82e5d/copy_of_tugas_minggu_14_spark_mllib_ony.py#L22-L56</td>
    <td><img src="https://github.com/onynovianti/SparkMLLib/blob/aa69e0d9659c083cced75312ad0015bc266896a7/Image/Slide%2030.png"></td>
 </tr>
 <tr>
    <th colspan="2" align="center">Penjelasan</th>
 </tr>
 <tr>
    <td colspan="2">Kode di atas menggunakan Spark MLlib untuk membangun model rekomendasi menggunakan metode ALS (Alternating Least Squares) pada dataset ratings.dat. Dataset tersebut dibaca dan diparse menjadi objek Rating, kemudian dibagi menjadi data training (80%) dan data test (20%). Model ALS kemudian dibuat dengan parameter yang telah ditentukan, dan dilakukan prediksi pada data test. Mean Squared Error (MSE) dihitung sebagai metrik evaluasi.</td>
 </tr>
</table><br>

<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Slide 48</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/SparkMLLib/blob/7f3ad12d4b8a5c6bd081e77c942ef89bcac82e5d/copy_of_tugas_minggu_14_spark_mllib_ony%20(2).py#L22-L63</td>
    <td><img src="https://github.com/onynovianti/SparkMLLib/blob/aa69e0d9659c083cced75312ad0015bc266896a7/Image/Slide%2048.png"></td>
 </tr>
 <tr>
    <th colspan="2" align="center">Penjelasan</th>
 </tr>
 <tr>
    <td colspan="2">Kode di atas menggunakan Spark MLlib untuk membangun model rekomendasi dengan menggunakan algoritma ALS (Alternating Least Squares) pada dataset ratings.dat. Data tambahan dalam variabel mydata ditambahkan ke dataset ratings. Model yang dibangun digunakan untuk menghasilkan rekomendasi produk untuk pengguna dengan ID 1. Hasil rekomendasi ditampilkan dengan menyertakan nama produk yang diurutkan berdasarkan peringkat.</td>
 </tr>
</table><br>

**Basic Statistic**
<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Basic Statistic</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/SparkMLLib/blob/7f3ad12d4b8a5c6bd081e77c942ef89bcac82e5d/copy_of_tugas_minggu_14_spark_mllib_ony%20(3).py#L22-L45</td>
    <td><img src="https://github.com/onynovianti/spark-streaming/blob/master/00_images/copy%20afiin.png"> <br>
    <img src="https://github.com/onynovianti/SparkMLLib/blob/aa69e0d9659c083cced75312ad0015bc266896a7/Image/Slide%2049.png"></td>
 </tr>
 <tr>
    <th colspan="2" align="center">Penjelasan</th>
 </tr>
 <tr>
    <td colspan="2">Kode di atas menggunakan Spark MLlib untuk menghitung statistik sederhana dari dataset ratings.dat. Dataset tersebut diambil dari file ratings.dat, kemudian hanya kolom rating yang digunakan untuk perhitungan. Statistik yang dihitung mencakup nilai rata-rata, variansi, dan jumlah elemen non-nol dalam dataset. </td>
 </tr>
</table>
<br>

**k-Means**
<table border="0">
 <tr>
    <th colspan="2" align="center"><b>k-Means</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/SparkMLLib/blob/7f3ad12d4b8a5c6bd081e77c942ef89bcac82e5d/copy_of_tugas_minggu_14_spark_mllib_ony%20(1).py#L44</td>
    <td><img src="https://github.com/onynovianti/SparkMLLib/blob/aa69e0d9659c083cced75312ad0015bc266896a7/Image/Slide%2054.png"></td>
 </tr>
 <tr>
    <th colspan="2" align="center">Penjelasan</th>
 </tr>
 <tr>
    <td colspan="2">Kode di atas menggunakan Spark MLlib untuk melakukan analisis klastering dengan menggunakan algoritma K-Means pada dataset yang diambil dari file kmeans_data.txt. Evaluasi dilakukan dengan menghitung Within Set Sum of Squared Errors (WSSSE) untuk mengukur kualitas klastering yang dihasilkan.</td>
 </tr>
</table><br>