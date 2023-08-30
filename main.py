to_do_list = []

def add_task():
  task = input("Task : ")
  to_do_list.append(task)
  print(f"Tugas {task} berhasil ditambah")
  
def view_tasks():
  if len(to_do_list) == 0:
    print("Tidak ada task")
  else:
    print("Daftar Tugas : ")
    for index, task in enumerate(to_do_list, start = 1):
      print("{}.{}".format(index, task))
      
def delete_task():
  view_tasks()
  try:
    task_number = int(input("Enter the number of the task"))
    if 1 <= task_number <= len(to_do_list):
      to_do_list.pop(task_number-1)
      print("Task berhasil dihapus")
  except ValueError:
    print("Task Number Tidak Valid")
    
def mark_as_done():
    view_tasks()
    try:
      task_number = int(input("Enter the number of the task"))
      if 1 <= task_number <= len(to_do_list):
        to_do_list.pop(task_number-1)
        print("Task masrked as done")
    except ValueError:
      print("Task Number Tidak Valid")

while True:
  print("TODO LIST APP")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Delete Task")
  print("4. Mark Task as Done")
  print("5. Quit")

  pilihan = input("Masukkan Pilihan : ")

  if pilihan == "1" :
    add_task()
  elif pilihan == "2" :
    view_tasks()
  elif pilihan == "3":
    delete_task()
  elif pilihan == "4":
      mark_as_done()
  else:
    print("Pilihan tidak valid")