from config import config
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from imblearn.over_sampling import SMOTE
def model_building(df):
    

    X = df.drop(columns=['Outcome'])
    y = df['Outcome']

    X_train, X_test, y_train, y_test = train_test_split(
                                                        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = RobustScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    smote = SMOTE(random_state=42)
    X_train, y_train = smote.fit_resample(X_train,y_train)

    return X_train, X_test, y_train, y_test
