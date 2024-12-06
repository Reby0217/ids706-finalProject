FROM amazon/aws-lambda-python:3.8

RUN pip install --upgrade pip && \
pip install --upgrade awscli

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

COPY check_duplicate_username_lambda.py ${LAMBDA_TASK_ROOT}

CMD [ "check_duplicate_username_lambda.lambda_handler" ]