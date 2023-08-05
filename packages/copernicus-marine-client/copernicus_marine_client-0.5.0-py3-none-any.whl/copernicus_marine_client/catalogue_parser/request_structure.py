from dataclasses import dataclass
from datetime import datetime
from json import load
from typing import Dict, List, Optional


@dataclass
class SubsetRequest:
    dataset_url: str = ""
    dataset_id: str = ""
    output_directory: str = ""
    assume_yes: bool = False
    dry_run: bool = False
    variables: Optional[List[str]] = None
    minimal_longitude: Optional[float] = None
    maximal_longitude: Optional[float] = None
    minimal_latitude: Optional[float] = None
    maximal_latitude: Optional[float] = None
    minimal_depth: Optional[float] = None
    maximal_depth: Optional[float] = None
    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None
    output_filename: Optional[str] = None
    force_protocol: Optional[str] = None

    def get_subset_request_dict(self) -> Dict:
        return self.__dict__

    def enforce_types(self):
        def datetime_parser(string: str):
            for fmt in [
                "%Y",
                "%Y-%m-%d",
                "%Y-%m-%dT%H:%M:%S",
                "%Y-%m-%d %H:%M:%S",
            ]:
                try:
                    return datetime.strptime(string, fmt)
                except ValueError:
                    pass
            raise ValueError(f"no valid date format found for: {string}")

        type_enforced_dict = {}
        for key, value in self.__dict__.items():
            if key in [
                "minimal_longitude",
                "maximal_longitude",
                "minimal_latitude",
                "maximal_latitude",
                "minimal_depth",
                "maximal_depth",
            ]:
                new_value = float(value) if value is not None else None
            elif key in [
                "start_datetime",
                "end_datetime",
            ]:
                new_value = datetime_parser(value) if value else None
            elif key in ["assume_yes", "dry_run"]:
                new_value = bool(value) if value is not None else None
            elif key in ["variables"]:
                new_value = list(value) if value is not None else None
            else:
                new_value = str(value) if value else None
            type_enforced_dict[key] = new_value
        self.__dict__.update(type_enforced_dict)


def subset_request_from_file(filepath) -> SubsetRequest:
    json_file = open(filepath)
    subset_request = SubsetRequest()
    subset_request.__dict__.update(load(json_file))
    subset_request.enforce_types()
    return subset_request


@dataclass
class NativeRequest:
    dataset_url: str = ""
    dataset_id: str = ""
    no_directories: bool = False
    show_outputnames: bool = False
    output_directory: str = "."
    assume_yes: bool = False
    dry_run: bool = False

    def get_native_request_dict(self) -> Dict:
        return self.__dict__

    def enforce_types(self):
        type_enforced_dict = {}
        for key, value in self.__dict__.items():
            if key in [
                "no_directories",
                "show_outputnames",
                "assume_yes",
                "dry_run",
            ]:
                new_value = bool(value) if value is not None else None
            else:
                new_value = str(value) if value else None
            type_enforced_dict[key] = new_value
        self.__dict__.update(type_enforced_dict)


def native_request_from_file(filepath) -> NativeRequest:
    json_file = open(filepath)
    native_request = NativeRequest()
    native_request.__dict__.update(load(json_file))
    native_request.enforce_types()
    return native_request


if __name__ == "__main__":
    sr = subset_request_from_file(
        "tests/resources/example_subset_request.json"
    )
    print(sr)
    nr = native_request_from_file(
        "tests/resources/example_native_request.json"
    )
    print(nr)
