echo commiting with message $1 then pushing and then executing Jenkins job
hg commit -m "$1" && hg push && wget -q http://localhost:8080/job/02-provision%20instance/build?token=secret0
