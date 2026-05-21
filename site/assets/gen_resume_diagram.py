from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import CloudFront, Route53
from diagrams.aws.storage import S3
from diagrams.aws.security import CertificateManager
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.network import APIGateway
from diagrams.aws.devtools import Codebuild
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.client import User
from diagrams.onprem.vcs import Github

with Diagram(
    "Cloud Resume Challenge",
    filename="cloud-resume-architecture",
    show=False,
    direction="LR",
    graph_attr={"bgcolor": "white", "pad": "0.5", "dpi": "150"},
):
    user = User("Visitor")

    with Cluster("Frontend"):
        dns = Route53("Route 53\nDNS")
        cdn = CloudFront("CloudFront\nCDN")
        cert = CertificateManager("ACM\nSSL Cert")
        bucket = S3("S3 Bucket\nHTML/CSS/JS")

    with Cluster("Backend API"):
        apigw = APIGateway("API Gateway\nGET /count")
        fn = Lambda("Lambda\nPython")
        db = Dynamodb("DynamoDB\nVisitor Counter")

    with Cluster("CI/CD"):
        gh = Github("GitHub\nActions")

    with Cluster("IaC"):
        state = S3("S3\nTF State")

    logs = Cloudwatch("CloudWatch\nLogs")

    user >> dns >> cdn >> bucket
    cert - cdn
    user >> Edge(label="JS fetch") >> apigw >> fn >> db
    fn >> logs
    gh >> Edge(label="s3 sync") >> bucket
    gh >> Edge(label="terraform apply") >> state
