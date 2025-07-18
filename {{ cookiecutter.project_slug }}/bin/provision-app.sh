#!/bin/bash

# init doctl
doctl auth init

# create app
doctl apps create --spec digitalocean.yaml
