def ited(company_data,company_database,output_file):
    
    #package imports
    import pandas as pd
    import numpy as np
    import json
    from sklearn.model_selection import train_test_split
    from sklearn import linear_model
    from sklearn import svm
    from sklearn import tree
    
    #data preprocessing
    company_data = company_data.fillna(100)
    company_database = company_database.fillna(company_database.mean())  
    
    #formatting model data
    X, y = company_database.values.tolist(), company_database['69. Ddx Invested'].values.tolist()
    
    #bayesian ridge 
    reg = linear_model.BayesianRidge()
    reg.fit(X, y)
    
    #svm
    regr = svm.SVR()
    regr.fit(X,y)
    
    #tree
    clf = tree.DecisionTreeRegressor()
    clf = clf.fit(X, y)
    
    #scoring
    ridge_score = int(reg.predict(company_data))
    svm_score = int(regr.predict(company_data))
    tree_score = int(clf.predict(company_data))
    scores = {"Score 1 (Ridge)":ridge_score,"Score 2 (SVM)":svm_score,"Score 3 (Tree)":tree_score}
    
    #writing score output to JSON
    with open(output_file,'w') as outfile:
        json.dump(scores,outfile)
    
    #etl process
    if __name__ == "__main__":
        import sys
        if len(sys.argv) < 4:
            print('Error: Must provide two input and one output files')
            sys.exit(-1)
            
        else:
                company_csv = sys.argv[1] 
                database_csv = sys.argv[2] 
                output_file = sys.argv[3] 
                ited(company_data,comany_database,output_file)
