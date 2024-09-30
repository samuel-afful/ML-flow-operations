import sys

import dagshub
dagshub.init(repo_owner='samuel-afful', repo_name='ML-flow-operations', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)