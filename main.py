# 1. menambahkan aktivitas
# 2. ngeliat semua aktivitas yang udah ditambahkan
# 3. menghapus aktivitas
# 4. tandain aktivitas kalo udah selesai

# Clean code
# 1. supaya orang baca nya mudah (readibility)
# 2. biar ketauan error nya dimana (maintaiable)
# 3. supaya kalo kita baca ulang itu ga bingung (readble & maintainable)

to_do_list = []

def add_task():
  task = input("Task : ")
  to_do_list.append(task)
  print(f"Tugas {task} berhasil ditambah")
  
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