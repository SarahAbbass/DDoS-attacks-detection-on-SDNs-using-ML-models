# DDoS-attacks-detection-on-SDNs-using-ML-models
As a part of EECE 490 - Intro to Machine Learning course, we stacked five machine learning models into one model to increase accuracy and performance rates of DDoS attacks detection and mitigation on SDNs:
-Dataset used: InSDN dataset containing normal generated traffic and different types of attacks such as DDoS, DoS, U2R, BFA, etc. The dataset consists of 57 attributes and 136743 training points.
-Source of dataset:N.-A. L.-K. ,. A. D. J. MAHMOUD SAID ELSAYED, ”InSDN: A Novel SDN Intrusion Dataset,” IEEE Explore, 8 September 2020 . [Online].Available: https://ieeexplore.ieee.org/document/9187858
-Machine learning models used: support vector machine, decision tree, random forest, naive bayes, and k-nearset neighbor.
-All models were trained and tested separately on the InSDN dataset. A confusion matrix and classification report were created to evaluate the outcomes.
-All models were stacked into one "smart detection stacking model" using a stacking classifier with accuracy and f1-score higher than the aforementioned models.
Used: Python, scikit-learn, pandas, numpy, matplotlib
