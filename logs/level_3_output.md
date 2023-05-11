2023-05-06 11:06:35.304033: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-05-06 11:06:37.774540: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
WARNING:tensorflow:From /usr/local/lib/python3.10/dist-packages/tensorflow/python/compat/v2_compat.py:107: disable_resource_variables (from tensorflow.python.ops.variable_scope) is deprecated and will be removed in a future version.
Instructions for updating:
non-resource variables are not supported in the long term
The following parameters will be applied for CNN training:
Training level: 3
Batch size: 48
Learning rate: 5e-05
Training iterations: 20000
Evaluation step: 1000
Restore Iteration: 5000
Path to the dataset: raw_images/
Path to VGG-19 network: vgg_pretrained/imagenet-vgg-verydeep-19.mat
2023-05-06 11:06:41.941117: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 11:06:42.080724: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 11:06:42.081063: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 11:06:42.088139: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 11:06:42.088467: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 11:06:42.088736: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 11:06:44.820545: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 11:06:44.820837: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 11:06:44.821028: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 11:06:44.821191: W tensorflow/core/common_runtime/gpu/gpu_bfc_allocator.cc:47] Overriding orig_value setting because the TF_FORCE_GPU_ALLOW_GROWTH environment variable is set. Original config value was 0.
2023-05-06 11:06:44.824049: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1635] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 14518 MB memory:  -> device: 0, name: Tesla V100-SXM2-16GB, pci bus id: 0000:00:04.0, compute capability: 7.0
Initializing variables
2023-05-06 11:06:56.785634: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:353] MLIR V1 optimization pass is not enabled
Restoring Variables
Loading test data...
Test data was loaded

Loading training data...
Training data was loaded

Training network
2023-05-06 11:08:52.416897: I tensorflow/compiler/xla/stream_executor/cuda/cuda_dnn.cc:424] Loaded cuDNN version 8700
2023-05-06 11:08:58.699981: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 2.85GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 11:08:58.721147: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 2.60GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 11:08:58.750216: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 2.85GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 11:08:58.837724: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 1.28GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 11:08:58.837794: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 1.28GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 11:08:58.866515: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 1.28GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 11:08:58.866577: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 1.28GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 11:08:59.467027: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 2.15GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 11:08:59.467111: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 2.15GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 11:08:59.688668: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 2.27GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
step 0 | training: 0.07338, test: 69.54 | content: 59.74, mse: 0.09805, psnr: 10.1

step 1000 | training: 14.88, test: 10.87 | content: 8.608, mse: 0.02264, psnr: 16.55

step 2000 | training: 9.129, test: 8.71 | content: 7.283, mse: 0.01428, psnr: 18.54

step 3000 | training: 7.856, test: 7.625 | content: 6.459, mse: 0.01165, psnr: 19.45

step 4000 | training: 6.968, test: 7.535 | content: 6.477, mse: 0.01058, psnr: 19.91

step 5000 | training: 6.61, test: 7.274 | content: 6.251, mse: 0.01023, psnr: 20.1

step 6000 | training: 6.422, test: 7.289 | content: 6.317, mse: 0.009723, psnr: 20.36

step 7000 | training: 6.174, test: 6.222 | content: 5.375, mse: 0.008473, psnr: 20.89

step 8000 | training: 5.922, test: 6.352 | content: 5.507, mse: 0.008447, psnr: 20.91

step 9000 | training: 5.799, test: 6.206 | content: 5.346, mse: 0.008603, psnr: 20.9

step 10000 | training: 5.554, test: 6.242 | content: 5.409, mse: 0.00833, psnr: 21

step 11000 | training: 5.386, test: 6.258 | content: 5.402, mse: 0.008556, psnr: 20.87

step 12000 | training: 5.408, test: 5.991 | content: 5.126, mse: 0.008656, psnr: 20.79

step 13000 | training: 5.251, test: 6.01 | content: 5.136, mse: 0.008738, psnr: 20.76

step 14000 | training: 5.187, test: 5.798 | content: 5.022, mse: 0.007763, psnr: 21.34

step 15000 | training: 5.045, test: 6.254 | content: 5.305, mse: 0.009495, psnr: 20.47

step 16000 | training: 5.05, test: 5.855 | content: 5.061, mse: 0.007941, psnr: 21.15

step 17000 | training: 5.002, test: 5.974 | content: 5.133, mse: 0.008402, psnr: 20.93

step 18000 | training: 4.901, test: 6.271 | content: 5.263, mse: 0.01008, psnr: 20.29

step 19000 | training: 4.815, test: 5.693 | content: 4.92, mse: 0.007738, psnr: 21.26

step 20000 | training: 4.711, test: 5.711 | content: 4.899, mse: 0.008111, psnr: 21.14