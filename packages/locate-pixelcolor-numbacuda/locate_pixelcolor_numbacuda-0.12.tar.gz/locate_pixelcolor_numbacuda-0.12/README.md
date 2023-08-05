# RGB search with numba.cuda - 10 x faster than numpy 

### pip install locate-pixelcolor-numbacuda


```python
from locate_pixelcolor_numbacuda import search_colors
from a_cv_imwrite_imread_plus import open_image_in_cv
import numpy as np
colors=[(66,  71,  69),(62,  67,  65),(144, 155, 153),(52,  57,  55),(127, 138, 136),(53,  58,  56),(51,  56,  54),(32,  27,  18),(24,  17,   8),]
```

#### image'https://www.pexels.com/pt-br/foto/foto-da-raposa-sentada-no-chao-2295744/'

```python
picnp = open_image_in_cv('pexels-alex-andrews-2295744.jpg',channels_in_output=3)
coords=search_colors(pic=picnp,colors=colors,threadsperblock=(18, 18,3),dtypetouse = np.int32)
print(coords)
%timeit search_colors(pic=picnp,colors=colors,threadsperblock=(18, 18,3),dtypetouse = np.int32)


# [[[  19   14]
#   [  19   14]
#   [  11   17]
#   ...
#   [6613 4524]
#   [6614 4524]
#   [6615 4524]]]
# 135 ms ± 3.5 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

# More benchmarks: https://github.com/hansalemaos/locate_pixelcolor_cpp

```
