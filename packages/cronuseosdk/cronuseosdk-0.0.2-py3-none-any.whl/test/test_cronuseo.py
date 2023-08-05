from cronuseosdk import Cronuseo


conuseo = Cronuseo("http://localhost:8080/api/v1", "super", "a7TqzHSln739+fLY4azCdNO0bRvnhp35M/3t2lemr3Q=")
response = conuseo.checkPermission("shashimal20", "read", "sales")
assert response == True