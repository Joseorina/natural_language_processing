#Natural Language Processing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t',quoting=3)

#Cleaning the text
import re
review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][0])
review = review.lower()

