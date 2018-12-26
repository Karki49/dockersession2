

import boto3

batch = boto3.client('batch')

def submitDemoJobs():
    for name in []:

        containerOverrides = {
            'environment':[
                {
                }
            ]
        }

        # customerName
        batch.submit_job(jobName="", jobQueue="",
                         jobDefinition="", containerOverrides="")

if __name__=='__main__':
    submitDemoJobs()
