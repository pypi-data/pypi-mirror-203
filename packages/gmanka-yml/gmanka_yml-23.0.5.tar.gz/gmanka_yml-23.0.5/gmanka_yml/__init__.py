from io import TextIOWrapper
from pathlib import Path
from typing import Any
import yaml


version = '23.0.4'
_sential = object()


def to_str(
    data,
) -> str:
    try:
        return yaml.dump(
            data,
            allow_unicode = True,
            Dumper = yaml.CDumper,
        )
    except AttributeError:
        return yaml.dump(
            data,
            allow_unicode = True,
            Dumper = yaml.Dumper,
        )


def to_file(
    data,
    path: str | Path,
) -> None:
    Path(path).parent.mkdir(
        exist_ok = True,
        parents = True,
    )
    with open(
        file = path,
        mode = 'w',
        encoding = 'utf-8',
    ) as file:
        file.write(
            to_str(
                data,
            ),
        )


def from_str(
    data: str | TextIOWrapper,
    default = _sential,
    expected_type = None,
) -> Any:
    try:
        parsed = yaml.safe_load(
            stream = data,
        )
    except Exception as error:
        if default == _sential:
            raise error
        else:
            return default
    if expected_type == None:
        return parsed
    elif isinstance(
        parsed,
        expected_type,
    ):
        return parsed
    elif default == _sential:
        raise TypeError(
            f'{expected_type} expected, but got type(data)'
        )
    else:
        return default


def from_file(
    path: str | Path,
    default = _sential,
    expected_type = None,
) -> Any:
    try:
        with open(
            file = path,
            mode = 'r',
        ) as file:
            return from_str( 
                data = file, 
                default = default, 
                expected_type = expected_type, 
            )
    except Exception as error:
        if default == _sential:
            raise error
        else:
            return default

