from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def select_features(data: pd.DataFrame, target_column: str, estimator=None) -> pd.DataFrame:
    
    label_encoder = LabelEncoder()
    for col in data.select_dtypes(include='object'):
        data[col] = label_encoder.fit_transform(data[col].astype(str))

    X = data.drop(target_column, axis=1)
    y = data[target_column]

    if estimator is None:
        estimator = RandomForestClassifier(n_estimators=100, random_state=42)
    sfm = SelectFromModel(estimator)

    sfm.fit(X, y)
    selected_features_mask = sfm.get_support()
    selected_features_names = X.columns[selected_features_mask]

    selected_data = data[selected_features_names.union([target_column])]

    return selected_data
