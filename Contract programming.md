# Контрактное программирование

**Контракты** - это правила валидации входных и выходных параметров функций.

Для работы с контрактами в Python используем библиотеку PyContracts.

Контракты нужны, для того чтобы:

- сделать динамически типизированный код стабильнее и защищеннее; 

- чтобы писать больше тестов для бизнес-логики и не заморачиваться с проверкой корректности структур данных.

**Контракты** дают уверенность в корректности типов аргументов и возвращаемых значений.

PyContracts поддерживает синтаксис Python 3 type hinting.

Контракты проверяются только в тестовом окружении и не замедляют продуктив.



### **Специфика контрактов**

Контракты могут быть реализованы тремя способами:

1. Использование ``@contract`` декоратор:

   ```python
   @contract(a='int,>0', b='list[N],N>0', returns='list[N]')
   def my_function(a, b):
       ...
   ```

2. Использование аннотаций (for Python 3):

   ```python
   @contract
   def my_function(a : 'int,>0', b : 'list[N],N>0') -> 'list[N]':
        # Requires b to be a nonempty list, and the return
        # value to have the same length.
        ...
   ```

3. Использование строк документации, вместе с `:type:` и `:rtype:` tags:

   ```python
   @contract
   def my_function(a, b):
       """ Function description.
           :type a: int,>0
           :type b: list[N],N>0
           :rtype: list[N]
       """
   ```

## Пример функций

```python
from contracts import contract

# Сумма а и b
@contract
def ExampleSum(a, b):
    """
    :param a: int|float > 0 # тип может быть либо int либо float
    :param b: int|float > 0
    :return: int|float
    """
    return a + b

# Деление a на b
@contract
def ExampleDiv(a, b):
    """
    :param a: int|float != 0
    :param b: int|float != 0
    :return: int|float
    """
    if a != 0 & b != 0:
    	return a / b
    else: return 37007
```



### Схема программы
```
Начало
   ввод(x, y);

если p(x, y) то на L1;
   z := g(x , y);
   на L2;

L1:  z := h(x,y);
   на L2;

L2: вывод(z);

Конец
```
