Training network
2023-05-07 15:51:49.203337: I tensorflow/stream_executor/cuda/cuda_dnn.cc:384] Loaded cuDNN version 8200
step 0 | training: 0.02402, test: 24.05 | content: 19.46, mse: 0.09176, psnr: 10.51, ms-ssim: 0.3397

step 1000 | training: 11.36, test: 9.972 | content: 9.285, mse: 0.01373, psnr: 18.92, ms-ssim: 0.8841

step 2000 | training: 7.845, test: 8.425 | content: 7.812, mse: 0.01227, psnr: 19.46, ms-ssim: 0.8883

step 3000 | training: 6.858, test: 7.648 | content: 7.084, mse: 0.01126, psnr: 19.84, ms-ssim: 0.8929

step 4000 | training: 6.022, test: 6.864 | content: 6.299, mse: 0.0113, psnr: 19.81, ms-ssim: 0.8962

step 5000 | training: 5.489, test: 6.236 | content: 5.639, mse: 0.01194, psnr: 19.65, ms-ssim: 0.8962

step 6000 | training: 5.229, test: 6.048 | content: 5.469, mse: 0.01158, psnr: 19.85, ms-ssim: 0.8987


Training network
2023-05-07 18:25:32.616451: I tensorflow/stream_executor/cuda/cuda_dnn.cc:384] Loaded cuDNN version 8200
step 6000 | training: 0.004482, test: 6.184 | content: 5.594, mse: 0.0118, psnr: 19.75, ms-ssim: 0.8993

step 7000 | training: 4.946, test: 5.633 | content: 5.108, mse: 0.01051, psnr: 20.18, ms-ssim: 0.9018

step 8000 | training: 4.847, test: 5.74 | content: 5.17, mse: 0.0114, psnr: 19.81, ms-ssim: 0.8961

step 9000 | training: 4.722, test: 5.493 | content: 4.948, mse: 0.0109, psnr: 20.06, ms-ssim: 0.9007

step 10000 | training: 4.541, test: 5.496 | content: 4.977, mse: 0.01039, psnr: 20.17, ms-ssim: 0.9012

step 11000 | training: 4.554, test: 5.268 | content: 4.718, mse: 0.01098, psnr: 20.01, ms-ssim: 0.8995

step 12000 | training: 4.533, test: 5.379 | content: 4.829, mse: 0.01101, psnr: 20.03, ms-ssim: 0.9011


Training network
2023-05-07 20:41:11.646545: I tensorflow/stream_executor/cuda/cuda_dnn.cc:384] Loaded cuDNN version 8200
step 12000 | training: 0.00379, test: 5.484 | content: 4.906, mse: 0.01156, psnr: 19.81, ms-ssim: 0.8997

step 13000 | training: 4.39, test: 5.145 | content: 4.632, mse: 0.01025, psnr: 20.29, ms-ssim: 0.9025

step 14000 | training: 4.375, test: 5.21 | content: 4.667, mse: 0.01086, psnr: 20.02, ms-ssim: 0.8994

step 15000 | training: 4.311, test: 5.07 | content: 4.541, mse: 0.01059, psnr: 20.17, ms-ssim: 0.9017

step 16000 | training: 4.183, test: 6.38 | content: 5.79, mse: 0.01181, psnr: 19.57, ms-ssim: 0.8938

step 17000 | training: 4.266, test: 5.147 | content: 4.52, mse: 0.01255, psnr: 19.53, ms-ssim: 0.8986

step 18000 | training: 4.206, test: 5.039 | content: 4.49, mse: 0.01097, psnr: 20.11, ms-ssim: 0.903

Traceback (most recent call last):
  File "train_model.py", line 225, in <module>
    train_data, train_answ = load_training_batch(dataset_dir, train_size, PATCH_WIDTH, PATCH_HEIGHT, DSLR_SCALE)
  File "/home/dr_seyma_gngr/projects/PyNET/load_dataset.py", line 68, in load_training_batch
    train_data = np.zeros((TRAIN_SIZE, PATCH_WIDTH, PATCH_HEIGHT, 4))
numpy.core._exceptions.MemoryError: Unable to allocate 7.48 GiB for an array with shape (5000, 224, 224, 4) and data type float64


Training network
2023-05-07 22:57:14.840690: I tensorflow/stream_executor/cuda/cuda_dnn.cc:384]L oaded cUDNN version 8200
step 18000 | training: 0.003471, test: 5.185 | content: 4.606, me: 0.01158, psnr: 19.95, ms-ssim: 0.901

step 19000 | training: 4.126, test: 4.986 | content: 4.468, mse: 0.01037, psnr:20.23, ms-ssim: 0.9021

step 20000 | training: 4.121, test: 5.05 | content: 4.511, mse: 0.01078, psnr: 20.1, ms-ssim: 0.9006

step 21000 | training: 4.08, test: 4.876 | content: 4.355, mse: 0.01041, psnr: 20.21, ms-ssim: 0.9027

step 22000 | training: 3.947, test: 4.926 | content: 4.428, mse: 0.009955, psnr:20.37, ms-ssim: 0.9033

step 23000 | training: 3.992, test: 5.01 | content: 4.399, mse: 0.01222, psnr: 19.64, ms-ssim: 0.8997

step 24000 | training: 3.988, test: 4.972 | content: 4.428, mse: 0.01089, psnr:20.14, ms-ssim: 0.9039
Traceback (most recent call last):
  File "train _model.py", line 225, in <module>
    train_data, train_answ = load_training batch(dataset_dir, train_size, PATCH_WIDTH, PATCH_HEIGHT, DSLR_SCALE)
  File "/home/dr_seyma_gngr/projects/PyNET/load_dataset.py",line 68, in load_tr aining_batch
    train_data = np. zeros ((TRAIN_SIZE, PATCH_ WIDTH, PATCH_HEIGHT, 4))
numpy.core._exceptions. MemoryError: Unable to allocate 7.48 GiB for an array wit h shape (5000, 224, 224, 4) and data type float64


Training network
2023-05-08 04:20:04.573677: I tensorflow/stream_executor/cuda/cuda_dnn.cc:384] Loaded cuDNN version 8200
step 24000 | training: 0.00338, test: 5.002 | content: 4.438, mse: 0.01127, psnr: 20.05, ms-ssim: 0.9021

step 25000 | training: 3.896, test: 4.893 | content: 4.382, mse: 0.01021, psnr: 20.32, ms-ssim: 0.9027

step 26000 | training: 3.907, test: 4.916 | content: 4.386, mse: 0.0106, psnr: 20.18, ms-ssim: 0.9008

step 27000 | training: 3.853, test: 4.792 | content: 4.257, mse: 0.01069, psnr: 20.12, ms-ssim: 0.9028

step 28000 | training: 3.755, test: 4.884 | content: 4.359, mse: 0.0105, psnr: 20.18, ms-ssim: 0.9041

step 29000 | training: 3.803, test: 4.948 | content: 4.32, mse: 0.01256, psnr: 19.54, ms-ssim: 0.8987

step 30000 | training: 3.797, test: 4.883 | content: 4.323, mse: 0.01121, psnr: 20.05, ms-ssim: 0.9042

Traceback (most recent call last):
  File "train_model.py", line 225, in <module>
    train_data, train_answ = load_training_batch(dataset_dir, train_size, PATCH_WIDTH, PATCH_HEIGHT, DSLR_SCALE)
  File "/home/dr_seyma_gngr/projects/PyNET/load_dataset.py", line 68, in load_training_batch
    train_data = np.zeros((TRAIN_SIZE, PATCH_WIDTH, PATCH_HEIGHT, 4))
numpy.core._exceptions.MemoryError: Unable to allocate 7.48 GiB for an array with shape (5000, 224, 224, 4) and data type float64


Training network
2023-05-08 06:36:43.428180: I tensorflow/stream_executor/cuda/cuda_dnn.cc:384] Loaded cuDNN version 8200
step 30000 | training: 0.003077, test: 4.985 | content: 4.394, mse: 0.01181, psnr: 19.89, ms-ssim: 0.9021

step 31000 | training: 3.703, test: 4.827 | content: 4.311, mse: 0.01032, psnr: 20.28, ms-ssim: 0.902

step 32000 | training: 3.721, test: 4.911 | content: 4.353, mse: 0.01115, psnr: 20, ms-ssim: 0.8992

step 33000 | training: 3.676, test: 4.769 | content: 4.236, mse: 0.01066, psnr: 20.14, ms-ssim: 0.9026

step 34000 | training: 3.584, test: 4.874 | content: 4.353, mse: 0.01041, psnr: 20.18, ms-ssim: 0.9033

step 35000 | training: 3.629, test: 4.76 | content: 4.198, mse: 0.01123, psnr: 19.94, ms-ssim: 0.9019

step 36000 | training: 3.632, test: 4.836 | content: 4.284, mse: 0.01103, psnr: 20.04, ms-ssim: 0.9039

Traceback (most recent call last):
  File "train_model.py", line 225, in <module>
    train_data, train_answ = load_training_batch(dataset_dir, train_size, PATCH_WIDTH, PATCH_HEIGHT, DSLR_SCALE)
  File "/home/dr_seyma_gngr/projects/PyNET/load_dataset.py", line 68, in load_training_batch
    train_data = np.zeros((TRAIN_SIZE, PATCH_WIDTH, PATCH_HEIGHT, 4))
numpy.core._exceptions.MemoryError: Unable to allocate 7.48 GiB for an array with shape (5000, 224, 224, 4) and data type float64



Training network
2023-05-08 09:01:37.067513: I tensorflow/stream_executor/cuda/cuda_dnn.cc:384] Loaded cuDNN version 8200
step 36000 | training: 0.002898, test: 5.081 | content: 4.47, mse: 0.01223, psnr: 19.72, ms-ssim: 0.9023

step 37000 | training: 3.549, test: 4.782 | content: 4.253, mse: 0.01057, psnr: 20.15, ms-ssim: 0.9022

step 38000 | training: 3.562, test: 4.856 | content: 4.297, mse: 0.01116, psnr: 19.98, ms-ssim: 0.8986

step 39000 | training: 3.526, test: 4.74 | content: 4.212, mse: 0.01055, psnr: 20.15, ms-ssim: 0.902

step 40000 | training: 3.445, test: 4.871 | content: 4.358, mse: 0.01025, psnr: 20.26, ms-ssim: 0.9032

step 41000 | training: 3.485, test: 4.7 | content: 4.137, mse: 0.01127, psnr: 19.92, ms-ssim: 0.902

step 42000 | training: 3.49, test: 4.856 | content: 4.295, mse: 0.01123, psnr: 20, ms-ssim: 0.9038

Traceback (most recent call last):
  File "train_model.py", line 225, in <module>
    train_data, train_answ = load_training_batch(dataset_dir, train_size, PATCH_WIDTH, PATCH_HEIGHT, DSLR_SCALE)
  File "/home/dr_seyma_gngr/projects/PyNET/load_dataset.py", line 68, in load_training_batch
    train_data = np.zeros((TRAIN_SIZE, PATCH_WIDTH, PATCH_HEIGHT, 4))
numpy.core._exceptions.MemoryError: Unable to allocate 7.48 GiB for an array with shape (5000, 224, 224, 4) and data type float64



Training network
2023-05-08 11:20:36.724661: I tensorflow/stream_executor/cuda/cuda_dnn.cc:384]L oaded cUDNN version 8200
step 42000 | training: 0.002806, test: 4.907 | content: 4.337, mse: 0.0114, psnr :19.98, ms-ssim: 0.9026

step 43000 | training: 3.414, test: 4.772 | content: 4.237, mse: 0.0107, psnr:20.06, ms-ssim: 0.9027

step 44000 | training: 3.434, test: 4.904 | content: 4.299, mse: 0.01209, psnr:19.67, ms-ssim: 0.8973

step 45000 | training: 3.412, test: 4.774 | content: 4.236, mse: 0.01077, psnr:20.08, ms-ssim: 0.901

step 46000 | training: 3.327, test: 4.759 | content: 4.242, mse: 0.01033, psnr:20.25, ms-ssim: 0.9026

step 47000 | training: 3.367, test: 4.715 | content: 4.147, mse: 0.01136, psnr:19.88, ms-ssim: 0.9018

step 48000 | training: 3.356, test: 4.877 | content: 4.31, mse: 0.01133, psnr: 19.96, ms-ssim: 0.9026

Traceback (most recent call last):
  File "train_model.py", line 225, in <module>
    train_data, train_answ = load_training_batch (dataset_dir, train_size, PATCH_WIDTH, PATCH_HEIGHT, DSLR_SCALE)
  File "/home/dr_seyma_gngr/projects/PyNET/load_dataset.py", line 68, in load tr aining_batch
    train_data = np. zeros ((TRAIN_SIZE, PATCH_ WIDTH, PATCH_HEIGHT, 4))
numpy.core._exceptions.MemoryError: Unable to allocate 7.48 GiB for an array wit h shape (5000,224, 224,4) and data type float64



Loading training data...
Training data was loaded

Training network
2023-05-08 13:48:39.157327: I tensorflow/stream_executor/cuda/cuda_dnn.cc:384] Loaded cuDNN version 8200
step 48000 | training: 0.002761, test: 4.974 | content: 4.385, mse: 0.01177, psnr: 19.86, ms-ssim: 0.9024

step 49000 | training: 3.3, test: 4.762 | content: 4.206, mse: 0.01112, psnr: 19.9, ms-ssim: 0.9025

step 50000 | training: 3.312, test: 4.932 | content: 4.327, mse: 0.01212, psnr: 19.65, ms-ssim: 0.8978