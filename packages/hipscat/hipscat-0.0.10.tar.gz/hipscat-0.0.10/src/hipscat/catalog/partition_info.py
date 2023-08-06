"""Container class to hold per-partition metadata"""

from typing import List

from hipscat.io import file_io, paths
from hipscat.pixel_math import HealpixPixel


class PartitionInfo:
    """Container class for per-partition info."""

    METADATA_ORDER_COLUMN_NAME = "Norder"
    METADATA_DIR_COLUMN_NAME = "Dir"
    METADATA_PIXEL_COLUMN_NAME = "Npix"

    def __init__(self, catalog_base_dir: file_io.FilePointer) -> None:
        self.catalog_base_dir = catalog_base_dir

        partition_info_pointer = paths.get_partition_info_pointer(self.catalog_base_dir)
        if not file_io.does_file_or_directory_exist(partition_info_pointer):
            raise FileNotFoundError(
                f"No partition info found where expected: {str(partition_info_pointer)}"
            )

        self.data_frame = file_io.load_csv_to_pandas(partition_info_pointer)

    def get_healpix_pixels(self) -> List[HealpixPixel]:
        """Get healpix pixel objects for all pixels represented as partitions.

        Returns:
            List of HealpixPixel
        """
        return [
            HealpixPixel(order, pixel)
            for order, pixel in zip(
                self.data_frame[self.METADATA_ORDER_COLUMN_NAME],
                self.data_frame[self.METADATA_PIXEL_COLUMN_NAME],
            )
        ]

    def get_file_names(self):
        """Get file handles for all partition files in the catalog

        Returns:
            one-dimensional array of strings, where each string is a partition file
        """
        file_names = []
        for _, partition in self.data_frame.iterrows():
            file_names.append(
                paths.pixel_catalog_file(
                    self.catalog_base_dir,
                    partition[self.METADATA_ORDER_COLUMN_NAME],
                    partition[self.METADATA_PIXEL_COLUMN_NAME],
                )
            )

        return file_names
