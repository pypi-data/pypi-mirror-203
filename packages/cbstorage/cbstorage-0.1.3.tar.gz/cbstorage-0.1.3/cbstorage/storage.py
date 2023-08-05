import boto3
import pathlib
import os
import io
import re
import glob


class Storage:
    pass


class Aws(Storage):
    """
            A class for managing local file cbstorage.
    """

    def list_files(self, bucket_name):
        """
            Return a list of all files in the given S3 bucket.
        """
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        return [file.key for file in bucket.objects.all()]

    def grep(self, file_list, pattern):
        """
            Return a list of files that match the given pattern.
        """
        return [file for file in file_list if re.search(pattern, file)]

    def get_difference_dates(self, s3_files, date_files):
        """
            Return a list of files that are in date_files but not in s3_files.
        """
        s3_files = [line.split('/')[-1].split('.')[0] for line in s3_files]
        other = list(set(date_files) - set(s3_files))
        return other

    def store_to_s3(self, df, filename, bucket_name):
        """
            Store the given DataFrame to S3 as a compressed Parquet file.
        """
        buffer = io.BytesIO()
        df.to_parquet(buffer, compression='gzip')
        s3_resource = boto3.resource('s3')
        s3_resource.Object(bucket_name, filename).put(Body=buffer.getvalue())

    def store_csv_s3(self, response, filename, bucket_name):
        """
            Store the given HTTP response as a CSV file in S3.
        """
        buffer = io.BytesIO()
        buffer.write(response.content)
        s3_resource = boto3.resource('s3')
        s3_resource.Object(bucket_name, filename).put(Body=buffer.getvalue())

    def store_json_s3(self, response, filename, bucket_name):
        """
            Store the given JSON response as a JSON file in S3.
        """
        buffer = io.StringIO()
        buffer.write(response)
        s3_resource = boto3.resource('s3')
        s3_resource.Object(bucket_name, filename).put(Body=buffer.getvalue())

    def store_buffer_s3(self, buffer, filename, bucket_name):
        """
            Store the given buffer as a file in S3.
        """
        s3_resource = boto3.resource('s3')
        s3_resource.Object(bucket_name, filename).put(Body=buffer.getvalue())

    def get_file(self, filename, bucket_name):
        """
            Return the contents of the given file in S3 as a bytes buffer.
        """

        buffer = io.BytesIO()
        s3 = boto3.client('s3')

        s3.download_fileobj(bucket_name, filename, buffer)
        buffer.seek(0)
        return buffer


class Local(Storage):
    """
        A class for managing local file cbstorage.
    """

    def __init__(self):
        self.basedir = '/data/notebooks/Lev2/backupS3/'

    def searching_all_files(self, directory):
        """
            Return a sorted list of full paths to all files in the given directory and its subdirectories.
        """
        dirpath = pathlib.Path(directory)
        assert dirpath.is_dir()
        file_list = []
        for x in dirpath.iterdir():
            if x.is_file():
                file_list.append(x.as_posix())
            elif x.is_dir():
                file_list.extend(self.searching_all_files(x))
        return sorted(file_list)

    def list_files(self, bucket):
        """
            Returns a list of file paths in the specified bucket directory.
        """
        bucket_dir = os.path.join(self.basedir, bucket)
        return self.searching_all_files(bucket_dir)

    def grep(self, list_files, pattern):
        """
            Returns a list of file paths that match the specified pattern.
        """
        pattern_dir = os.path.join(list_files, pattern)
        return glob.glob(os.path.join(pattern_dir, '*'))

    def get_difference_dates(self, files_s3, files_dates):
        """
            Returns a list of files in `files_dates` that are not in `files_s3`
        """
        files_s3 = [os.path.basename(line).split('.')[0] for line in files_s3]
        other = list(set(files_dates) - set(files_s3))
        return other

    def store_to_s3(self, df, filename, bucket):
        """
            Stores a pandas DataFrame to a Parquet file in the specified bucket directory.
        """
        path = pathlib.Path(f'{self.basedir}{bucket}/{filename}')
        self.create_folder_not_exists(path)
        df.to_parquet(path.as_posix(), compression='gzip')

    def store_csv_s3(self, response, filename, bucket):
        """
            Stores a CSV file from an HTTP response to the specified bucket directory.
        """
        path = pathlib.Path(f'{self.basedir}{bucket}/{filename}')
        self.create_folder_not_exists(path)
        open(path.as_posix(), "wb").write(response.content)

    def store_json_s3(self, response, filename, bucket):
        """
            Stores a JSON file from an HTTP response to the specified bucket directory.
        """
        path = pathlib.Path(f'{self.basedir}{bucket}/{filename}')
        self.create_folder_not_exists(path)
        open(path.as_posix(), "w").write(response)

    def store_buffer_s3(self, buffer, filename, bucket):
        """
            Stores a binary buffer to the specified bucket directory.
        """
        path = pathlib.Path(f'{self.basedir}{bucket}/{filename}')
        self.create_folder_not_exists(path)
        open(path.as_posix(), "wb").write(buffer.getvalue())

    def get_file(self, filename, bucket):
        """
            Returns a binary buffer of the specified file from the specified bucket directory.
        """
        path = f'{self.basedir}{bucket}/{filename}'
        buffer = io.BytesIO()
        buffer.write(open(path, 'rb').read())
        buffer.seek(0)
        return buffer

    def open_file(self, filename, bucket, mode="wb", **kwargs):
        """
            Opens the specified file in the specified bucket directory in the specified mode.
        """
        path = pathlib.Path(f'{self.basedir}{bucket}/{filename}')
        self.create_folder_not_exists(path)
        f = open(path.as_posix(), mode, **kwargs)
        return f

    def create_folder_not_exists(self, path):
        """
            Creates the parent directory of a file path if it does not already exist.
        """
        parent = path.parent
        if not parent.exists():
            print("Create folder:", parent)
            parent.mkdir(parents=True, exist_ok=True)

    def get_difference_files(self, files_s3, files_dates):
        """
            Returns a list of files in `files_dates` that are not in `files_s3`.
        """
        files_s3 = [os.path.basename(line) for line in files_s3]
        files_dates = [os.path.basename(line) for line in files_dates]
        other = list(set(files_dates) - set(files_s3))
        print(other)
        return other

    def file_exists(self, file, bucket):
        """
            Checks if the given file exists in the specified bucket.
        """
        return pathlib.Path(f"{self.basedir}{bucket}/{file}").exists()

    def find_file(self, file, files):
        """
            Searches for the given file in the list of files.
        """
        full_path = f"{self.basedir}{file}"
        if full_path in files:
            return file
        else:
            return False

    def grep_files(self, pattern, bucket):
        """
            Gets a list of files in the specified bucket that match the given pattern.
        """
        t = f"{self.basedir}{bucket}/{pattern}"
        return glob.glob(t)