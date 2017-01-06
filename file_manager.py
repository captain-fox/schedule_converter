import glob, os
os.chdir(".")

def search_for_file():
    n = 0
    for file in glob.glob("*.csv"):

        n = n + 1

        if n > 1:
            print("More than one .csv file found")
            for filelist in glob.glob("*.csv"):
                print(filelist)
        elif n < 1:
            print("No .csv files found in directory")
            for filelist in glob.glob("*.csv"):
                print(filelist)

    print("File found: " + file + "\n")
    return file