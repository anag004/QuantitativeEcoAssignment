#!/bin/bash

cat fdi.csv | grep $1 | cut -d, -f${2}
