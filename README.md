This project is an application that tells you how many points you have in a ten meters shooting target after choosing a correct file.
This file must contain a picture of a target with ten holes in it in jpeg, jpg or png format.

It is developped with Python v3.7.6 using Flask Framework v1.1.2.

The request and response are sent and received using Ajax.

As this is the first version of the app, it will only work correctly if:
- only ten holes are in the target
- the ten holes are distinct, none hole merges to another one
- the background must be distinct from the target.

In case you have "Echec. La couleur du fond n'a pas pu être dissociée." error message then the background must be darker and in one color.
In the other case where you have "Echec. Impossible de repérer les 10 trous." error message then you must have ten holes in the target exactly.

You can add your background color range by putting it in getPoints.py file in the boudaries list.
The color is converted from RGB to HSV color.



In order not to store big files in the repo, here the links to example files to download so you can see how it works:

Correct pictures:

https://imgbox.com/lewVoUqO

https://imgbox.com/Ea1XBGBl

https://imgbox.com/7NT3ltrE

https://imgbox.com/fDsp7pUo

https://imgbox.com/ZuZ5GveP

https://imgbox.com/i9by89Sg

https://imgbox.com/DJdErZhT

https://imgbox.com/jmfatBs9

https://imgbox.com/I5KLFTNB



Test pictures to put in targetapp/tests/ folder:

https://imgbox.com/Qkw4ih51 ->(img_error_test.jpeg)

https://imgbox.com/xFHJy502 ->(img_ok_extractImg_test.jpg)

https://imgbox.com/VOoG3AmO ->(img_ok_processImg_test.jpg)

https://imgbox.com/W5NdAYRY ->(img_ok_test.jpeg)

To see the website working, just go to the following url :

https://target-ebres.herokuapp.com/


