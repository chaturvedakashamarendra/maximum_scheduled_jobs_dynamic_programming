a1=[]
job=[]
def load_file(f):
    file=open(f,'r')
    values=file.read()
    #getting each job from file
    s=values.splitlines()
    for i in s:
        a1=[]
        s1=i.split()
        #appending start time, finish time and weight for each job
        a1.append(int(s1[0]))
        a1.append(int(s1[1]))
        a1.append(int(s1[2]))
        #job[] is the list containing each job from the file
        job.append(a1)
    return job


#calculating compatible jobs : for each job the previous compatible job with the largest index j<i is calculated
def calculate_compatibility(job):
    #initializing the compatable_jobs list with -1
    compatible_jobs=[-1]*len(job)
    #finding the compatible job with largest index j<i
    for i in range(0,len(job)):
        for j in range(i-1,-1,-1):
            #if finish time of j is <= start time of i
            if(job[j][1]<=job[i][0]):
                compatible_jobs[i]=j
                break
    return compatible_jobs

#calculating maximum weight for the jobs
def max_weight(A,p):
    #initializing computated_weight with 0
    computed_weight=[0]*len(A)
    for j in range(0,len(A)):
        #computed_weight[j]=maximum(weight of j + computed_weight[compatible_job] , previous computed_weight (computed_weight[j-1])
        computed_weight[j]=max(A[j][2]+computed_weight[p[j]],computed_weight[j-1])
    return computed_weight[len(A)-1]

files=["input1.txt","input2.txt"]
for file in files:
    #loading each job from file into job list
    job=load_file(file)
    #sorting the jobs based on finish time
    job.sort(key=lambda job:job[1])
    #calculating compatible jobs
    compatible_jobs=calculate_compatibility(job)
    #calculating maximum weight
    maximum_weight=max_weight(job,compatible_jobs)
    print("The maximum weight for",file,"is",maximum_weight)
