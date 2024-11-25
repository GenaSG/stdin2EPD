#!/bin/bash
zip -x ./env/**\* -x ./**/__pycache__/**\* -x build.sh -r ../stdin2EPD.zip *
echo '#!/usr/bin/env python3' | cat - ../stdin2EPD.zip > ../stdin2EPD.pyz
chmod +x ../stdin2EPD.pyz 
