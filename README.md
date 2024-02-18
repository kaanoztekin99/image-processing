# image-processing

* Görüntüyü Gri Tonlama Dönüştürmek (Grayscale): Görüntüyü gri tonlamaya dönüştürmek, renk bilgisini koruyarak hesaplama yapmayı kolaylaştırır. Gri tonlamaya dönüştürme işlemi, görüntüdeki her pikselin tek bir yoğunluk değerine (0-255 arasında) sahip olduğu bir görüntü oluşturur. Bu, görüntü üzerindeki kenarları ve konturları daha iyi algılamak için önemlidir, çünkü renk bilgisiyle uğraşmamız gerekmez.


## Kenar Algılama (Canny Edge Detection): 
Canny kenar algılama, görüntüdeki kenarları tespit etmek için kullanılan bir tekniktir. Kenarlar, görüntüdeki yoğunluk değişikliklerinin (kontrast farklılıklarının) belirgin olduğu yerlerdir. Canny kenar algılama, kenarların konumlarını ve yoğunluklarını hassas bir şekilde belirleyerek görüntüdeki nesnelerin şeklini ve yapısını belirlememize yardımcı olur.

* Canny kenar algılama algoritması, görüntülerdeki kenarları tespit etmek için kullanılan bir yöntemdir. Bu algoritmanın parametreleri şunlardır:

* Görüntü: Kenarları tespit etmek için kullanılan giriş görüntüsü.
* Alt Eşik Değeri (Low Threshold): Kenar piksellerinin zayıf olarak kabul edildiği eşik değeri. Bu değer altındaki kenarlar genellikle gerçek kenarlar değildir ve kenar olarak kabul edilmezler.
* Üst Eşik Değeri (High Threshold): Kenar piksellerinin güçlü olarak kabul edildiği eşik değeri. Bu değer üstündeki kenarlar kesinlikle kenar olarak kabul edilir.
* Aperture Size: Sobel gradyan hesaplaması için kullanılan kenar tespitindeki filtre büyüklüğü. Varsayılan değer genellikle 3'tür.
* L2 Gradient (Opsiyonel): Kenarların büyüklüğünü hesaplamak için kullanılacak gradyanın L2-norm kullanılıp kullanılmayacağını belirten bir bayrak. Varsayılan olarak False'dir.

## Kontur Algılama (Contour Detection): 
* Kenar algılama işleminden sonra, algılanan kenarları birleştirerek nesnelerin dış sınırlarını belirleyen konturlar elde edilir. Bu konturlar, nesnelerin genel şeklini temsil eder. Kontur algılama, nesne tespiti, tanıma ve analizi gibi birçok görüntü işleme görevinde kullanılır.


## Kapalı Poligon Algılama (Polygon Approximation): 
* Konturlar genellikle düzensiz ve pürüzlü olabilir, bu nedenle kapalı poligonlar gibi daha basitleştirilmiş şekillere dönüştürülürler. Kapalı poligonlar, nesnelerin daha anlaşılır ve işlenebilir bir temsilini sağlar. Bu, nesneleri tanıma ve analiz etme sürecini kolaylaştırabilir.


## Hough Line dönüşümü
* Görüntüdeki doğrusal yapıları (çizgileri) tespit etmek için kullanılır. Bu dönüşüm, özellikle kenar algılama gibi işlemlerden elde edilen veriler üzerinde çalışır. Kenar algılama, görüntüdeki keskin değişiklikleri (genellikle obje sınırlarında) bulur ve bu değişiklikler genellikle çizgileri temsil eder.
* Hough Line dönüşümü, bu kenar bilgilerini alır ve bu çizgilerin parametrelerini (genellikle rho ve theta) kullanarak doğrusal yapıları tanımlar. Bu şekilde, bir görüntüdeki çizgileri belirleyebilir ve çizgilerin konumunu ve yönünü elde edebiliriz.
