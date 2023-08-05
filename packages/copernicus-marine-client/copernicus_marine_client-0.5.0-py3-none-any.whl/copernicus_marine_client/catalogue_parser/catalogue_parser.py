from copy import deepcopy
from dataclasses import dataclass
from datetime import timedelta
from itertools import groupby
from json import loads
from multiprocessing import Pool
from typing import Any, Callable, Iterable, Optional, Tuple, TypeVar

import requests
from cachier import cachier


@dataclass
class CopernicusMarineDatasetService:
    protocol: str
    uri: str


@dataclass
class CopernicusMarineDatasetCoordinates:
    coordinates_id: str
    units: str
    minimum_value: float
    maximum_value: float
    step: Optional[float]
    values: Optional[str]


@dataclass
class CopernicusMarineDatasetVariable:
    short_name: str
    standard_name: str
    units: str
    bbox: Tuple[float, float, float, float]
    coordinates: list[CopernicusMarineDatasetCoordinates]


@dataclass
class CopernicusMarineProductDataset:
    dataset_id: str
    dataset_name: str
    services: list[CopernicusMarineDatasetService]
    variables: list[CopernicusMarineDatasetVariable]


@dataclass
class CopernicusMarineProductProvider:
    name: str
    roles: list[str]
    url: str
    email: str


@dataclass
class CopernicusMarineProduct:
    title: str
    product_id: str
    thumbnail_url: str
    description: str
    production_center: str
    creation_datetime: str
    modified_datetime: Optional[str]
    keywords: dict[str, str]
    datasets: list[CopernicusMarineProductDataset]


@dataclass
class CopernicusMarineCatalogue:
    products: list[CopernicusMarineProduct]


OPENDAP_KEY = "opendap"
MOTU_KEY = "motu"
FTP_KEY = "ftp"

_S = TypeVar("_S")
_T = TypeVar("_T")


def map_parallel(
    function: Callable[[_S], _T], iterable: Iterable[_S]
) -> list[_T]:
    parallel_processes = 20
    with Pool(parallel_processes) as pool:
        return pool.map(function, iterable)


def map_reject_none(
    function: Callable[[_S], Optional[_T]], iterable: Iterable[_S]
) -> Iterable[_T]:
    return (element for element in map(function, iterable) if element)


@cachier(stale_after=timedelta(hours=3))
def _fetch_raw_products() -> list[dict[str, Any]]:
    response = requests.post(
        "https://cmems-be.lobelia.earth/api/datasets",
        json={"size": 1000, "includeOmis": True},
    )
    assert response.ok, response.text
    raw_catalogue: dict[str, Any] = loads(response.text)
    return map_parallel(
        _fetch_raw_product,
        raw_catalogue["datasets"].keys(),
    )


def _fetch_raw_product(product_id: str) -> dict[str, Any]:
    response = requests.get(product_url(product_id))
    assert response.ok, response.text
    return loads(response.text)


def product_url(product_id: str) -> str:
    return (
        f"https://cmems-be.lobelia.earth/api/dataset/{product_id}"
        + "?variant=detailed-v2"
    )


def variable_title_to_standard_name(variable_title: str) -> str:
    return variable_title.lower().replace(" ", "_")


def variable_to_pick(layer: dict[str, Any]) -> bool:
    return (
        layer["variableId"] != "__DEFAULT__"
        and layer["subsetVariableIds"]
        and len(layer["subsetVariableIds"]) == 1
    )


def to_datasets(
    raw_services: dict[str, dict[str, str]], layers: dict[str, dict[str, Any]]
) -> list[CopernicusMarineProductDataset]:
    def to_service(
        protocol_uri: Tuple[str, str]
    ) -> CopernicusMarineDatasetService:
        return CopernicusMarineDatasetService(
            protocol=protocol_uri[0], uri=protocol_uri[1]
        )

    def to_variable(layer: dict[str, Any]) -> CopernicusMarineDatasetVariable:
        def to_coordinates(
            subset_attributes: Tuple[str, dict[str, Any]]
        ) -> CopernicusMarineDatasetCoordinates:
            coordinate_name = subset_attributes[0]
            values: Optional[str]
            if coordinate_name == "depth":
                values = layer.get("zValues")
            elif coordinate_name == "time":
                values = layer.get("tValues")
            else:
                values = None
            return CopernicusMarineDatasetCoordinates(
                coordinates_id=subset_attributes[0],
                units=subset_attributes[1]["units"],
                minimum_value=subset_attributes[1]["min"],
                maximum_value=subset_attributes[1]["max"],
                step=subset_attributes[1].get("step"),
                values=values,
            )

        return CopernicusMarineDatasetVariable(
            short_name=layer["variableId"],
            standard_name=variable_title_to_standard_name(
                layer["variableTitle"]
            ),
            units=layer["units"],
            bbox=layer["bbox"],
            coordinates=list(
                map(to_coordinates, layer["subsetAttrs"].items())
            ),
        )

    def to_dataset(
        dataset_group: Tuple[str, Iterable[dict[str, Any]]],
    ) -> CopernicusMarineProductDataset:
        dataset_id = dataset_group[0]
        layer_elements = list(dataset_group[1])
        return CopernicusMarineProductDataset(
            dataset_id=dataset_id,
            dataset_name=layer_elements[0]["subdatasetTitle"],
            services=list(map(to_service, raw_services[dataset_id].items())),
            variables=list(
                map(to_variable, filter(variable_to_pick, layer_elements))
            ),
        )

    groups = groupby(layers.values(), key=lambda layer: layer["subdatasetId"])
    return sorted(
        map(to_dataset, groups), key=lambda dataset: dataset.dataset_id
    )


def _parse_product(raw_product: dict[str, Any]) -> CopernicusMarineProduct:
    return CopernicusMarineProduct(
        title=raw_product["title"],
        product_id=raw_product["id"],
        thumbnail_url=raw_product["thumbnailUrl"],
        description=raw_product["abstract"],
        production_center=raw_product["originatingCenter"],
        creation_datetime=raw_product["creationDate"],
        modified_datetime=raw_product.get("modifiedDate"),
        keywords=raw_product["keywords"],
        datasets=to_datasets(raw_product["services"], raw_product["layers"]),
    )


def parse_catalogue(
    overwrite_cache: bool = False,
) -> CopernicusMarineCatalogue:
    raw_products: list[dict[str, Any]] = _fetch_raw_products(
        overwrite_cache=overwrite_cache
    )

    return CopernicusMarineCatalogue(
        products=sorted(
            map(_parse_product, raw_products),
            key=lambda product: product.product_id,
        ),
    )


def get_dataset_from_id(
    catalogue: CopernicusMarineCatalogue, dataset_id: str
) -> CopernicusMarineProductDataset:
    for product in catalogue.products:
        for dataset in product.datasets:
            if dataset_id == dataset.dataset_id:
                return dataset
    raise KeyError(
        f"The requested dataset '{dataset_id}' was not found in the catalogue,"
        " you can use 'copernicus-marine describe --include-datasets "
        "-c <search_token>' to find the dataset id"
    )


def get_product_from_url(
    catalogue: CopernicusMarineCatalogue, dataset_url: str
) -> CopernicusMarineProduct:
    """
    Return the product object, with its dataset list filtered
    """
    filtered_catalogue = filter_catalogue_with_strings(
        catalogue, [dataset_url]
    )
    if filtered_catalogue is None:
        raise TypeError("filtered catalogue is empty")
    return filtered_catalogue.products[0]


def get_protocol_from_url(dataset_url) -> str:
    if dataset_url.startswith("ftp://"):
        protocol = FTP_KEY
    elif "/motu-web/Motu" in dataset_url:
        protocol = MOTU_KEY
    elif "/wms/" in dataset_url:
        protocol = "OGC:WMS:getCapabilities"
    elif "/thredds/dodsC/" in dataset_url:
        protocol = OPENDAP_KEY
    else:
        raise ValueError(f"No protocol matching url: {dataset_url}")
    return protocol


def get_protocol_url_from_id(
    dataset_id: str, protocol_key_order: list[str]
) -> Tuple[str, str]:
    catalogue = parse_catalogue()
    dataset_urls = (
        get_dataset_url_from_id(catalogue, dataset_id, protocol)
        for protocol in protocol_key_order
    )
    try:
        dataset_url = next(filter(lambda dataset: dataset, dataset_urls))
        protocol = get_protocol_from_url(dataset_url)
    except StopIteration as exception:
        raise KeyError(
            f"Dataset {dataset_id} does not have a valid protocol "
            f"for subset function. Available protocols: {protocol_key_order}"
        ) from exception
    return protocol, dataset_url


def get_service_url(
    dataset: CopernicusMarineProductDataset, protocol: str
) -> str:
    service_urls = iter(
        [
            service.uri
            for service in dataset.services
            if service.protocol == protocol
        ]
    )
    return next(service_urls, "")


def get_dataset_url_from_id(
    catalogue: CopernicusMarineCatalogue, dataset_id: str, protocol: str
) -> str:
    dataset = get_dataset_from_id(catalogue, dataset_id)
    return get_service_url(dataset, protocol)


def filter_catalogue_with_strings(
    catalogue: CopernicusMarineCatalogue, tokens: list[str]
) -> Optional[CopernicusMarineCatalogue]:
    filtered_catalogue = deepcopy(catalogue)
    return find_match_object(filtered_catalogue, tokens)


def find_match_object(value: Any, tokens: list[str]) -> Any:
    match: Any
    if isinstance(value, str):
        match = find_match_string(value, tokens)
    elif isinstance(value, list):
        match = find_match_list(value, tokens)
    elif hasattr(value, "__dict__"):
        match = find_match_dict(value, tokens)
    else:
        match = None
    return match


def find_match_string(string: str, tokens: list[str]) -> Optional[str]:
    return string if any(token in string for token in tokens) else None


def find_match_list(object_list: list[Any], tokens) -> Optional[list[Any]]:
    def find_match(element: Any) -> Optional[Any]:
        return find_match_object(element, tokens)

    filtered_list: list[Any] = list(map_reject_none(find_match, object_list))
    return filtered_list if filtered_list else None


def find_match_dict(
    structure: dict[str, Any], tokens
) -> Optional[dict[str, Any]]:
    filtered_dict = {
        key: find_match_object(value, tokens)
        for key, value in structure.__dict__.items()
        if find_match_object(value, tokens)
    }

    found_match = any(filtered_dict.values())
    if found_match:
        new_dict = dict(structure.__dict__, **filtered_dict)
        structure.__dict__ = new_dict
    return structure if found_match else None
