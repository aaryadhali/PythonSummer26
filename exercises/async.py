#We define this as a coroutine using 'async def'
import asyncio
import time


async def download_file(file_name):
    print(f"Starting download: {file_name}")
    #asyncio.sleeep is non-blocking. It yields control back to the loop
    await asyncio.sleep(1)
    print(f"finished download: {file_name}")

async def main():
    start_time = time.time()

    #we always schedule all three tasks to run at the same time 
    await asyncio.gather(
        download_file("Photo_1"),
        download_file("Photo_2"),
        download_file("Photo_3")
    )

    duration = time.time()-start_time
    print(f"total time taken: {duration:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())