import os,  time



while True:
    sync_command = f"aws s3 sync s3://covid-hackathongtemory videos/ "
    os.system(sync_command)
    print("Check")
    time.sleep(15)

    # s3 = boto3.client('s3', aws_access_key_id='AKIAJRFOLRO6MACCCL6A', aws_secret_access_key='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')
