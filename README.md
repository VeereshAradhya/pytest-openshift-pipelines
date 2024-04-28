# pytest-openshift-pipelines
Project to test Openshift Pipelines using pytest


### Prerequisites
Install virtual environment
```
pip install vitrualenv
```
Create and activate virtual environment and install required python packages
```
$ virtualenv env
$ source ./env/bin/activate 
$ pip install -U -r requirements.txt
```

### Running tests
* Login to an Openshift Cluster using `oc login` command
* Make sure that the Openshift Pipelines operator is installed
* Run the below command
```
pytest osp/tests/test-pipelinerun.py -v
```
Sample output
```
 pytest osp/tests/test-pipelinerun.py -v -s                                              ✔  pytest-openshift-pipelines Py  11:52:55 PM 
==================================================================================== test session starts =====================================================================================
platform linux -- Python 3.12.2, pytest-8.1.1, pluggy-1.4.0 -- /home/varadhya/workspace/src/github.com/pytest-openshift-pipelines/env/bin/python
cachedir: .pytest_cache
rootdir: /home/varadhya/workspace/src/github.com/pytest-openshift-pipelines
collected 2 items                                                                                                                                                                            

osp/tests/test-pipelinerun.py::TestPipelineruns::test_simple_pipelinerun_success /home/varadhya/workspace/src/github.com/pytest-openshift-pipelines
PASSED
osp/tests/test-pipelinerun.py::TestPipelineruns::test_simple_pipelinerun_failure /home/varadhya/workspace/src/github.com/pytest-openshift-pipelines
PASSED

================================================================
```
