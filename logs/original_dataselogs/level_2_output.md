2023-05-06 19:29:16.671109: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-05-06 19:29:19.131372: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
WARNING:tensorflow:From /usr/local/lib/python3.9/dist-packages/tensorflow/python/compat/v2_compat.py:107: disable_resource_variables (from tensorflow.python.ops.variable_scope) is deprecated and will be removed in a future version.
Instructions for updating:
non-resource variables are not supported in the long term
The following parameters will be applied for CNN training:
Training level: 2
Batch size: 18
Learning rate: 5e-05
Training iterations: 20000
Evaluation step: 1000
Restore Iteration: 20000
Path to the dataset: raw_images/
Path to VGG-19 network: vgg_pretrained/imagenet-vgg-verydeep-19.mat
2023-05-06 19:29:23.189986: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 19:29:23.771269: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 19:29:23.771654: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 19:29:23.772790: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 19:29:23.773045: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 19:29:23.773237: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 19:29:26.565703: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 19:29:26.566030: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 19:29:26.566206: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:996] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
2023-05-06 19:29:26.566330: W tensorflow/core/common_runtime/gpu/gpu_bfc_allocator.cc:47] Overriding orig_value setting because the TF_FORCE_GPU_ALLOW_GROWTH environment variable is set. Original config value was 0.
2023-05-06 19:29:26.566367: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1635] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 14518 MB memory:  -> device: 0, name: Tesla V100-SXM2-16GB, pci bus id: 0000:00:04.0, compute capability: 7.0
Initializing variables
2023-05-06 19:29:42.340984: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:353] MLIR V1 optimization pass is not enabled
Restoring Variables
Loading test data...
Test data was loaded

Loading training data...
Training data was loaded

Training network
2023-05-06 19:31:56.021635: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 115605504 exceeds 10% of free system memory.
2023-05-06 19:31:56.021772: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 115605504 exceeds 10% of free system memory.
2023-05-06 19:31:56.042716: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 115605504 exceeds 10% of free system memory.
2023-05-06 19:31:56.205344: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 57802752 exceeds 10% of free system memory.
2023-05-06 19:31:56.205442: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 57802752 exceeds 10% of free system memory.
2023-05-06 19:32:02.166512: I tensorflow/compiler/xla/stream_executor/cuda/cuda_dnn.cc:424] Loaded cuDNN version 8700
2023-05-06 19:32:09.716201: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 7.93GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 19:32:10.181350: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 2.62GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 19:32:10.191550: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 2.62GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 19:32:10.202579: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 1.95GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 19:32:10.242245: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 2.62GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 19:32:10.246311: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 2.62GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 19:32:10.430951: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 5.40GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 19:32:10.598673: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 1.15GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 19:32:10.598790: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 1.15GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
2023-05-06 19:32:10.600668: W tensorflow/tsl/framework/bfc_allocator.cc:296] Allocator (GPU_0_bfc) ran out of memory trying to allocate 621.25MiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
step 0 | training: 0.05073, test: 62.11 | content: 52.48, mse: 0.09629, psnr: 10.22

step 1000 | training: 12.31, test: 7.959 | content: 6.286, mse: 0.01673, psnr: 17.93

step 2000 | training: 6.606, test: 7.164 | content: 5.729, mse: 0.01435, psnr: 18.79

step 3000 | training: 6.012, test: 6.476 | content: 5.27, mse: 0.01206, psnr: 19.46

step 4000 | training: 5.787, test: 6.337 | content: 5.218, mse: 0.01118, psnr: 19.86

step 5000 | training: 5.638, test: 5.976 | content: 4.91, mse: 0.01067, psnr: 19.94

step 6000 | training: 5.3, test: 5.68 | content: 4.693, mse: 0.009869, psnr: 20.29

step 7000 | training: 5.319, test: 5.764 | content: 4.783, mse: 0.009811, psnr: 20.39

step 8000 | training: 5.249, test: 5.831 | content: 4.765, mse: 0.01066, psnr: 20.15

step 9000 | training: 4.999, test: 5.503 | content: 4.563, mse: 0.009397, psnr: 20.54

step 10000 | training: 4.943, test: 5.49 | content: 4.499, mse: 0.009915, psnr: 20.34

step 11000 | training: 4.913, test: 5.336 | content: 4.418, mse: 0.009184, psnr: 20.68

step 12000 | training: 4.841, test: 5.453 | content: 4.466, mse: 0.009873, psnr: 20.35

step 13000 | training: 4.765, test: 5.517 | content: 4.586, mse: 0.009305, psnr: 20.59

step 14000 | training: 4.804, test: 5.512 | content: 4.444, mse: 0.01068, psnr: 20.14

step 15000 | training: 4.722, test: 5.192 | content: 4.279, mse: 0.009132, psnr: 20.78

step 16000 | training: 4.646, test: 5.098 | content: 4.226, mse: 0.008721, psnr: 20.91

step 17000 | training: 4.572, test: 5.298 | content: 4.378, mse: 0.009198, psnr: 20.74

step 18000 | training: 4.568, test: 5.145 | content: 4.278, mse: 0.008672, psnr: 20.89

step 19000 | training: 4.54, test: 5.452 | content: 4.471, mse: 0.009807, psnr: 20.48

step 20000 | training: 4.548, test: 5.214 | content: 4.238, mse: 0.009764, psnr: 20.49