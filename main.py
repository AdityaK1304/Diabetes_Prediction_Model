from src.data_ingestion import data_ingestion    
from src.data_preprocessing import data_preprocessing
from src.model_building import model_building
def main():
    df = data_ingestion()
    numerical_stats_report = data_preprocessing(df)
    X_train, X_test, y_train, y_test = model_building(df)
    print(X_train.shape)
    
    


if __name__ == "__main__":
    main()
