github : https://github.com/bernt-matthias/mb-galaxy-tools/tree/master/tools/checkm 
this tool relies on the DB in a specific, hardcoded location:
 echo {\"dataRoot\": \"/media/deolivl/QIB_deolivl/nobackup/GTDBTK\", \"remoteManifestURL\": \"https://data.ace.uq.edu.au/public/CheckM_databases/\", \"manifestType\": \"CheckM\", \"localManifestName\": \".dmanifest\", \"remoteManifestName\": \".dmanifest\"} > \${CONDA_PREFIX}/lib/python2.7/site-packages/checkm/DATA_CONFIG &&

