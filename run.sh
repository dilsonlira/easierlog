#!/bin/sh

# Build and run a container from a local Dockerfile

image_name=$(echo $(pwd) | rev | cut -d "/" -f1 | rev)

if test -f Dockerfile; then
    docker build -t $image_name .

    if [[ $1 = "d" ]]; then
        # Debug mode
        docker run -it --rm $image_name sh
    else
        docker run --rm $image_name
    fi

else
    echo "There is no Dockerfile in the current directory."
fi
