from azure.storage.blob import BlobClient, ContainerClient
import pandas as pd


class BlobIO:
    def __init__(self, storage_url: str, container_name: str, access_key: str) -> None:
        self._storage_url = storage_url
        self._container_name = container_name
        self._access_key = access_key

    def to_csv(self, df: pd.DataFrame, filename: str, **kwargs) -> None:
        """
        Converts df to csv and upload to storage.

        Args:
            df (pd.DataFrame): dataframe to be saved on storage as csv
            filename (str): filename. Extension must be included
            kwargs: keyword arguments related to pandas.DataFrame.to_csv() method
        """
        client = BlobClient(
            self._storage_url,
            self._container_name,
            blob_name=filename,
            credential=self._access_key,
        )
        csv = df.to_csv(**kwargs)
        client.upload_blob(csv)
        return

    def read_csv(self, filename: str, **kwargs) -> pd.DataFrame:

        client = BlobClient(
            self._storage_url,
            self._container_name,
            blob_name=filename,
            credential=self._access_key,
        )
        csv = client.download_blob()
        return pd.read_csv(csv, **kwargs)

    def upload_file(
        self, filename: str, target_filename: str | None = None, overwrite: bool = False
    ) -> None:
        """
        Uploads a every kind of file to Azure Blob Storage

        Args:
            filename (str): local path with filename to the file
            target_filename (str | None, optional): target filename on Azure Blob Storage.
                Can include folder structure. If not provided, local filename is used as target filename.
                Defaults to None.
        """

        client = BlobClient(
            self._storage_url,
            self._container_name,
            blob_name=target_filename if target_filename is not None else filename,
            credential=self._access_key,
        )

        with open(filename, "rb") as file:
            client.upload_blob(file, overwrite=overwrite)

    def download_file(self, filename: str, output_filename: str) -> None:
        """
        Download any kind of file from blob. Saves the file locally.

        Args:
            filename (str): target filename to be downloaded (with full specification of nested folders from container)
            output_filename (str): where to save the downloaded file
        """

        client = BlobClient(
            self._storage_url,
            self._container_name,
            blob_name=filename,
            credential=self._access_key,
        )

        with open(output_filename, "wb") as file:
            file.write(client.download_blob().readall())

    def contains(
        self,
        filename: str,
    ) -> bool:
        """
        Checks whether a file is contained in the blob

        Args:
            filename (str): target filename to be checked (with full specification of nested folders from container)

        Returns:
            bool: True id the filename is present on the blob
        """

        client = ContainerClient(
            self._storage_url,
            self._container_name,
            credential=self._access_key,
        )
        return True if filename in [i["name"] for i in client.list_blobs()] else False
