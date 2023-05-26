import os
import timeit
import shutil
import psutil

def detect_usb_devices():
    usb_devices = []

    for partition in psutil.disk_partitions():
        if 'removable' in partition.opts or partition.fstype == 'exfat':
            usb_devices.append(partition.mountpoint)

    return usb_devices

def test_read_write_speed(file_size_bytes, test_file_path, num_iterations=10):
    def write_test():
        with open(test_file_path, 'wb') as test_file:
            test_file.write(os.urandom(file_size_bytes))

    def read_test():
        with open(test_file_path, 'rb') as test_file:
            _ = test_file.read()

    write_time = timeit.timeit(write_test, number=num_iterations) / num_iterations
    read_time = timeit.timeit(read_test, number=num_iterations) / num_iterations

    os.remove(test_file_path)

    return write_time, read_time

def display_speed_results(write_time, read_time, file_size_bytes, file_size_desc):
    write_speed = file_size_bytes / write_time / (1024 ** 2)
    read_speed = file_size_bytes / read_time / (1024 ** 2)

    print(f"Write speed for {file_size_desc}: {write_speed:.2f} MB/s")
    print(f"Read speed for {file_size_desc}: {read_speed:.2f} MB/s")

def main():
    usb_devices = detect_usb_devices()

    if not usb_devices:
        print("No USB devices detected.")
        return

    usb_mount_path = usb_devices[0]
    print(f"Testing USB device at: {usb_mount_path}")
    test_file_path = os.path.join(usb_mount_path, "speed_test_file")

    # 1 MB file
    file_size_bytes = 1 * 1024 ** 2
    write_time, read_time = test_read_write_speed(file_size_bytes, test_file_path)
    display_speed_results(write_time, read_time, file_size_bytes, "1 MB")

    # Calculate time for 1 GB file
    file_size_gb = 1024
    write_time_gb = write_time * file_size_gb
    read_time_gb = read_time * file_size_gb

    print(f"\nTime to write a 1 GB file: {write_time_gb:.2f} seconds")
    print(f"Time to read a 1 GB file: {read_time_gb:.2f} seconds")

if __name__ == "__main__":
    main()
