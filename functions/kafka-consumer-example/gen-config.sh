#!/bin/bash

source .env
eval "echo \"$(cat samconfig-template.toml)\"" > samconfig.toml
