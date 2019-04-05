## CAPTCHA generator. Just for fun :).

The CAPTCHA created like this:

![1](https://github.com/skyduy/CAPTCHA_generator/raw/master/samples/BJNF_ccac.jpg)
![2](https://github.com/skyduy/CAPTCHA_generator/raw/master/samples/EGVL_2a78.jpg)
![3](https://github.com/skyduy/CAPTCHA_generator/raw/master/samples/EGVL_2a78.jpg)


Actually this is used to generate training data of project [CNN_keras](https://github.com/skyduy/CNN_keras)

### example:
```python
from captcha import Captcha

letter_set = '0123456789'
letters_per_img = 5
min_width, min_height = 128, 36
c = Captcha(min_width, min_height, letter_set, letters_per_img, debug=True)
c.batch_create_img(5)
```

#### TODO
 - Add more customizable params.
 - Improve performance.
