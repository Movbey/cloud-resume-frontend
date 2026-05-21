from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import Eventbridge, SNS
from diagrams.aws.cost import CostExplorer
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.client import User

with Diagram(
    "AWS Cost Optimizer",
    filename="cost-optimizer-architecture",
    show=False,
    direction="LR",
    graph_attr={"bgcolor": "white", "pad": "0.5", "dpi": "150"},
):
    schedule = Eventbridge("EventBridge\nDaily 8AM ET")

    with Cluster("Lambda: cost-optimizer-reporter"):
        fn = Lambda("Handler")
        ce = CostExplorer("Cost Explorer\nAPI (3 calls)")
        scanner_group = [
            EC2("EC2 / EBS\nDescribe"),
            RDS("RDS\nDescribe"),
            Cloudwatch("CloudWatch\nMetrics"),
        ]

    db = Dynamodb("DynamoDB\nCost History")
    topic = SNS("SNS Topic")
    email = User("Email\nReport")

    schedule >> fn
    fn >> ce
    fn >> scanner_group
    fn >> db
    fn >> topic >> email
