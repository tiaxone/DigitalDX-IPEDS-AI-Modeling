# DigitalDx AI Modelling (iTed) Work

## Progress thus Far

So far something of a working model has been built using human generated inputs (Yifu's categorical scores,) non-categorical numeric data (Mkt size, US spending, etc.) and non-categorical + categorical data (Timing of results, Solution Entry Point, etc.).

As of now the results are decently promising given the small size and relative incompleteness of the dataset (accurate at predicting if a company warrants a DDx investment roughly ~80% of the time) but there is still a considerable way to go for enhancing the model and the validity of its results. 

For the time being a Logistic Regression model (via SkLearn) has been used for simplicity and model explainability (see below) but going forward it will be extremely prudent to try a variety of different approaches to enhance performance. 

````markdown
X, y = num_non_num.values.tolist(), data['69. Ddx Invested'].values.tolist()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=6)
clf = LogisticRegression(random_state=0).fit(X_train, y_train)

from sklearn.model_selection import cross_val_score
scores = cross_val_score(clf, X_train, y_train, cv=15) 
scores
````

Please see the notebook in this repo for the entire source code and the datasets used.

## Things to be Done

i) The dataset itself needs to be greatly improved RE completeness. Many fields for various companies have been left blank forcing me to impute values hampering data quality (and drastically decreasing model performance). First and foremost this needs to be remedied (and can easily be done by any Fellow, using Sabit's new front-end).

ii) Model tuning needs to be performed on both the LR model that has already been trained and future models using different methods. This should have a dramatic effect on model performance and serve to further validate the original model.

iii) Further features need to be added and implemented (ie Disease type, Educational background (which needs a better scoring system), etc.) and existing features need to be screened (and potentially dropped). The model right now has over 60+ features, many of which may even be hindering performance, and needs to be tuned further. A PCA analysis would go a long way here.


### Biases/Preferences to Incorporate Into Modelling

For some of the categorical variables used in the model, certain "biases" or scalings have been introduced in order to tailor iTed to reflect the specific preferences of DDx's investment process.

The below table describes these preferences (in order of importance/significance).

| Feature  | Prefences (in Order L -> R)  |
|------------|-------------------------------------------|
| QoL Impacts  | Fatal -> Disabling -> Severe Pain -> Rash -> etc. |
| Solution Accuracy  | 90%+ (Desired) -> 70-90% (Ok) -> 60% (Ok if Only Known Solution) |
| Clinical Trials  | 300+ -> 200-300 & US -> EU -> Elsewhere |
| Number of Patents  |  Granted -> Provisional -> Filed |
| Funding Round | Up to 10M -> 10-20M -> 20M+ |
| Solution Benefits | Less Invasive -> More Accurate -> Less Expensive -> Faster |

## iTed.py & Endpoints

Beyond the notebook I have also put together a py script to serve as a baseline for iTed's ML ops (called ited.py). This py script defines the function ited() which takes in 3 inputs: a company's data, the entire database of companies tracked thus far, and an output file (in this case a JSON). The script is designed to be run constantly (each time a new startup fills in their info they have their scores calculated and their data is added to the database).

As the models are constantly retrained each time a new company is added (and thus added to the database) performance should ideally continue to improve over time. The output is a JSON of the three ML scores for each new company (a value between 0-1 corresponding to each model fit to the data (a Bayesian Ridge, Decision Tree and SVM)). 

The required input files are included in this repo and serve as the current template for both the company database and the information fed into the models to be scored. See database.xlsx and company.xlsx.
