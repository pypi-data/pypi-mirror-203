from datetime import datetime
from typing import List, Optional

import click

from copernicus_marine_client.catalogue_parser.catalogue_parser import (
    MOTU_KEY,
    OPENDAP_KEY,
    get_dataset_url_from_id,
    get_protocol_from_url,
    parse_catalogue,
)
from copernicus_marine_client.catalogue_parser.request_structure import (
    SubsetRequest,
    subset_request_from_file,
)
from copernicus_marine_client.download_functions.download_motu import (
    download_motu,
)
from copernicus_marine_client.download_functions.download_opendap import (
    download_opendap,
)

PROTOCOL_KEYS_ORDER = {"opendap": OPENDAP_KEY, "motu": MOTU_KEY}


@click.group()
def cli_group_subset() -> None:
    pass


@cli_group_subset.command(
    "subset",
    help="""Downloads subsets of datasets as NetCDF files.
    Either one of 'dataset-id' or 'dataset-url' is required
    (can be found via the 'copernicus-marine describe' command).

Example:

  copernicus-marine subset
--dataset-id METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2
--variable analysed_sst --variable sea_ice_fraction
--start-datetime 2021-01-01 --end-datetime 2021-01-02
--minimal-longitude 0.0 --maximal-longitude 0.1
--minimal-latitude 0.0 --maximal-latitude 0.1

  copernicus-marine subset -i METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2 -v analysed_sst
  -v sea_ice_fraction -t 2021-01-01 -T 2021-01-02 -x 0.0 -X 0.1 -y 0.0 -Y 0.1
""",
)
@click.option(
    "--dataset-url",
    "-u",
    type=str,
    help="The full dataset URL",
)
@click.option(
    "--dataset-id",
    "-i",
    type=str,
    help="The dataset id",
)
@click.option(
    "--login",
    prompt=True,
    hide_input=False,
)
@click.option(
    "--password",
    prompt=True,
    hide_input=True,
)
@click.option(
    "--variable",
    "-v",
    "variables",
    type=str,
    help="Specify dataset variables",
    multiple=True,
)
@click.option(
    "--minimal-longitude",
    "-x",
    type=click.FloatRange(min=-180, max=180),
    help="Minimal longitude for the subset",
)
@click.option(
    "--maximal-longitude",
    "-X",
    type=click.FloatRange(min=-180, max=180),
    help="Maximal longitude for the subset",
)
@click.option(
    "--minimal-latitude",
    "-y",
    type=click.FloatRange(min=-90, max=90),
    help="Minimal latitude for the subset",
)
@click.option(
    "--maximal-latitude",
    "-Y",
    type=click.FloatRange(min=-90, max=90),
    help="Maximal latitude for the subset",
)
@click.option(
    "--minimal-depth",
    "-z",
    type=click.FloatRange(min=0),
    help="Minimal depth for the subset",
)
@click.option(
    "--maximal-depth",
    "-Z",
    type=click.FloatRange(min=0),
    help="Maximal depth for the subset",
)
@click.option(
    "--start-datetime",
    "-t",
    type=click.DateTime(
        ["%Y", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"]
    ),
    help="The start datetime of the temporal subset",
)
@click.option(
    "--end-datetime",
    "-T",
    type=click.DateTime(
        ["%Y", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"]
    ),
    help="The end datetime of the temporal subset",
)
@click.option(
    "--output-directory",
    "-o",
    type=click.Path(),
    required=True,
    help="The destination folder for the downloaded files."
    + " Default is the current directory",
    default="",
)
@click.option(
    "--output-filename",
    "-f",
    type=click.Path(),
    help="Concatenate the downloaded data in the given file name"
    + " (under the output path)",
)
@click.option(
    "--assume-yes",
    is_flag=True,
    help="Flag to skip confirmation before download",
)
@click.option(
    "--force-protocol",
    type=click.Choice(list(PROTOCOL_KEYS_ORDER.keys())),
    help="Force download through one of the available protocols",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Flag to specify NOT to send the request to external server. "
    "Returns the request instead",
)
@click.option(
    "--request-file",
    type=click.Path(),
    help="Option to pass a filename corresponding to a file containg CLI arguments. "
    "The file MUST follow the structure of dataclass 'SubsetRequest'. "
    "ANY PARAMETER SPECIFIED ASIDE FROM FILE WILL NOT "
    "BE TAKEN INTO CONSIDERATION FOR THE REQUEST IF FILE "
    "IS SPECIFIED.",
)
def subset(
    dataset_url: str,
    dataset_id: str,
    login: str,
    password: str,
    variables: Optional[List[str]],
    minimal_longitude: Optional[float],
    maximal_longitude: Optional[float],
    minimal_latitude: Optional[float],
    maximal_latitude: Optional[float],
    minimal_depth: Optional[float],
    maximal_depth: Optional[float],
    start_datetime: Optional[datetime],
    end_datetime: Optional[datetime],
    output_filename: Optional[str],
    force_protocol: Optional[str],
    request_file: Optional[str],
    output_directory: str = "",
    assume_yes: bool = False,
    dry_run: bool = False,
):
    if request_file:
        subset_request = subset_request_from_file(request_file)
    else:
        subset_request = SubsetRequest(
            dataset_url=dataset_url,
            dataset_id=dataset_id,
            variables=variables,
            minimal_longitude=minimal_longitude,
            maximal_longitude=maximal_longitude,
            minimal_latitude=minimal_latitude,
            maximal_latitude=maximal_latitude,
            minimal_depth=minimal_depth,
            maximal_depth=maximal_depth,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            output_directory=output_directory,
            output_filename=output_filename,
            assume_yes=assume_yes,
            force_protocol=force_protocol,
            dry_run=dry_run,
        )
    subset_function(
        login,
        password,
        subset_request,
    )


def subset_function(
    login: str,
    password: str,
    subset_request: SubsetRequest,
):
    possible_protocols = (
        PROTOCOL_KEYS_ORDER.values()
        if not subset_request.force_protocol
        else [PROTOCOL_KEYS_ORDER[subset_request.force_protocol]]
    )
    if subset_request.force_protocol:
        click.echo(
            f"You forced selection of protocol: {subset_request.force_protocol}"
        )
    if not subset_request.dataset_url:
        if not subset_request.dataset_id:
            raise SyntaxError(
                "Must specify at least one of 'dataset_url' or 'dataset_id'"
            )
        catalogue = parse_catalogue()
        protocol_keys_iterator = iter(possible_protocols)
        while not subset_request.dataset_url:
            try:
                protocol = next(protocol_keys_iterator)
            except StopIteration:
                raise KeyError(
                    f"Dataset {subset_request.dataset_id} does "
                    "not have a valid protocol "
                    f"for subset function. Available protocols: {possible_protocols}"
                )
            subset_request.dataset_url = get_dataset_url_from_id(
                catalogue, subset_request.dataset_id, protocol
            )
    else:
        protocol = get_protocol_from_url(subset_request.dataset_url)
        catalogue = None
    if (
        subset_request.force_protocol
        and protocol != subset_request.force_protocol
    ):
        raise AttributeError("Dataset url does not match forced protocol!")
    elif protocol == OPENDAP_KEY:
        click.echo("download through OPeNDAP")
        if subset_request.dry_run:
            print(
                "download_opendap("
                + ", ".join(
                    [
                        f"{login}",
                        "HIDING_PASSWORD",
                        f"{subset_request}",
                    ]
                )
                + ")"
            )
            return
        download_opendap(
            login,
            password,
            subset_request,
        )
    elif protocol == MOTU_KEY:
        click.echo("download through MOTU")
        if subset_request.dry_run:
            print(
                "download_motu("
                + ", ".join(
                    [
                        f"{login}",
                        "HIDING_PASSWORD",
                        f"{subset_request}",
                        "NOT_PRINTING_CATALOGUE",
                    ]
                )
                + ")"
            )
            return
        download_motu(
            login,
            password,
            subset_request,
            catalogue=catalogue,
        )
    elif not protocol:
        raise KeyError(
            f"The requested dataset '{subset_request.dataset_id}' does not have "
            f"{possible_protocols} url available"
        )
    else:
        raise KeyError(f"Protocol {protocol} not handled by subset command")


if __name__ == "__main__":
    subset()
