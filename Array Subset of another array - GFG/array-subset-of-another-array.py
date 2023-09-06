#User function Template for python3
def isSubset( a1, a2, n, m):
    s1 = set(a1)
    s2 = set(a2)

    if all(a1.count(x) >= a2.count(x) for x in s2):
        return "Yes"
    return "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends