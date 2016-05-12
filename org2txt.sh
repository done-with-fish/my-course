#!/bin/bash

find $1 -type f -iname "*.org" -print0 | parallel -0 org2txt
