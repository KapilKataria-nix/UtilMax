from kubernetes import client,config
#load KKubernetes configuration
config.load_kube_config()

#Create a Kubernetes API client
api_client = client.ApiClient()


#Creating Deployment

deployment = client.VlDeployement(
    metadata = client.VlObjectMeta(name= 'aws-flask-app'),
    spec = client.VlDeployementSpec(
        replicas=1,
        selector=client.VlLabelSelector(
            match_labels={"app": "aws-flask-app"}
        ),
        template = client.VlPodTemplateSpec(
            metadata = client.VlObjectMeta(
                labels={"app":"aws-flask-app"}

            ),
            spec=client.VlPodSpec(
                conntainer=[
                    client.VlContainer(
                        name="aws-flask-container",
                        image="997846889746.dkr.ecr.ap-south-1.amazonaws.com/cloud-native-repo:latest",
                        ports=[client.VlContainerPort(container_port=5000)]
                    )
                ]
            )
        )

    )
)


#Crate the deployment

api_instance = client.AppVlApi(api_client)
api_instance.create_namespaced_deployment(
    namespace="default",
    body = deployment
)

# Define the service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="my-flask-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "aws-flask-app"},
        ports=[client.V1ServicePort(port=5000)]
    )
)

# Create the service
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)