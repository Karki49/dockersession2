
import logging
logging.basicConfig(level=logging.INFO)
import random
import time
import os

def makeCake(customerName):
    cakeType = random.choice(["black forest", "while forest", "caramel"])
    for step in ["making batter", "put in oven", "let it cool"]:
        logging.info(step + " Cake for " + customerName)
        time.sleep(5)
    logging.info("Tada! %s cake for %s is ready!" %(cakeType, customerName))


if __name__=='__main__':
    name = os.environ.get("customerName", "Anonymous")
    makeCake(name)
