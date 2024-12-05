from aws_cdk import (
    Duration,
    Stack,
    aws_dynamodb,
    aws_events,
    aws_events_targets,
    aws_lambda,
)
from constructs import Construct


class DynamodbLambdaStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create DynamoDB table
        demo_table = aws_dynamodb.Table(
            self, "user_info",
            partition_key=aws_dynamodb.Attribute(
                name="id", type=aws_dynamodb.AttributeType.STRING
            ),
        )

        # Create producer lambda function
        producer_lambda = aws_lambda.Function(
            self, "write_to_dynamodb_lambda_function",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            handler="write_to_dynamodb_lambda.lambda_handler",
            code=aws_lambda.Code.from_asset("./lambda/producer"),
        )
        producer_lambda.add_environment("TABLE_NAME", demo_table.table_name)

        # Create consumer lambda function
        consumer_lambda = aws_lambda.Function(
            self, "check_duplicate_username_lambda_function",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            handler="check_duplicate_username_lambda.lambda_handler",
            code=aws_lambda.Code.from_asset("./lambda/consumer"),
        )
        consumer_lambda.add_environment("TABLE_NAME", demo_table.table_name)

        # Finally, grant permission to lambda to read from & write to demo table
        demo_table.grant_write_data(producer_lambda)
        demo_table.grant_read_data(consumer_lambda)


        # Create query lambda function
        login_lambda = aws_lambda.Function(
            self, "check_login_lambda_function",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            handler="login_lambda.lambda_handler",
            code=aws_lambda.Code.from_asset("./lambda/login"),
        )
        login_lambda.add_environment("TABLE_NAME", demo_table.table_name)

        # Grant permission to lambda to read from demo table
        demo_table.grant_read_data(login_lambda)