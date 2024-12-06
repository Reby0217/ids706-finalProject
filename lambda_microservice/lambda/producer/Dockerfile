FROM amazon/aws-lambda-python:3.8

RUN pip install --upgrade pip && \
pip install --upgrade awscli

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

COPY write_to_dynamodb_lambda.py ${LAMBDA_TASK_ROOT}

CMD [ "write_to_dynamodb_lambda.lambda_handler" ]