# Convert from dng to pny and test it with implemented model.
python dng_to_png.py 20230512_131836.dng ../datasets/zurich-raw-to-rgb/raw_images/test/huawei_full_resolution; python test_model.py original=true

# Only convert dng to png and locate it in test folder
python dng_to_png.py 20230512_131836.dng ../datasets/zurich-raw-to-rgb/raw_images/test/huawei_full_resolution;

# Only test image
python test_model.py original=true 

# Split Image
python split_full_resolution.py ../datasets/zurich-raw-to-rgb/raw_images/test/huawei_raw_full_resolution/20230512_131836.png 448 448 ../datasets/zurich-raw-to-rgb/raw_images/test/huawei_raw