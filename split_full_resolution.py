import imageio.v2 as imageio
import sys, os

if __name__ == "__main__":

    full_resolution_file = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    output = sys.argv[4]

    print("Splitting file: " + full_resolution_file + " to width:", str(width), " and height:", str(height))

    if not os.path.isfile(full_resolution_file):
        print("The file doesn't exist!")
        sys.exit()

    image = imageio.imread(full_resolution_file)

    tiles = [image[x:x+width,y:y+height] for x in range(0,image.shape[0],width) for y in range(0,image.shape[1],height)]



    i = 0
    ext = full_resolution_file.split(".")[-1]
    for tile in tiles:
        if len(tile) == height and len(tile[0] == width):
            imageio.imwrite(output + "/" + str(i) + "." + ext, tile)
            i=i+1
        else:
            break

    print(str(i) + " images saved.")

