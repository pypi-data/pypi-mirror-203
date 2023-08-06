# gmanka yml

some useful shortcuts for pyyaml

## installation

```bash
pip install gmanka_yml
```

## navigation

- [to_str](#to_str)  
- [to_file](#to_file)  
- [from_str](#read_str)  
- [from_file](#read_file)  
- [default](#default)
- [expected_type](#expected_type)
- [changelog](changelog)

## to_str[^](#functions)

converts any data to yml string and returns it

```py
import gmanka_yml as yml

my_dict = {
    'element_1': 1,
    2: 'element_2',
    3: [
        'list_element_1',
        'list_element_2',
    ]
}

print(yml.to_str(my_dict))
```

output:

```yaml
element_1: 1
2: element_2
3:
- list_element_1
- list_element_2
```

## to_file[^](#functions)

same as [to_str](#to_str), but writes data to file instead of returning

```py
yml.to_file(
    data = my_dict,
    path = 'file.yml',
)
```

## from_str[^](#functions)

```py
import gmanka_yml as yml

my_str = '''
element_1: 1
2: element_2
3:
- list_element_1
- list_element_2
'''

my_dict = yml.from_str(my_str)

print(my_dict)

print(type(my_dict))
```

output:

```py
{'element_1': 1, 2: 'element_2', 3: ['list_element_1', 'list_element_2']}

<class 'dict'>
```

## from_file[^](#functions)

same as [from_str](#read_str), but reads data from file

```py
yml.from_file('file.yml')
```

## default

```py
yml.from_str(1) # raises TypeError

yml.from_str(1, default = None) # returns None
```

## expected type

```py
yml.from_str(
    data = '{}',
    expected_type = list,
) # raises TypeError

yml.from_str(
    data = '{}',
    default = None,
    expected_type = list,
) # returns None
```

