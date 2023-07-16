import boto3

client = boto3.client('ecr')

repository_name = "cloud-native-repo"
#This wil create a reporsitory in aws
response = client.create_repository(repositoryName = repository_name)

#Storing the repositoryUri 
repository_uri = response['repository']['repositoryUri']

print(repository_uri)


