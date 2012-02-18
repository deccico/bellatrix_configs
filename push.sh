echo commiting with message $1
hg commit -m "$1" && hg push && wget http://localhost:8080/job/02-provision%20instance/build?token=secret0
