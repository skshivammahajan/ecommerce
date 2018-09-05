import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# C:\Users\EZSHIGU\Documents\Shivam Mahajan\dev\ecommerce
print(BASE_DIR)
print(os.path.join(BASE_DIR, "static_my_proj"))
# C:\Users\EZSHIGU\Documents\Shivam Mahajan\dev\ecommerce\static_my_proj

print(os.path.join(os.path.dirname(BASE_DIR), "static_cdn"))
# C:\Users\EZSHIGU\Documents\Shivam Mahajan\dev\static_cdn
