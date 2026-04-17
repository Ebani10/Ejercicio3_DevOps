#!/bin/bash
# Este corre en CodeBuild para mandar el log a S3
BUCKET_NAME="ebani-act-devops"
LOG_FILE="backup.log"

echo "Enviando log de actividad a S3..."
aws s3 cp $LOG_FILE s3://$BUCKET_NAME/$LOG_FILE