# Machine_learning_project
This is first Machine learning project

"""
conda create -p <env_name> python == 3.7 -y
"""

"""
conda activate venv/
"""

'''
to check the git status
git status
'''

'''
git commit -m "name"
git push origin main
'''

'''
Docker Build image
docker build -t <image_name>:<tagname> .
NOTE: image name for docker should be lowercase
'''


'''
to list docker images
docker images
'''

'''
To run docker image
docker run -p 5000:5000 -e PORT=5000 b2dcd5c953d2
To delete docker image
docker rmi IMAGE_ID
list of all docker images
docker images
'''

'''
Docker container command
docker ps -a 
docker stop CONTAINER_ID
docker rm CONTAINER_ID
'''

'''
python setup.py install

'''

'''
Artifacts output at each  step or stage of pipeline.In the entity we are going to define each component of pipeline.
Dataingestion Artifact
Datavalidation artifact
Datatransformation artifact
Modeltrainer artifact
modelevaluation artifact
modelpush artifact

The above one will be an output but we also need an input at each component. this is called configuration like
Dataingestion config
Datavalidation config
Datatransformation config
'''

'''
In config folder we will have some files, database, or any information.
'''

'''
Install ipynb kernel
pip install ipykernel
''