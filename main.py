import random

def guess_the_number():
  min_number = 1
  max_number = 100
  attempts = 7
  secret_number = random.randint(min_number, max_number)

  print(f"Вітаємо у грі 'Вгадай число'! Вам потрібно вгадати число від {min_number} до {max_number}. У вас {attempts} спроб.")

  for attempt in range(1, attempts + 1):
      try:
          guess = int(input(f"Спроба {attempt}. Введіть ваш варіант: "))
      except ValueError:
          print("Будь ласка, введіть ціле число.")
          continue
      
      if guess < secret_number:
          print("Занадто маленьке.")
      elif guess > secret_number:
          print("Занадто велике.")
      else:
          print(f"Вітаємо! Ви вгадали число {secret_number} за {attempt} спробу(и)!")
          return
  
  print(f"Ви використали всі {attempts} спроб. Загадане число було {secret_number}. Спробуйте ще!")

if __name__ == "__main__":
  guess_the_number()
