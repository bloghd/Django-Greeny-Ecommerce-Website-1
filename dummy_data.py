import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from faker import Faker
import random
from products.models import Product, Category, Brand

def seed_brand(num):
    fake = Faker()
    imagess = ['01.jpeg','02.png','03.jpg','04.jpg','05.jpeg','06.jpg','07.jpeg','08.jpeg','09.jpeg','10.jpeg']
    for _ in range(num):
        name = fake.name()
        image = f"brands/{imagess[random.randint(0,9)]}"
        Brand.objects.create(
            name=name,
            image=image
        )
    print('done brand')
        
def seed_category(num):
    fake = Faker()
    imagess = ['01.jpeg','02.png','03.jpg','04.jpg','05.jpeg','06.jpg','07.jpeg','08.jpeg','09.jpeg','10.jpeg']
    for _ in range(num):
        name = fake.name()
        image = f"categories/{imagess[random.randint(0,9)]}"
        Category.objects.create(
            name=name,
            image=image
        )
    print('done category')
        
def seed_products(num):
    fake = Faker()
    flag_type = ['New', 'Feature']
    imagess = ['01.jpeg','02.png','03.jpg','04.jpg','05.jpeg','06.jpg','07.jpeg','08.jpeg','09.jpeg','10.jpeg']

    brands = list(Brand.objects.all())
    categories = list(Category.objects.all())
    
    if not brands:
        print("No brands found. Please seed the brands first.")
        return
    if not categories:
        print("No categories found. Please seed the categories first.")
        return

    for _ in range(num):
        name = fake.name()
        start_sku = 1000
        for i in range(num):
            sku = f"{start_sku + i:06}"
        price = round(random.uniform(20.99, 99.99), 2)
        description = fake.text(max_nb_chars=10000)
        flag = random.choice(flag_type)
        image = f"products/{imagess[random.randint(0,9)]}"
        
        brand = random.choice(brands)
        category = random.choice(categories)
        
        Product.objects.create(
            name=name,
            sku=sku,
            price=price,
            description=description,
            flag=flag,
            image=image,
            brand=brand,
            category=category,
        )
    print('done products')


seed_brand(30)
seed_category(30)
seed_products(600)