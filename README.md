## CAPTCHA generator. Just for fun :).

The CAPTCHA created like this:

![1](https://github.com/skyduy/CAPTCHA_generator/raw/master/samples/3VDL1_f23e.jpg)
![2](https://github.com/skyduy/CAPTCHA_generator/raw/master/samples/12JBJ_17c6.jpg)
![3](https://github.com/skyduy/CAPTCHA_generator/raw/master/samples/CUY25_5d54.jpg)


Actually this is used to generate training data of project [CNN_keras](https://github.com/skyduy/CNN_keras)

### example:
```python
from captcha import Captcha

c = Captcha(150, 40, debug=True)
c.batch_create_img(10)
```

#### TODO
 - improve performance.
 - support multi parameters.
