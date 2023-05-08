from src.exception import InsuranceException
from src.logger import logging
import os
import sys
from src.utils import get_collection_as_dataframe
from src.entity.config_entity import DataIngestionConfig
from src.entity.config_entity import TrainingPipelineConfig
from src.components.data_ingestion import DataIngestion
from src.entity.artifacts_entity import DataIngestionArtifact
  
if __name__=="__main__":
    try:
        # get_collection_as_dataframe(database_name="INSURANCE", collection_name="INSURANCE_PROJECT")
        # test_logger_and_expection()
        training_pipelne_config =TrainingPipelineConfig()
        data_ingestion_config =DataIngestionConfig(training_pipeline_config=training_pipelne_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
    except Exception as e:
        print(e)