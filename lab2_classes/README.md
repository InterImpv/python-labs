## animal

**Вихідне завдання:**

Детально розглянути приклад коду з останньої лекції (animal.py)

(екстра): Спробувати внести в лекційний приклад запропоновані зміни, розширивши його та додавши додаткові атрибути та методи:

```
TODO: fill classes below with the required logic
   to represent human and person (probably with tax number, ...)
TODO: try to make an Enterprise able to own Pets
TODO: - add class to represent vaccine
      - add class to represent generic chip,
       and separate subclasses for concrete animal ID chips
      - anything other you want to extend here
```

**Результат:**

Додано класи **Vaccine** (репрезентує вакцину), **Enterprise** (репрезентує компанію, яка може бути власником домашньої тварини), абстрактний клас **Chip** (репрезентує чіп певного розміру) та два нащадки **RFIDChip** та **GPSChip** (репрезентують вже реальні приклади чіпу для тварин). Також доповнено клас **Animal** (вік) та його нащадків **Human** (ім'я) і **Person** (податковий номер).

## basicclasses

**Вихідне завдання:**

Написати свою ієрархію класів, яка моделює об'єкти нашого світу, наприклад:
 - Особа, Робітник, Компанія з декількома Робітниками;

  або

 - Тварина, Домашня тварина, Особа, Власник і т.д;

або будь-які інші об'єкти на ваш розсуд. Потрібно використовувати наслідування об'єктів, `super()`, а також спеціальний метод `__repr__`.

**Результат:**

Маємо скрипт, що містить три основні класи **Vehicle**, **Propulsion**, **MovementSystem** та по парі субкласів **Wheels**, **Tracks**, **CombustionEngine**, **TurbineEngine**, що наслідуються від **MovementSystem** та **Propulsion** відповідно. Клас **Vehicle** створюється за екземплярами класів **Propulsion** та **MovementSystem** або їх нащадками.

## coolfunction

**Вихідне завдання:**

Спробуйте з наведеної нижче функції зробити функцію, що може приймати або `iterable`, або будь-яку кількість позиційних аргументів через ",":

```
def avg(iterable):
    return sum(iterable) / len(iterable)
```

Виконано з використанням конструкції `*args`, що дозволяє задавати функції змінну кількість вхідних аргументів.