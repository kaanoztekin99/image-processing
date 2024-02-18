# image-processing

* Görüntüyü Gri Tonlama Dönüştürmek (Grayscale): Görüntüyü gri tonlamaya dönüştürmek, renk bilgisini koruyarak hesaplama yapmayı kolaylaştırır. Gri tonlamaya dönüştürme işlemi, görüntüdeki her pikselin tek bir yoğunluk değerine (0-255 arasında) sahip olduğu bir görüntü oluşturur. Bu, görüntü üzerindeki kenarları ve konturları daha iyi algılamak için önemlidir, çünkü renk bilgisiyle uğraşmamız gerekmez.


* Kenar Algılama (Canny Edge Detection): Canny kenar algılama, görüntüdeki kenarları tespit etmek için kullanılan bir tekniktir. Kenarlar, görüntüdeki yoğunluk değişikliklerinin (kontrast farklılıklarının) belirgin olduğu yerlerdir. Canny kenar algılama, kenarların konumlarını ve yoğunluklarını hassas bir şekilde belirleyerek görüntüdeki nesnelerin şeklini ve yapısını belirlememize yardımcı olur.


* Kontur Algılama (Contour Detection): Kenar algılama işleminden sonra, algılanan kenarları birleştirerek nesnelerin dış sınırlarını belirleyen konturlar elde edilir. Bu konturlar, nesnelerin genel şeklini temsil eder. Kontur algılama, nesne tespiti, tanıma ve analizi gibi birçok görüntü işleme görevinde kullanılır.


* Kapalı Poligon Algılama (Polygon Approximation): Konturlar genellikle düzensiz ve pürüzlü olabilir, bu nedenle kapalı poligonlar gibi daha basitleştirilmiş şekillere dönüştürülürler. Kapalı poligonlar, nesnelerin daha anlaşılır ve işlenebilir bir temsilini sağlar. Bu, nesneleri tanıma ve analiz etme sürecini kolaylaştırabilir.
