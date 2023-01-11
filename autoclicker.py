import random
import time
import mouse

for i in range(255):
    time.sleep(random.uniform(0.1, 0.11))
    
    if random.random() < 0.8:
        mouse.click(button='left')
    else:
        mouse.click(button='left')