"""
https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pearson/04GreedyAlgorithms-2x2.pdf
"""

#TODO: sort jobs beforehand -> O(nlogn)

def compatibles(end, requests):
    compatibles = []
    for job in requests:
        if job[0] >= end:
            compatibles.append(job)
    return compatibles
    

def earliest_finish(requests):
    min_finish_job = requests[0];
    for job in requests:
        if job[1] < min_finish_job[1]:
            min_finish_job = job
    return min_finish_job

def interval_scheduling_greedy(requests):
    """ Greedy implementation of interval scheduling
        Returns subset of requests with maximum number of jobs
        time: O(n^2)
        space: O()
    """
    optimal_subset = []

    while (len(requests)>0):
        job = earliest_finish(requests)
        compatible_list = compatibles(job[1], requests)
        optimal_subset.append(job)
        requests = compatible_list
    return optimal_subset


        

        
