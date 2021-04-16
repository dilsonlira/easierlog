#!/bin/sh

# Build and run a container from a local Dockerfile

project_name=$(pwd | rev | cut -d "/" -f1 | rev)

if mypy $project_name; then

    if test -f Dockerfile; then
        docker build -t $project_name .

        if [ "$1" = "d" ]; then
            # Debug mode
            docker run -it --rm $project_name sh
        else
            docker run --rm $project_name
        fi

    else
        echo "There is no Dockerfile in the current directory."
    fi
fi
