#!/bin/bash

parameter=6000

while true; do
    # Run your command line application with the necessary parameters
    python train_model_restore_from_same_level.py level=0 batch_size=8 num_train_iters=100000 restore_iter=$parameter


    # Check the exit code of your application
    if [ $? -eq 0 ]; then
        echo "Application exited successfully"
        break
    else
        echo "Application crashed, restarting..."
        sleep 60 # Wait for 60 seconds before restarting
    fi

    # Update the parameter for the next iteration
    parameter=$((parameter+2000))
done