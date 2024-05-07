import time

def check_jobs(filename='jobs.txt'):
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            status, description = line.strip().split(',', 1)
            if status == 'pending':
                file.write(f'in_progress,{description}\n')
                print(f"Rozpoczęto pracę: {description}")
                time.sleep(30)  
                file.write(f'done,{description}\n')
                print(f"Zakończono pracę: {description}")
            else:
                file.write(line)

if __name__ == "__main__":
    while True:
        check_jobs()
        time.sleep(5)
