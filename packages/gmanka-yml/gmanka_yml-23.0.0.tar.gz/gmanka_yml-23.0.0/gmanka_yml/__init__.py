from io import TextIOWrapper
from pathlib import Path
import yaml


version = '23.0.0'


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
        path,
        'w'
    ) as file:
        file.write(
            to_str(
                data,
            )
        )


def read_str(
    data: str | TextIOWrapper,
):
    try:
        return yaml.load(
            data,
            Loader = yaml.CLoader,
        )
    except AttributeError:
        return yaml.load(
            data,
            Loader = yaml.Loader,
        )


def read_file(
    path: str | Path
):
    with open(
        path,
        'r',
    ) as file:
        return read_str(
            file
        )

