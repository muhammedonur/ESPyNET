import os
import shutil

def GetNumericalOrderedList(arr):
    return sorted(os.listdir(arr), key=lambda x: int(x.split("_")[0]))

def DeleteAllFilesInPath(source):
    i=0
    for filename in GetNumericalOrderedList(source):
        os.remove(source+filename)
        i=i+1
    print("All files[", i, "] in", source, "are removed.")

def SplitFilesInPath(source, destination, percent):
    print("SplitFilesInPath:", source, destination, percent)
    i=0
    for filename in GetNumericalOrderedList(source):
        if i%percent==0:
            os.rename(source+filename, destination+filename)
        i=i+1
    print("Files in source:", source, " are splitted to", destination, "with", percent, "% percent.")

def RenameAllFilesInPath(source, posix):
    print("RenameAllFilesInPath:", source, posix)
    i=0
    for filename in GetNumericalOrderedList(source):
        new_filename = str(i) + posix + "." + filename.split(".")[-1]
        if os.path.exists(source+new_filename):
            print("! File:", source+filename ,"already exists, it will be overwritten.")
        os.rename(source+filename, source+new_filename)
        i=i+1
    print("All files[", i, "] in", source, "are renamed numerically with", posix, "posix.")

def PrepareDataset(regenerate):
    gt_raw_path = "gt_RAW_npz/"
    gt_rgb_path = "gt_RGB/"
    moire_raw_path = "moire_RAW_npz/"
    moire_rgb_path = "moire_RGB/"

    datasets_root_folder = "../datasets/"
    original_dataset_folder = datasets_root_folder + "raw_moire_image_dataset_original/"
    dataset_folder = datasets_root_folder + "raw_moire_image_dataset/"

    train_folder_path = datasets_root_folder + dataset_folder + "trainset/"
    test_folder_path = datasets_root_folder + dataset_folder + "testset/"

    train_gt_raw_path = train_folder_path + gt_raw_path
    train_gt_rgb_path = train_folder_path + gt_rgb_path
    train_moire_raw_path = train_folder_path + moire_raw_path
    train_moire_rgb_path = train_folder_path + moire_rgb_path

    test_gt_raw_path = test_folder_path + gt_raw_path
    test_gt_rgb_path = test_folder_path + gt_rgb_path
    test_moire_raw_path = test_folder_path + moire_raw_path
    test_moire_rgb_path = test_folder_path + moire_rgb_path

    if regenerate:
        try:
            shutil.rmtree(dataset_folder)
        except OSError as e:
            print("There is no old dataset folder to remove before preparing new dataset folder.: %s : %s" % (dataset_folder, e.strerror))
        shutil.copytree(original_dataset_folder, dataset_folder)
    
    DeleteAllFilesInPath(test_gt_raw_path)
    DeleteAllFilesInPath(test_gt_rgb_path)
    DeleteAllFilesInPath(test_moire_raw_path)
    DeleteAllFilesInPath(test_moire_rgb_path)
    SplitFilesInPath(train_gt_raw_path, test_gt_raw_path, 10)
    SplitFilesInPath(train_gt_rgb_path, test_gt_rgb_path, 10)
    SplitFilesInPath(train_moire_raw_path, test_moire_raw_path, 10)
    SplitFilesInPath(train_moire_rgb_path, test_moire_rgb_path, 10)
    RenameAllFilesInPath(test_gt_raw_path, "_gt")
    RenameAllFilesInPath(test_gt_rgb_path, "_gt")
    RenameAllFilesInPath(test_moire_raw_path, "_m")
    RenameAllFilesInPath(test_moire_rgb_path, "_m")
    RenameAllFilesInPath(train_gt_raw_path, "_gt")
    RenameAllFilesInPath(train_gt_rgb_path, "_gt")
    RenameAllFilesInPath(train_moire_raw_path, "_m")
    RenameAllFilesInPath(train_moire_rgb_path, "_m")

PrepareDataset(False)