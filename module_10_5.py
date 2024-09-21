import multiprocessing
from datetime import datetime

def read_info(file_path):
    with open(file_path) as f:
        while True:
            l = f.readline()
            if l == '':
                break

if __name__ == '__main__':

    start = datetime.now()
    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]
    with multiprocessing.Pool(processes=5) as pool:
        pool.map(read_info,filenames )

  #  for i in filenames:
  #      read_info(i)


    end = datetime.now()
    print(end-start)
