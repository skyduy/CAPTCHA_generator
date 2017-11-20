## CAPTCHA generator. Just for fun :).

The CAPTCHA created like this:

![1](https://github.com/skyduy/CAPTCHA_generator/raw/master/samples/7L2Nd.jpg)
![2](https://github.com/skyduy/CAPTCHA_generator/raw/master/samples/7NTYH.jpg)
![3](https://github.com/skyduy/CAPTCHA_generator/raw/master/samples/A4KA4.jpg)


Actually this is used for training data of project [CNN_keras](https://github.com/skyduy/CNN_keras)

### example:
```python
from captcha.core import Captcha

c = Captcha(150, 40, debug=True)
c.batch_create_img(10)
```

#### TODO
 - improve performance.
 - support multi parameters.
