from aws_cdk import (
    core,
    aws_lambda,
    aws_apigateway
)

from hitcounter import HitCounter
from cdk_dynamo_table_viewer import TableViewer as viewer


class CdkworkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = aws_lambda.Function(
            self,
            'HelloHandler',
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            code=aws_lambda.Code.asset('lambda'),
            handler='hello.handler'  # Name of the file, plus the name of the function
        )

        hello_with_counter = HitCounter(
            self,
            'HelloHitCounter',
            downstream=my_lambda
        )

        aws_apigateway.LambdaRestApi(
            self,
            'Endpoint',
            handler=hello_with_counter.handler
        )
        viewer(
            self,
            'ViewHitCounter',
            title='The hits',
            table=hello_with_counter.table,
            sort_by="hits",
        )

