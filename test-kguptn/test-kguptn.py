import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1680711920652 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://test-kguptn-1/input/sample.json"],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1680711920652",
)

# Script generated for node Change Schema
ChangeSchema_node1680712286756 = ApplyMapping.apply(
    frame=AmazonS3_node1680711920652,
    mappings=[
        ("fruit", "string", "fruit", "string"),
        ("size", "string", "size", "string"),
        ("color", "string", "color", "string"),
    ],
    transformation_ctx="ChangeSchema_node1680712286756",
)

# Script generated for node Amazon S3
AmazonS3_node1680712399627 = glueContext.getSink(
    path="s3://test-kguptn-1/output/",
    connection_type="s3",
    updateBehavior="LOG",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1680712399627",
)
AmazonS3_node1680712399627.setCatalogInfo(
    catalogDatabase="test-kguptn", catalogTableName="new-table-kguptn"
)
AmazonS3_node1680712399627.setFormat("json")
AmazonS3_node1680712399627.writeFrame(ChangeSchema_node1680712286756)
job.commit()
