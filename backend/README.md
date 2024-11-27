# Proje Kurulumu ve Geliştirme Rehberi

 ## IntelliJ IDEA Kurulumu

 - **Set Up IntelliJ IDE**

 - **Load pom.xml Configuration to IDE**, ensure IntelliJ sees `pom.xml` and Maven

 ## Veritabanı Bağlantısını Yapılandırın

 - From right hand side of the IDE, click the `Database` icon and configure it for your already set up local database.
   - **DB Name:** `eventlink`
   - **User Name:** `postgres` (usually)
   - **Check it with these commands:**

     ```bash
     psql -U postgres
     \du
     ```

 - **User Password:** the password used when logging into pgAdmin

 - **Check it with this command:**
   - **Linux:** `cd /etc/postgresql/<version>/main/pg_hba.conf`
   - **Windows:** `cd C:\Program Files\PostgreSQL\<version>\data\pg_hba.conf`
   - **pg_hba.conf dosyasındaki METHOD kısmını geçici olarak "trust" olarak değiştirin.**
   - **PostgreSQL'i yeniden başlatın:** `sudo systemctl restart postgresql`
   - **PostgreSQL shell'e bağlanın:** `psql -U postgres`
     ```sql
     ALTER USER username WITH PASSWORD 'new_password';
     ```

 - **Konfigürasyonu Eski Haline Getirin:**
   - pg_hba.conf dosyasını eski haline çevirerek trust yerine önceki kimlik doğrulama yöntemini (örneğin, `md5`) kullanın.
   - **PostgreSQL'i yeniden başlatın:** `sudo systemctl restart postgresql`

 ## Maven Komutları ve Kod Kontrolleri

 - **Do Clean & Install after and before writing any chunk of code to see anything went wrong.**
 - **Run tests for checking if writing new chunks broke old system functionality.**

 ### Clean & Install (Runs tests, checks dependencies, whole thing)

 - **Right hand side of the IDE is _M_ icon, navigate to `backend > lifecycle > clean & install`**
 - **On Command Line:**
   ```bash
   cd backend
   mvn clean install
   ```

 ### Running Only Tests

 - **Right hand side of the IDE is _M_ icon, navigate to `backend > lifecycle > test`**
 - **On Command Line:**
   ```bash
   cd backend
   mvn test
   ```

 ## Notlar

 - **Clean & Install:** Testleri çalıştırır, bağımlılıkları kontrol eder ve tüm projeyi derler.
 - **Testler:** Yeni kod parçacıkları eklediğinizde eski sistem işlevselliğinin bozulup bozulmadığını kontrol eder.
