Модуль `db_simple` предоставляет простой способ работы с файлами JSON.

Для работы с модулем нужно создать объект класса Database, указав имя файла без расширения .json, и вызвать метод open

edit_value(key, value) - изменяет значение элемента с указанным ключом

При использование модуля :
edit_members(key, new_members) - заменяет все элементы словаря с указанным ключом на новые элементы из словаря new_members

edit_name(key, new_key) - изменяет ключ элемента с указанным ключом на новый ключ new_key

Обратите внимание, что все методы edit_* должны вызываться только после вызова метода open, который открывает файл JSON для работы с ним.

После этого можно использовать методы класса Database для работы с данными в файле:

```python
database.set("key1", "value1") database.set("key2", "value2") value = database.get("key1") print(value) # Output: "value1" keys = database.keys() print(keys) # Output: ["key1", "key2"] database.delete("key2")