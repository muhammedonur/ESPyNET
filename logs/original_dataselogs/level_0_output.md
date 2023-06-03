step 0 | training: 0.02135, test: 22.06 | content: 10.29, mse: 0.09292, psnr: 10.45, ms-ssim: 0.4441

step 1000 | training: 11.87, test: 12.29 | content: 6.411, mse: 0.01514, psnr: 18.6, ms-ssim: 0.8385

step 2000 | training: 10.05, test: 11.68 | content: 5.885, mse: 0.01536, psnr: 18.56, ms-ssim: 0.8425

step 3000 | training: 9.86, test: 11.28 | content: 5.554, mse: 0.01435, psnr: 18.89, ms-ssim: 0.8448

Traceback (most recent call last):
  File "train_model.py", line 225, in <module>
    train_data, train_answ = load_training_batch(dataset_dir, train_size, PATCH_WIDTH, PATCH_HEIGHT, DSLR_SCALE)
  File "/home/dr_seyma_gngr/projects/PyNET/load_dataset.py", line 68, in load_training_batch
    train_data = np.zeros((TRAIN_SIZE, PATCH_WIDTH, PATCH_HEIGHT, 4))
numpy.core._exceptions.MemoryError: Unable to allocate 7.48 GiB for an array with shape (5000, 224, 224, 4) and data type float64


step 3000 | training: 0.008993, test: 11.35 | content: 5.55, mse: 0.01421, psnr: 18.93, ms-ssim: 0.8467

step 4000 | training: 9.152, test: 11.05 | content: 5.286, mse: 0.01309, psnr: 19.17, ms-ssim: 0.8496

step 6000 | training: 0.008607, test: 10.74 | content: 5.048, mse: 0.01239, psnr: 19.37, ms-ssim: 0.8513

step 7000 | training: 8.538, test: 10.64 | content: 5.02, mse: 0.01305, psnr: 19.21, ms-ssim: 0.852

step 8000 | training: 8.574, test: 10.52 | content: 4.925, mse: 0.01296, psnr: 19.27, ms-ssim: 0.8498

step 8000 | training: 0.008137, test: 10.75 | content: 4.942, mse: 0.01367, psnr: 19.02, ms-ssim: 0.8506

step 9000 | training: 8.215, test: 10.37 | content: 4.806, mse: 0.01299, psnr: 19.24, ms-ssim: 0.8542

step 10000 | training: 8.203, test: 10.27 | content: 4.693, mse: 0.01333, psnr: 19.2, ms-ssim: 0.851

step 10000 | training: 0.007642, test: 10.46 | content: 4.757, mse: 0.01329, psnr: 19.13, ms-ssim: 0.8519

step 11000 | training: 8.017, test: 10.36 | content: 4.827, mse: 0.01318, psnr: 19.19, ms-ssim: 0.8539

step 12000 | training: 8.027, test: 10.21 | content: 4.618, mse: 0.01332, psnr: 19.2, ms-ssim: 0.8511

step 12000 | training: 0.007423, test: 10.74 | content: 4.849, mse: 0.01361, psnr: 19.14, ms-ssim: 0.8497

step 13000 | training: 7.871, test: 10.21 | content: 4.664, mse: 0.01326, psnr: 19.22, ms-ssim: 0.8549

step 14000 | training: 7.879, test: 10.16 | content: 4.569, mse: 0.0135, psnr: 19.12, ms-ssim: 0.8507

step 14000 | training: 0.007321, test: 10.5 | content: 4.781, mse: 0.01332, psnr: 19.18, ms-ssim: 0.8527

step 15000 | training: 7.77, test: 10.35 | content: 4.626, mse: 0.01355, psnr: 19.15, ms-ssim: 0.8537

step 16000 | training: 7.779, test: 10.11 | content: 4.565, mse: 0.01291, psnr: 19.32, ms-ssim: 0.8521

step 16000 | training: 0.007271, test: 10.25 | content: 4.624, mse: 0.01373, psnr: 19.05, ms-ssim: 0.8502

step 17000 | training: 7.649, test: 10.27 | content: 4.619, mse: 0.01366, psnr: 19.1, ms-ssim: 0.8541

step 18000 | training: 7.679, test: 10.08 | content: 4.55, mse: 0.01264, psnr: 19.41, ms-ssim: 0.8534

step 18000 | training: 0.007096, test: 10.08 | content: 4.561, mse: 0.01218, psnr: 19.52, ms-ssim: 0.8531

step 19000 | training: 7.614, test: 10 | content: 4.538, mse: 0.01233, psnr: 19.46, ms-ssim: 0.8547

step 20000 | training: 7.638, test: 10.05 | content: 4.491, mse: 0.01284, psnr: 19.37, ms-ssim: 0.8529

step 20000 | training: 0.007035, test: 10.33 | content: 4.591, mse: 0.01337, psnr: 19.22, ms-ssim: 0.8516

step 21000 | training: 7.562, test: 9.972 | content: 4.492, mse: 0.0122, psnr: 19.53, ms-ssim: 0.8548

step 22000 | training: 7.536, test: 10 | content: 4.474, mse: 0.01284, psnr: 19.36, ms-ssim: 0.8525

step 22000 | training: 0.006835, test: 10.35 | content: 4.595, mse: 0.01316, psnr: 19.26, ms-ssim: 0.8525

step 23000 | training: 7.491, test: 10.12 | content: 4.559, mse: 0.01226, psnr: 19.53, ms-ssim: 0.8532

step 24000 | training: 7.478, test: 9.977 | content: 4.454, mse: 0.01283, psnr: 19.35, ms-ssim: 0.8517

step 24000 | training: 0.006831, test: 10.12 | content: 4.541, mse: 0.01222, psnr: 19.52, ms-ssim: 0.8534

step 25000 | training: 7.391, test: 10.06 | content: 4.588, mse: 0.0121, psnr: 19.56, ms-ssim: 0.8536

step 26000 | training: 7.387, test: 10.01 | content: 4.442, mse: 0.0136, psnr: 19.15, ms-ssim: 0.8514

step 26000 | training: 0.006807, test: 10.4 | content: 4.533, mse: 0.01474, psnr: 18.86, ms-ssim: 0.8506

step 27000 | training: 7.332, test: 9.991 | content: 4.523, mse: 0.01217, psnr: 19.55, ms-ssim: 0.8548

step 28000 | training: 7.342, test: 10.05 | content: 4.447, mse: 0.01423, psnr: 19.07, ms-ssim: 0.8515

step 28000 | training: 0.006797, test: 10 | content: 4.424, mse: 0.01301, psnr: 19.33, ms-ssim: 0.8535

step 29000 | training: 7.269, test: 10.03 | content: 4.553, mse: 0.01275, psnr: 19.3, ms-ssim: 0.8547

step 30000 | training: 7.27, test: 9.937 | content: 4.42, mse: 0.01317, psnr: 19.31, ms-ssim: 0.8534

step 30000 | training: 0.006561, test: 10.44 | content: 4.519, mse: 0.01518, psnr: 18.75, ms-ssim: 0.8489

step 31000 | training: 7.222, test: 10.12 | content: 4.63, mse: 0.01292, psnr: 19.25, ms-ssim: 0.8554

step 32000 | training: 7.203, test: 10.02 | content: 4.423, mse: 0.01399, psnr: 19.07, ms-ssim: 0.8522

step 32000 | training: 0.006495, test: 9.988 | content: 4.465, mse: 0.01268, psnr: 19.4, ms-ssim: 0.8537

step 33000 | training: 7.164, test: 10.09 | content: 4.581, mse: 0.01259, psnr:19.39, ms-ssim: 0.8557

step 34000 | training: 7.166, test: 9.924 | content: 4.421, mse: 0.01296, psnr:19.38, ms-ssim: 0.854

step 34000 | training: 0.006434, test: 10.25 | content: 4.471, mse: 0.01452, psnr: 18.92, ms-ssim: 0.8501

step 35000 | training: 7.14, test: 9.968 | content: 4.517, mse: 0.01201, psnr: 19.63, ms-ssim: 0.8555

step 36000 | training: 7.136, test: 9.895 | content: 4.422, mse: 0.0128, psnr: 19.43, ms-ssim: 0.8545

step 36000 | training: 0.006439, test: 10.37 | content: 4.474, mse: 0.015, psnr: 18.81, ms-ssim: 0.8507

step 37000 | training: 7.091, test: 9.897 | content: 4.463, mse: 0.012, psnr: 19.61, ms-ssim: 0.8547

step 38000 | training: 7.099, test: 9.892 | content: 4.443, mse: 0.01237, psnr:19.51, ms-ssim: 0.8546

step 38000 | training: 0.006407, test: 10 | content: 4.446, mse: 0.01238, psnr: 19.46, ms-ssim: 0.8526

step 39000 | training: 7.013, test: 9.892 | content: 4.455, mse: 0.0121, psnr: 19.52, ms-ssim: 0.8549

step 40000 | training: 7.034, test: 9.919 | content: 4.446, mse: 0.01265, psnr: 19.42, ms-ssim: 0.854

step 40000 | training: 0.006363, test: 10.17 | content: 4.459, mse: 0.01368, psnr: 19.14, ms-ssim: 0.8519

step 41000 | training: 6.943, test: 10.08 | content: 4.569, mse: 0.01255, psnr: 19.38, ms-ssim: 0.8539

step 42000 | training: 6.952, test: 9.952 | content: 4.469, mse: 0.01272, psnr: 19.41, ms-ssim: 0.8532

Bu kısmın logları eksik

step 44000 | training: 0.006326, test: 10.17 | content: 4.518, mse: 0.01271, psnr: 19.4, ms-ssim: 0.8539

step 45000 | training: 6.893, test: 10.03 | content: 4.525, mse: 0.01185, psnr: 19.62, ms-ssim: 0.8533

step 46000 | training: 6.886, test: 9.871 | content: 4.448, mse: 0.01171, psnr: 19.71, ms-ssim: 0.8555

step 46000 | training: 0.006116, test: 9.882 | content: 4.415, mse: 0.01187, psnr: 19.63, ms-ssim: 0.8535

step 47000 | training: 6.845, test: 9.906 | content: 4.475, mse: 0.01149, psnr: 19.76, ms-ssim: 0.8541

step 48000 | training: 6.869, test: 9.857 | content: 4.446, mse: 0.01177, psnr: 19.68, ms-ssim: 0.8553

step 48000 | training: 0.006208, test: 10.19 | content: 4.484, mse: 0.0137, psnr: 19.1, ms-ssim: 0.8513

step 49000 | training: 6.856, test: 9.924 | content: 4.468, mse: 0.01224, psnr: 19.51, ms-ssim: 0.8539

step 50000 | training: 6.837, test: 9.911 | content: 4.427, mse: 0.01316, psnr: 19.42, ms-ssim: 0.8552

step 50000 | training: 0.006151, test: 10.03 | content: 4.447, mse: 0.01404, psnr: 19.18, ms-ssim: 0.8537

step 51000 | training: 6.814, test: 9.893 | content: 4.471, mse: 0.01173, psnr: 19.67, ms-ssim: 0.8549

step 52000 | training: 6.787, test: 9.887 | content: 4.457, mse: 0.0118, psnr: 19.67, ms-ssim: 0.8553

step 52000 | training: 0.006154, test: 9.838 | content: 4.412, mse: 0.01172, psnr: 19.67, ms-ssim: 0.8551

step 53000 | training: 6.772, test: 9.867 | content: 4.444, mse: 0.01185, psnr: 19.66, ms-ssim: 0.8542

step 54000 | training: 6.754, test: 9.851 | content: 4.423, mse: 0.01217, psnr: 19.55, ms-ssim: 0.8551

step 54000 | training: 0.00603, test: 10.02 | content: 4.471, mse: 0.01255, psnr: 19.42, ms-ssim: 0.854

step 55000 | training: 6.719, test: 9.885 | content: 4.443, mse: 0.01175, psnr: 19.69, ms-ssim: 0.8538

step 56000 | training: 6.713, test: 9.911 | content: 4.443, mse: 0.01321, psnr: 19.35, ms-ssim: 0.8554

step 56000 | training: 0.006081, test: 9.93 | content: 4.42, mse: 0.01283, psnr: 19.4, ms-ssim: 0.8543

step 57000 | training: 6.682, test: 9.948 | content: 4.474, mse: 0.01198, psnr: 19.6, ms-ssim: 0.8528

step 58000 | training: 6.698, test: 9.805 | content: 4.407, mse: 0.01192, psnr: 19.61, ms-ssim: 0.8561

step 58000 | training: 0.005964, test: 10.05 | content: 4.546, mse: 0.01206, psnr: 19.56, ms-ssim: 0.8551

step 59000 | training: 6.664, test: 10 | content: 4.504, mse: 0.01191, psnr: 19.59, ms-ssim: 0.8529

step 60000 | training: 6.682, test: 9.802 | content: 4.391, mse: 0.01192, psnr: 19.62, ms-ssim: 0.8557

step 60000 | training: 0.005921, test: 9.952 | content: 4.46, mse: 0.01212, psnr: 19.57, ms-ssim: 0.855

step 61000 | training: 6.648, test: 9.965 | content: 4.487, mse: 0.01209, psnr: 19.54, ms-ssim: 0.8544

step 62000 | training: 6.629, test: 9.857 | content: 4.407, mse: 0.01243, psnr:19.45, ms-ssim: 0.8552

step 62000 | training: 0.005827, test: 10.01 | content: 4.498, mse: 0.01275, psnr: 19.32, ms-ssim: 0.8546

step 63000 | training: 6.588, test: 9.851 | content: 4.452, mse: 0.01176, psnr: 19.67, ms-ssim: 0.8557

step 64000 | training: 6.57, test: 9.814 | content: 4.401, mse: 0.01196, psnr: 19.61, ms-ssim: 0.8553

step 64000 | training: 0.005862, test: 9.897 | content: 4.423, mse: 0.01215, psnr: 19.5, ms-ssim: 0.8545

step 65000 | training: 6.536, test: 9.91 | content: 4.521, mse: 0.01173, psnr: 19.69, ms-ssim: 0.8566

step 66000 | training: 6.535, test: 9.835 | content: 4.417, mse: 0.01211, psnr: 19.54, ms-ssim: 0.8557

step 66000 | training: 0.0058, test: 9.954 | content: 4.478, mse: 0.01205, psnr: 19.56, ms-ssim: 0.8551

step 67000 | training: 6.512, test: 9.973 | content: 4.56, mse: 0.01187, psnr: 19.64, ms-ssim: 0.8561

step 68000 | training: 6.52, test: 9.964 | content: 4.446, mse: 0.01281, psnr: 19.31, ms-ssim: 0.8547

step 68000 | training: 0.005953, test: 9.942 | content: 4.474, mse: 0.01227, psnr: 19.47, ms-ssim: 0.8543

step 69000 | training: 6.468, test: 9.916 | content: 4.511, mse: 0.01205, psnr: 19.56, ms-ssim: 0.8561

step 70000 | training: 6.481, test: 9.883 | content: 4.424, mse: 0.01236, psnr: 19.44, ms-ssim: 0.8547

step 70000 | training: 0.005767, test: 10.05 | content: 4.519, mse: 0.01295, psnr: 19.23, ms-ssim: 0.854

step 71000 | training: 6.426, test: 9.997 | content: 4.584, mse: 0.01209, psnr: 19.55, ms-ssim: 0.856

step 72000 | training: 6.458, test: 9.972 | content: 4.482, mse: 0.0132, psnr: 19.37, ms-ssim: 0.854

step 72000 | training: 0.005805, test: 9.971 | content: 4.458, mse: 0.01302, psnr: 19.4, ms-ssim: 0.8547

step 73000 | training: 6.427, test: 9.993 | content: 4.558, mse: 0.01233, psnr: 19.49, ms-ssim: 0.8554

step 74000 | training: 6.456, test: 9.887 | content: 4.463, mse: 0.01213, psnr: 19.53, ms-ssim: 0.8553

step 74000 | training: 0.005758, test: 9.878 | content: 4.413, mse: 0.01214, psnr: 19.53, ms-ssim: 0.8536

step 75000 | training: 6.417, test: 10.03 | content: 4.526, mse: 0.01179, psnr: 19.71, ms-ssim: 0.8548

step 76000 | training: 6.453, test: 9.865 | content: 4.444, mse: 0.01191, psnr: 19.6, ms-ssim: 0.8555

step 76000 | training: 0.00569, test: 9.971 | content: 4.497, mse: 0.01213, psnr: 19.53, ms-ssim: 0.8548

step 77000 | training: 6.384, test: 9.933 | content: 4.51, mse: 0.01169, psnr: 19.7, ms-ssim: 0.8551

step 78000 | training: 6.418, test: 9.905 | content: 4.466, mse: 0.01217, psnr: 19.56, ms-ssim: 0.8547

step 78000 | training: 0.005697, test: 9.893 | content: 4.448, mse: 0.01213, psnr: 19.57, ms-ssim: 0.8551

step 79000 | training: 6.378, test: 9.851 | content: 4.457, mse: 0.01162, psnr: 19.73, ms-ssim: 0.8557

step 80000 | training: 6.391, test: 9.924 | content: 4.461, mse: 0.01301, psnr: 19.44, ms-ssim: 0.8548

step 80000 | training: 0.005701, test: 10.04 | content: 4.48, mse: 0.01372, psnr: 19.25, ms-ssim: 0.8537

step 81000 | training: 6.337, test: 9.846 | content: 4.443, mse: 0.01182, psnr: 19.68, ms-ssim: 0.8555

step 82000 | training: 6.369, test: 9.912 | content: 4.475, mse: 0.01179, psnr: 19.66, ms-ssim: 0.8547

step 82000 | training: 0.005712, test: 9.878 | content: 4.438, mse: 0.01192, psnr: 19.62, ms-ssim: 0.8549

step 83000 | training: 6.334, test: 9.904 | content: 4.41, mse: 0.01186, psnr: 19.61, ms-ssim: 0.8539

step 84000 | training: 6.364, test: 9.926 | content: 4.479, mse: 0.01187, psnr: 19.66, ms-ssim: 0.854

step 84000 | training: 0.005665, test: 9.924 | content: 4.467, mse: 0.01222, psnr: 19.54, ms-ssim: 0.8548

step 85000 | training: 6.291, test: 9.924 | content: 4.468, mse: 0.01193, psnr: 19.59, ms-ssim: 0.8534

step 86000 | training: 6.312, test: 9.886 | content: 4.475, mse: 0.01162, psnr: 19.74, ms-ssim: 0.8543

step 86000 | training: 0.005584, test: 9.875 | content: 4.463, mse: 0.01165, psnr: 19.72, ms-ssim: 0.8551

step 88000 | training: 0.005564, test: 9.846 | content: 4.435, mse: 0.01167, psnr: 19.7, ms-ssim: 0.8551

step 89000 | training: 6.265, test: 10 | content: 4.558, mse: 0.01204, psnr: 19.57, ms-ssim: 0.8538

step 90000 | training: 6.29, test: 9.82 | content: 4.417, mse: 0.01183, psnr: 19.66, ms-ssim: 0.8553