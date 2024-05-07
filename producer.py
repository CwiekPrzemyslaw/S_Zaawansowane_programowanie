import time

def add_job(job_description, filename='jobs.txt'):
    with open(filename, 'a') as file:
        file.write(f'pending,{job_description}\n')

def process_job(job, filename='jobs.txt'):
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            status, description = line.strip().split(',', 1)
            if description == job:
                file.write(f'in_progress,{description}\n')
                print(f"Rozpoczęto pracę: {description}")
                time.sleep(30)  
                file.write(f'done,{description}\n')
                print(f"Zakończono pracę: {description}")
            else:
                file.write(line)

if __name__ == "__main__":
    while True:
        job_description = input("Podaj opis pracy do wykonania (lub wpisz 'exit' aby zakończyć): ")
        if job_description.lower() == 'exit':
            break
        add_job(job_description)
        print("Praca dodana do kolejki.")
        
        time.sleep(5)
