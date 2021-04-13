Tools:
-------
Install following tools on your machine:

1. Docker
   - https://docs.docker.com/get-docker/

2. VirtualBox
   - https://www.virtualbox.org/wiki/Downloads

3. kubectl
   - https://kubernetes.io/docs/tasks/tools/

4. Minikube
    MacOS:
    - wget https://github.com/kubernetes/minikube/releases/download/v1.15.0/minikube-darwin-amd64
    - chmod +x minikube-darwin-amd64
    Linux:
    - wget https://github.com/kubernetes/minikube/releases/download/v1.15.0/minikube-linux-amd64
    - chmod +x minikube-linux-amd64

5. Helm (version3)
   - https://helm.sh/docs/intro/install/

6. Google Cloud CLI
   - gcloud 

7. KubePlus kubectl plugins for cluster discovery (only available for MacOS and Linux)
   (available at: https://github.com/cloud-ark/kubeplus). 
   ```
   - wget https://github.com/cloud-ark/kubeplus/raw/master/kubeplus-kubectl-plugins.tar.gz
   - gunzip kubeplus-kubectl-plugins.tar.gz
   - tar -xvf kubeplus-kubectl-plugins.tar
   - export KUBEPLUS_HOME=`pwd`
   - export PATH=$KUBEPLUS_HOME/plugins/:$PATH
   - Verify: kubectl kubeplus commands
     - You should see list of all the available plugin commands
   ```

