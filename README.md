
# Floyd-Steinberg Dithering Algorithm

Bu repo, gri tonlamalı bir görüntüyü iki tonlu bir görüntüye dönüştürmek için Floyd-Steinberg dithering algoritmasını uygular. Dithering, görüntülerin sınırlı renk paletleriyle daha iyi görünmesini sağlamak için kullanılır.

## Gereksinimler

- Python 3.x
- Gerekli kütüphaneler:
  - `numpy`
  - `PIL` (Pillow)
  - `matplotlib` (görüntüleri göstermek için)

## Kurulum

1. **Kütüphaneleri Yükleyin**  
   Aşağıdaki komutları kullanarak gerekli kütüphaneleri yükleyin:

   ```bash
   pip install numpy Pillow matplotlib
   ```

2. **Repoyu Klonlayın**  
   Repoyu yerel bilgisayarınıza klonlayın:

   ```bash
   git clone https://github.com/zenithura/image-dithering.git
   cd image-dithering
   ```

## Kullanım Talimatları

1. **Görüntüyü Hazırlayın**  
   Kullanmak istediğiniz görüntüyü `input_image.png` adıyla `floyd_steinberg.py` dosyasıyla aynı dizinde kayd edin.

2. **Algoritmayı Çalıştırın**  
   Aşağıdaki komutu kullanarak algoritmayı çalıştırın:

   ```bash
   python floyd_steinberg.py
   ```

3. **Sonuç**  
   İşlenen görüntü `output_image.png` adıyla kaydedilecektir. Sonuç görüntüsünü kontrol edin.

   ![Çıktı Görüntüsü](combine.jpg)  

## Algoritma Hakkında

Floyd-Steinberg dithering algoritması, her pikselin hata değerini komşu piksellere dağıtarak, iki renkli bir görüntü elde etmek için kullanılan bir yöntemdir. Bu teknik, daha pürüzsüz geçişler sağlarken, iki renk arasında daha fazla ayrıntı tutmaya yardımcı olur.

## Örnek Görüntüler

Aşağıda, algoritmanın bazı örnek görüntüler üzerinde nasıl çalıştığını gösteren birkaç örnek bulunmaktadır:

- **Giriş Görüntüsü**  
  ![Giriş Görüntüsü](911.webp)  
  

- **İşlenmiş Görüntü**  
  ![İşlenmiş Görüntü](output.png)  
  
