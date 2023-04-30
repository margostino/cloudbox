import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions


class GluePythonSampleTest:
    def __init__(self):
        params = []
        if '--JOB_NAME' in sys.argv:
            params.append('JOB_NAME')
        args = getResolvedOptions(sys.argv, params)

        # spark = SparkSession.builder().appName("Python Spark SQL Hive integration example").config("spark.sql.warehouse.dir", "/home/glue_user/spark/").enableHiveSupport().getOrCreate()

        self.context = GlueContext(SparkSession.builder.getOrCreate())
        # self.context = GlueContext(spark)
        self.job = Job(self.context)

        if 'JOB_NAME' in args:
            jobname = args['JOB_NAME']
        else:
            jobname = "test"
        self.job.init(jobname, args)


    def run(self):
        dyf = read_json(self.context, "http://host.docker.internal:4566/sample-bucket/data.json")
        # dyf.printSchema()
        # print(f"Old table schema:{str(dyf.schema.fields)}")
        dyf.show(100)

        self.job.commit()


def read_json(glue_context, path):
    dynamicframe = glue_context.create_dynamic_frame.from_options(
        connection_type='s3',
        connection_options={
            # 'endpointUrl': 'http://host.docker.internal:4566/sample-bucket/persons.json',
            'paths': [path]
            # 'recurse': True
        },
        # additional_options={
        #     'endpointUrl': 'http://host.docker.internal:4566'
        # },
        format='json',
        format_options={
            # "jsonPath": "$.id",
            "multiline": True,
            # "optimizePerformance": True, -> not compatible with jsonPath, multiline
        }
    )
    return dynamicframe


if __name__ == '__main__':
    GluePythonSampleTest().run()
