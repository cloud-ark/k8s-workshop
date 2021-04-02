GKE Cheat sheet:
----------------

1) How to enable traffic for Services that are of type NodePort on GKE?
A) Login to GCP console

   - Go to Kubernetes Engine -> Clusters -> Note down cluster name ("Name")
   
   -  Go to VPC Network -> Firewall -> Select the rule that has following name:
      gke-cluster_name-<string of letters+numbers>-all
   -> Hit Edit
   -> In the Source IP ranges, enter: 0.0.0.0/0
   -> Hit Save

