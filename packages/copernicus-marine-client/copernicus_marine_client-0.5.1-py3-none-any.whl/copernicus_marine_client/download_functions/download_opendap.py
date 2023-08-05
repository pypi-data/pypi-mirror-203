from opendap_downloader.opendap_downloader import download_dataset

from copernicus_marine_client.catalogue_parser.request_structure import (
    SubsetRequest,
)


def download_opendap(
    login: str,
    password: str,
    subset_request: SubsetRequest,
):
    geographical_subset = (
        subset_request.minimal_latitude,
        subset_request.maximal_latitude,
        subset_request.minimal_longitude,
        subset_request.maximal_longitude,
    )
    temporal_subset = (
        subset_request.start_datetime,
        subset_request.end_datetime,
    )
    depth_range = (subset_request.minimal_depth, subset_request.maximal_depth)
    limit = False
    download_dataset(
        login,
        password,
        subset_request.dataset_url,
        subset_request.output_directory,
        subset_request.output_filename,
        subset_request.variables,
        geographical_subset,
        temporal_subset,
        depth_range,
        limit,
        subset_request.assume_yes,
    )
