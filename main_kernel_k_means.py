import sys
from LoadData import * 
from k_means import * 
from evaluation import * 
from kernel_k_means import * 

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "[usage] <data-file> <ground-truth-file>"
        exit(1) 
    
    dataFilename = sys.argv[1]
    groundtruthFilename = sys.argv[2]
    
    data = loadPoints(dataFilename) 
    groundtruth = loadClusters(groundtruthFilename) 

    sigma = 4.0
    
    data = kernel(data, sigma)  

    nDim = len(data[0]) 
   
    K = 2  # Suppose there are 2 clusters 
    
    centers = []
    centers.append(data[0])
    centers.append(data[1]) 
    
    results = kmeans(data, centers) 

    res_Purity = purity(results, groundtruth) 
    res_NMI = NMI(results, groundtruth) 
    
    print "Purity =", res_Purity
    print "NMI = ", res_NMI
    

