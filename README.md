# K8S lab #1


## Goal

Learn basics of Kubernetes by building a simple phonebook service that provides
a REST API over HTTP.

## Requirements

1. Service must be written in Python.
2. The phonebook must be stored persistently in the provided MongoDB database.
3. The service must be deployed in k8s.
4. Users must not experience downtimes when incidents happen.
5. Users must not experience downtimes when new version of the service is deployed.
   
## Important information

1. The server's hostname is sre.romcheg.me.
2. Use `ubuntu` users because this is a new server.
3. Your ssh client may complain that the server's public key has changed. You may need
   to remove the appropriiate line from your `.ssh/known_hosts` file.

## Step 1 - Deploy mongodb using docker-compose

1. Use provided compose file to deploy mongodb and mongo-express - a web admin panel for mongo.
2. Go to the web panel and create a database for the phonebook. Inside the database create
   a new collection for phonebook records.

## Step 2 – Install virtualenv and dependencies

1. Python's dependency management is tricky and quickly becomes messy, if different projects
   try to install dependencies into the host system. This is one of the reasons for
   python apps to be packaged into their own container images.
   
   However, sometimes it is handy to test your python code without running a container.
   For this reason `virtualenv` is used.
   
   Simply run the following:
   
   ```
   virtualenv my_env
   source ./my_env/bin/activate
   ```
   
   to create and activate a python's virtualenvironment. With a virtual environment
   activated. You can safely install dependencies using pip install. Pip will install
   them into a created virtual environment, and not into the system.
   
   To deactivate the environment simply run `deactivate`.
   The environment must be activated for dependencies to be available.

2. Install dependencies
   Run `pip install Flask` and `pip install pymongo` to install required libraries.
3. Use `pip freeze` to generate `requirements.txt`

## Step 3 – Fix the service code

The python code of the service is not complete. Follow the comments to complete it.

## Step 4 – Deploy the service to k8s

1. Create and publish container image
2. Create necessary k8s objects to deploy the service.

Created service must have at least 4 instances. Hint - use deployment to allow
updating the service without downtimes.

Use `kubectl run --rm -it --image docker.io/curlimages/curl -- sh` to run a pod
and to access your API with curl.

## Step 5 – Create a new version of a service

### Step 5.1 

Add a new endpoint to the service:

```
PUT /records/<record id>

Updates a record with a provided id with a new data, provided in a the request body.
```

Use record creation as an example. To update the record in the database
use the `update_one()` collection's method.

### Step 5.2

Build and release a new image (tag it as `phonebook:v2`)

### Step 5.3

Update the image version in the k8s deployment and observe, how it rotates
the pods using kubectl get pods.

## Step 6

Use curl to check the new api like in step 4.

