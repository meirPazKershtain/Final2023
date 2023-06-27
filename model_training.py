import pickle
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score


merged_df=data3.copy()
# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(merged_df.drop('price', axis=1), merged_df['price'], test_size=0.2, random_state=42)

# Define the column transformer for preprocessing
numValue=['Area','מספר תושבים', 'שטח', 'דירוג צפיפות', 'מדד גיני']
cutValue =[ 'type','room_number','סוג',
        'condition ', 'furniture ','floor', 'total_floors']

numerical_pipeline = Pipeline([
    ('scaling', StandardScaler())
])



categorical_pipeline = Pipeline([
    ('one_hot_encoding', OneHotEncoder(sparse=False, handle_unknown='ignore'))#
])


column_transformer = ColumnTransformer([
     ('numerical_preprocessing', numerical_pipeline, numValue),
    ('categorical_preprocessing', categorical_pipeline, cutValue)
    ], remainder='drop')

# Create the pipeline with the preprocessor and the ElasticNet model



pipe_preprocessing_model = Pipeline([
    ('preprocessing_step', column_transformer),
    ('model',  ElasticNet(alpha=0.5, l1_ratio=0.5))
])


# Train the model and perform cross-validation
#scores = cross_val_score(pipe_preprocessing_model, X_train, y_train, cv=10, scoring='neg_mean_squared_error')
#mse_scores = -scores


# Fit the model on the full training data
preprocessing_model=pipe_preprocessing_model.fit(X_train, y_train)


pickle.dump(preprocessing_model, open('trained_model.pkl','wb'))

# Loading model to compare the results


###model = pickle.load(open('model.pkl','rb'))


# Evaluate the model on the test data
#y_pred = pipe_preprocessing_model.predict(X_test)
#mse = mean_squared_error(y_test, y_pred)
#r2 = r2_score(y_test, y_pred)

# Print the performance metrics
#print('Mean Squared Error (CV):', mse_scores.mean(),mse_scores.mean()**0.5)
#print('Mean Squared Error (Test):', mse,mse**0.5)
