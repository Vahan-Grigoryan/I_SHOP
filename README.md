# I_SHOP
This is common internet shop(children care theme) where users can subscribe to new products mailing list, mark product as liked, add it to cart, purchase it with paypal or card(with pointed card credentials), change profile fields, affect product rating by comments, evaluate the product, read advices about child health care, filter products by brand, price range, category, colors and all these together!

## How to run project
_Note that in final_project/.gitignore i have *.env_ 
If you want run project you will need this file, for it you can write to my gmail: vahan.grigoryan.f@gmail.com

With **docker** from root dir run `docker-compose up`

Without docker:
Ensure that you have installed node.js, python and run following:
```
cd final_project
pip install -r django_requirements.txt
py manage.py runserver
```
Open new terminal
```
npm install --prefix fproject_front
npm run serve
```
