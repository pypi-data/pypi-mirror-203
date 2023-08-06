from io import TextIOWrapper
from pathlib import Path
import yaml


version = '23.0.1'
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
            )
        )


def read_str(
    data: str | TextIOWrapper,
    default = _sential,
    expected_type = None,
):
    try:
        loaded = yaml.load(
            data,
            Loader = yaml.CLoader,
        )
    except AttributeError:
        return yaml.load(
            data,
            Loader = yaml.Loader,
        )
    except Exception as error:
        if default == _sential:
            raise error
        else:
            return default
    if expected_type == None:
        return data
    elif isinstance(
        data,
        expected_type,
    ):
        return data
    elif default == _sential:
        raise TypeError(
            f'{expected_type} expected, but got type(data)'
        )
    else:
        return default


def read_file(
    path: str | Path,
    default = _sential,
    expected_type = None,
):
    try:
        with open(
            file = path,
            mode = 'r',
            encoding = 'utf-8',
        ) as file:
            return read_str(
                file,
                default = default,
                expected_type = expected_type,
            )
    except Exception as error:
        if default == _sential:
            raise error
        else:
            return default

