## CAPTCHA generator. Just for fun :).

The CAPTCHA created like this:

![1](https://github.com/skyduy/CAPTCHA_generator/raw/master/samples/BJNF_ccac.jpg)
![2](https://github.com/skyduy/CAPTCHA_generator/raw/master/samples/EGVL_2a78.jpg)
![3](https://github.com/skyduy/CAPTCHA_generator/raw/master/samples/EGVL_2a78.jpg)


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
