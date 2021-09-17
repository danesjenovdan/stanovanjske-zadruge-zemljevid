#!/bin/bash

sudo docker login rg.fr-par.scw.cloud/djnd -u nologin -p $SCW_SECRET_TOKEN

# BUILD AND PUBLISH STANOVANJSKE ZADRUGE ZEMLJEVID
sudo docker build -f stanovanjskeZadrugeZemljevidApi/Dockerfile -t stanovanjske-zadruge-zemljevid:latest ./stanovanjskeZadrugeZemljevidApi
sudo docker tag stanovanjske-zadruge-zemljevid:latest rg.fr-par.scw.cloud/djnd/stanovanjske-zadruge-zemljevid:latest
sudo docker push rg.fr-par.scw.cloud/djnd/stanovanjske-zadruge-zemljevid:latest

sudo docker build -f front/Dockerfile -t stanovanjske-zadruge-zemljevid-frontend:latest ./front
sudo docker tag stanovanjske-zadruge-zemljevid-frontend:latest rg.fr-par.scw.cloud/djnd/stanovanjske-zadruge-zemljevid-frontend:latest
sudo docker push rg.fr-par.scw.cloud/djnd/stanovanjske-zadruge-zemljevid-frontend:latest
