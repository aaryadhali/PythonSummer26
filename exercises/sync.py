import time

def download_file(file_name):
    print(f"starting download: {file_name}")
    #time.sleep stops the entire program for 1 second
    time.sleep(1)
    print(f"Finished download{file_name}")

def main():
    start_time = time.time()
    download_file("Photo_1")
    download_file("Photo_2")
    download_file("Photo_3")

    duration = time.time() - start_time
    print(f"Total time taken is {duration:2f} seconds")

if __name__ == "__main__":
    main()