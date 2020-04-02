# Heart-disease-prediction

# Machine learning (Final Year Project)

<p align="center">
  <img width="460" height="300" src="https://github.com/ak224001/Heart-disease-prediction/blob/master/static/predict-heart-disease.jpg">
</p>
<h3>Acknowledgements</h3>
I would like to express my Thanks and gratitude to Dr. N. Renugadevi, Assistant Professor,indian institute of information technology for giving me an opportunity and guiding me during this project, giving me the valuable time and inputs to complete my project. 
</br>
I express my deepest Thanks to Abhinav singh, Himanshu yadav (Classmates) project partner for helping me in completing the tasks performed in this period and helping me in completing this project.

<h2>Introduction</h2>
New technologies like Machine learning and Big data analytics have been proven to provide promising solutions to biomedical communities, healthcare problems, and patient care. They also help in early prediction of disease by accurate interpretation of medical data. At an initial stage the prediction of heart disease can save human lives.

### Dataset : <a href = "https://www.kaggle.com/ronitf/heart-disease-uci">Heart-disease-prediction dataset</a>

### Dataset Description 
There are 15 columns in the dataset, however the first column name is not a good parameter as far as machine learning is considered so, there are effectively 14 columns.

1.	<b>Age</b> : displays the age of the individual.
2.	<b>Sex</b> : displays the gender of the individual using the following   format : 1 = male
          0 = female.
3.	<b>Chest-pain type </b>: displays the type of chest-pain experienced by the individual using the following format :
           1 = typical angina
           2 = atypical angina
           3 = non - anginal pain
           4 = asymptotic
4.	<b>Resting Blood Pressure </b>: displays the resting blood pressure value of an individual in mmHg (unit)
5.	<b>Serum Cholestrol</b> : displays the serum cholestrol in mg/dl (unit)
6.	<b>Fasting Blood Sugar</b> : compares the fasting blood sugar value of an individual with 120mg/dl. 
   If fasting blood sugar > 120mg/dl then : 1  (true)
                                else : 0   (false)
7.	<b>Resting ECG</b> : 
              0 = normal
              1 = having ST-T wave abnormality
              2 = left ventricular hyperthrophy
8.	<b>Max heart rate achieved</b> : displays the max heart rate achieved by an individual.
9.	<b>Exercise induced angina </b>: 
              1 = yes
              0 = no
10. <b>ST depression induced by exercise relative to rest </b>: displays the value which is integer or float.
11. <b>Peak exercise ST segment </b>: 
              1 = upsloping
              2 = flat
              3 = downsloping
12.	<b>Number of major vessels (0-3) colored by flourosopy </b>: displays the value as integer or float.
13.	<b>Thal </b>: displays the thalassemia : 
              3 = normal
              6 = fixed defect
              7 = reversable defect
14.	<b>Diagnosis of heart disease </b>: Displays whether the individual is suffering from heart disease or not : 
              0 = absence
              1,2,3,4 = present.
### Data Analysis

<b>Variation of Age</b> 
<p align="center">
  <img width="800" height="400" src="https://github.com/ak224001/Heart-disease-prediction/blob/master/images/Variation_of_Age.png">
</p>
We see that most people who are suffering are of the age of 58, followed by 57.
Majorly, people belonging to the age group 50+ are suffering from the disease.
</br>
<b>Heart disease frequency related to sex</b>
<p align="center">
  <img width="800" height="400" src="https://github.com/ak224001/Heart-disease-prediction/blob/master/images/frequency_related_to_sex.png">
</p>
</br>
<b>Heart disease frequency related to Chest pain type</b>
<p align="center">
  <img width="800" height="400" src="https://github.com/ak224001/Heart-disease-prediction/blob/master/images/Frequency_related_to_Chest_pain_typepng.png">
</p>
</br>
<b>Heart Disease Frequency According To FBS</b>
<p align="center">
  <img width="800" height="400" src="https://github.com/ak224001/Heart-disease-prediction/blob/master/images/Frequency_related_to_FBS.png">
</p>
</br>
<b>Heart Disease Frequency According To slope</b>
<p align="center">
  <img width="800" height="400" src="https://github.com/ak224001/Heart-disease-prediction/blob/master/images/Frequency_Related_to_slope.png">
</p>
</br>
<b>Max Heart rate</b>
<p align="center">
  <img width="600" height="300" src="https://github.com/ak224001/Heart-disease-prediction/blob/master/images/MAX_Heart_rate.png">
</p>
</br>
<h3> The Approach</h3>
<b>SVM</b>
 Accuracy for SVM for test set = 89.32%
</br>
<b>LogisticRegression</b>
 LogisticRegression Test Accuracy = 86.89%
</br>
<b>Random Forest Algorithm </b>
 Random Forest Algorithm Accuracy Score = 88.52%
</br>
<a href = "http://ec2-3-12-197-90.us-east-2.compute.amazonaws.com:8080/">Project link</a>
<h4>REFERENCES </h4>
[1] Sharma Purushottam, Dr. Kanak Saxena, Richa Sharma, “Heart Disease Prediction System Evaluation using C4.5 Rules and Partial Tree”, Springer, Computational Intelligence in Data Mining,vol.2, 2015, pp.285-294.</br>
[2] Boshra Brahmi, Mirsaeid Hosseini Shirvani, “Prediction and Diagnosis of Heart Disease by Data Mining Techniques”, Journals of Multidisciplinary Engineering Science and Technology, vol.2, 2 February 2015, pp.164-168.</br>
[3] Ashwini Shetty A, Chandra Naik, “Different Data Mining Approaches for Predicting Heart Disease”, International Journal of Innovative in Science Engineering and Technology, Vol.5, May 2016, pp.277-281.
