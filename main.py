
from sensor.configuration.mongo_db_connection import MongoDBClienct
from sensor.exception import SensorException
import sys, os
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig


if __name__=='__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.__dict__)
    except Exception as e:
        print(e)
