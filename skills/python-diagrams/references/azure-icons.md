# Azure & Infrastructure Icons in Python `diagrams`

Always set `outformat="svg"` and `show=False` in `Diagram(...)` unless raster output is explicitly required.

## Common Azure Imports (`diagrams.azure.*`)

- **Compute**: `AppServices`, `FunctionApps`, `ContainerApps`, `KubernetesServices`, `VM` (`diagrams.azure.compute`)
- **Network**: `ApplicationGateway`, `FrontDoors`, `VirtualNetworks`, `Subnets`, `LoadBalancers`, `DNSZones`, `PrivateEndpoint` (`diagrams.azure.network`)
- **Database & Storage**: `SQLDatabases`, `CosmosDb`, `DatabaseForPostgresqlServers`, `DatabaseForMysqlServers`, `CacheForRedis`, `StorageAccounts`, `BlobStorage` (`diagrams.azure.database`, `diagrams.azure.storage`)
- **Integration & Messaging**: `ServiceBus`, `EventGridTopics`, `EventHubs`, `APIManagement` (`diagrams.azure.integration`)
- **Security & Identity**: `KeyVaults`, `ActiveDirectory` (`diagrams.azure.security`, `diagrams.azure.identity`)
- **DevOps & Monitoring**: `ApplicationInsights`, `LogAnalyticsWorkspaces`, `ContainerRegistries` (`diagrams.azure.devops`, `diagrams.azure.analytics`)

## On-Premises & Generic (`diagrams.onprem.*`)

- `Apache`, `Nginx`, `PHP`, `MySQL`, `PostgreSQL`, `Redis`, `Docker`, `Client`, `User`

## Example Skeleton

```python
from pathlib import Path
from diagrams import Cluster, Diagram, Edge
from diagrams.azure.compute import ContainerApps
from diagrams.azure.database import DatabaseForPostgresqlServers
from diagrams.azure.network import FrontDoors
from diagrams.azure.security import KeyVaults

OUT_FILE = str(Path(__file__).resolve().parents[1] / "out" / "azure-topology")

with Diagram(
    "Azure Application Topology",
    filename=OUT_FILE,
    outformat="svg",
    show=False,
    direction="LR",
):
    edge = FrontDoors("Azure Front Door")
    with Cluster("Production VNet"):
        app = ContainerApps("API Service")
        db = DatabaseForPostgresqlServers("PostgreSQL")
        kv = KeyVaults("Key Vault")
    edge >> Edge(label="HTTPS") >> app
    app >> Edge(label="TLS") >> db
    app >> Edge(label="Secrets") >> kv
```
