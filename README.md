# Micro-services for hotspot analysis

This repository contains the following micro-services for hotspot analysis:
1. Overlay: services related to frequency and duration overlay
2. Ranking: services reated to Actor ranking based on efficiency
3. Automation: services related to finding RPA opportunities
4. Bias: services related to ODM bias.
5. Sociogram: services related to generating sociogram and analysis.
6. Loops: services related to find re-works.

# Instructions to run the services:

1. Clone the repository.
2. Install the package requirements: ```pip install -r requirements.txt```
3. Run service: ```python app.py```

# Note: 
1. The services will be accessible on: ```http://0.0.0.0:3030``` after running app.py.
2. Services are deployed and accessible at: ```http://process-min.sl.cloud9.ibm.com:3030```
3. These services can be accessed through CURL as well. 

# Directory structure:

```core/``` -- contains the source code for all services.

```rest_api/``` -- contains the source code for the API hosting and namespaces.

```app.py``` -- code file to start the services.

# Install as module:

1. ```conda create -y -n hotspot python=3.6```
2. ```conda activate hotspot```
3. ```conda install pip```
4. ```pip install git+ssh://git@github.ibm.com/research-dba/baox-services.git```

OR

1. ```git clone git@github.ibm.com:research-dba/baox-services.git```
2. ```cd baox-services```
3. ```python setup.py install```

Sample usage of the module: https://github.ibm.com/research-dba/baox-notebooks/blob/master/sample_usage_as_module.ipynb

Sample data can be found at: https://github.ibm.com/research-dba/baox-data-simulations/tree/master/data


To uninstall the module: ```pip uninstall hotspot-analysis```
