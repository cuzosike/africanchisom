py
import boto3
ecc = boto3.client('ec2')
ins = ecc.describe_instances()
ins2 = ins.__str__()
ins3 = ins2.split()

for x in ins3:
    if 'i-' in x:
        print(x)
        
       
        
        
ecc.start_instances(InstanceIds=[])
#In the brackets above, paste an Instance ID (use quote marks)


