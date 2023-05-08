import pandas as pd
import numpy as np
import pymongo
import json

client = pymongo.MongoClient("mongodb+srv://santhosh:sandy@cluster0.3bk3km6.mongodb.net/?retryWrites=true&w=majority")
DATA_FILE_PATH = "G:\Practice\Insurance Project\Insurance_Project\insurance.csv"
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    # print(f"shape'{df.shape}")

    df.reset_index(drop=True,inplace= True)

    json_record =  list(json.loads(df.T.to_json()).values())
    # print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
