import argparse
import json
import os

from pyarrow.parquet import write_table

from benchmark import run_benchmark

parser = argparse.ArgumentParser(description='Benchmark S3 parquet reading in Python')
subparsers = parser.add_subparsers()

URSA_LABS_BUCKET = 'ursa-labs-taxi-data'


def run_cmd(cmd: str):
    print(cmd)
    result = os.system(cmd)
    assert result == 0


def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False


def get_custom_bucket(region: str) -> str:
    print('Setting up S3 bucket...')
    import boto3
    account_id = boto3.client('sts').get_caller_identity().get('Account')
    default_name = f's3-parquet-test-{account_id}'

    bucket_name = input(f'Bucket name (default: {default_name}): ') or default_name
    if not yes_or_no(f"Create bucket {bucket_name}?"):
        print('Cancelling')
        return URSA_LABS_BUCKET

    cmd = (f'aws --region {region} cloudformation deploy '
           '--stack-name S3ParquetTest --template-file bucket.yml '
           f'--parameter-overrides BucketName={bucket_name} '
           '--no-fail-on-empty-changeset')
    run_cmd(cmd)

    print('Uploading parquet files...')
    run_cmd(f'aws s3 sync ./data/2018/ s3://{bucket_name}/2018/')

    return bucket_name


def init(args):
    print('Downloading parquet files...')
    run_cmd(f'aws s3 sync s3://{URSA_LABS_BUCKET}/2018/ ./data/2018/')

    # Ask for region (show your default)
    print('Which AWS region should you use? Using a nearby one provides better performance.')
    print('If you choose us-east-2, you can use Ursa Lab\'s bucket. Otherwise we will create your own bucket.')
    default_region = 'us-east-2'
    region = input(f'Region (default: {default_region}): ') or default_region

    # if us-east-2 use ursa-labs bucket
    if region == default_region:
        bucket_name = URSA_LABS_BUCKET
    else:
        bucket_name = get_custom_bucket(region)

    with open('settings.json', 'w') as f:
        json.dump({'bucket_name': bucket_name}, f)
    
    print('Done.')

parser_init = subparsers.add_parser('init')
parser_init.set_defaults(func=init)


def run(args):
    print('Running benchmark...')
    with open('settings.json', 'r') as f:
        settings = json.load(f)
    
    results = run_benchmark(
        files=[1],
        columns=[1, 4, None],
        bucket=settings['bucket_name'],
    )

    write_table(results, 'results.parquet')
    print('Done.')

parser_run = subparsers.add_parser('run')
parser_run.set_defaults(func=run)


def cleanup(args):
    with open('settings.json', 'r') as f:
        settings = json.load(f)
    
    if settings['bucket_name'] != URSA_LABS_BUCKET:
        print('Blowing away S3 bucket...')
        cmd = 'aws cloudformation delete-stack --stack-name S3ParquetTest'
        run_cmd(cmd)
    
    os.rmdir('data')
    os.remove('settings.json')
    print('Done.')

parser_cleanup = subparsers.add_parser('cleanup')
parser_cleanup.set_defaults(func=cleanup)


args = parser.parse_args()
args.func(args)