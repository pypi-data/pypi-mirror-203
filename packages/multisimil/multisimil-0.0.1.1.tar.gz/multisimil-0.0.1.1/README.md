## Multisimil
This is a Python package to calculate similarity between two classified images at multiple scales.

The main objective of this package is to enable comparision of actual and predicted land use maps at multiple scales so a more relaxed assesment of accuracy can be done which is not possible with pixel to pixel comarision. It allows for the simulated map to miss the exact location of particular land use by a few pixels (specified by the user), and still will be considered a good prediction.

The module can be installed by:
```Python
! pip install multisimil
```
It is important to understand that in case of pixel to pixel comarision, even if when the entire map is shifted by 1 pixel, it will drastically reduce the accuracy. However, with comparing the frequecy of occurance of different land use classes in a neighborhood, a better comparision can be made.

```Python
import multisimil
from osgeo import gdal

image1 = "path/to/image1.tif"
image2 = "path/to/image2.tif"

rband1 = gdal.Open(image1).GetRasterBand(1)
rband2 = gdal.Open(image2).GetRasterBand(1)

array1 = rband1.ReadAsArray()
array2 = rbdand2.ReadAsArray()

nodata1 = rband1.GetNoDataValue()
nodata2 = rband2.GetNoDataValue()

array1[array1 == nodata1] = 0
array2[array2 == nodata2] = 0

# TO use 9*9 neighborhood, set f = 9
similarity = multisimil.calculate_similarity(array1, array2, f = 9)

```

Similarly, we can calculate similarity for multiple neighborhood filter sizes.

```Python
# This will calculate similarity for neighborhood sizes from 1*1 to 91*91
find_multiresolution_similarity(array1, array2, min_size = 1, max_size = 100, steps = 10)
```
More features to come soon.