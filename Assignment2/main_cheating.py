# import copy
# weakref
import re
import sys

def default_gt(node_a, node_b):
    """Not to be used outside lnk_list insert_sort but the users may 
    code another one to substitute it if needed, so it's outside the 
    class. Defines how two lnk_nodes should be compared, returning 1 if
    node_a is greater or equal to b and 0 otherwise"""
    if not node_a:
        return 0
    if not node_b:
        return 1
    if node_a.value >= node_b.value: # While not used in the task I 
        return 1                     # considered it the most logic
    else:                            # default
        return 0
        


def gt_by_chom_arm_cheating(node_a, node_b):
    """Not to be used outside lnk_list insert_sort.
    Defines how two lnk_nodes should be compared, returning 1 if
    node_a is greater or equal to b and 0 otherwise using chromosome 
    arm as first discriminant if read_sec_locations_cheating used"""
    if not node_a:
        return 0
    if not node_b:
        return 1
    if node_a.loci>=node_b.loci:
        return 1
    else:
        return 0
       
def gt_by_chom_alone(node_a, node_b):
    """Not to be used outside lnk_list insert_sort.
    Defines how two lnk_nodes should be compared, Suposing loci already
    contains only the chromosome arm information."""
    if not node_a:
        return 0
    if not node_b:
        return 1
    if (int(node_a.loci[:-1]),node_a.loci[-1])>= (int(node_b.loci[:-1]),
    node_b.loci[-1]):
        return 1                     # considered it the most logic
    else:                            # default
        return 0
    
class lnk_list:
    def __init__(self, loci, val, n=False):
        self.root = lnk_node(loci,val)
        self.current = self.root
        self.last = self.root
    
    def start(self):
        """Resets the cursor current back to the root"""
        self.current = self.root
    
    def next(self):
        """Advance one position, returns 0 if already at the end and 1 
        otherwise"""
        n = self.current.n
        self.current = n
        if n!=False:
            return 1
        else:
            return 0
    
    def new_node(self,loci,val):
        """ Creates a new node at the end of the list"""
        self.last.insert(lnk_node(loci,val))
        self.last = self.last.n
    
    def insert(self, new_node):
        """Inserts a single node at the current position"""
        self.current.insert(new_node)
        
    def __add__(self, b):
        """Add the content of a second lnk_list after the own """
        if type(self)!=type(b):
            raise NameError('lnk_list can only be added to ln_list')
        else:
            self.last.n = b.root
            self.last = b.last  
    
    def insert_sort(self, gt_function = default_gt):
        """ Sorts the lnk_list using insertion sort"""
        sorted_list = lnk_list(self.root.loci, self.root.value)
        to_rmv = self.root
        self.root = self.root.n
        del(to_rmv) # giben that del just remove the reference to let
                    # the garbage collector to actuate creating to_rmv
                    # was not really needed but useful to be explicid.
        while self.root:
            to_add = self.root
            self.root = to_add.n
            sorted_list.current = sorted_list.root
            if gt_function(sorted_list.root, to_add):
                to_add.n = sorted_list.root
                sorted_list.root = to_add
                #print(to_add.loci)
                continue
            while not gt_function(sorted_list.current.n, to_add) and sorted_list.current.n:
                sorted_list.next()
            sorted_list.insert(to_add)
        self.root = sorted_list.root
                
    def __str__(self):
        cur = self.root
        ret = ""
        while cur:
            ret+="[loci: "+str(cur.loci)+", value: "+str(cur.value)+"] -> "
            cur = cur.n
        return ret
         

class lnk_node:
    def __init__(self, loci, val, n=False):
        self.loci = loci
        #self.chrom = int(loci.split(".").strip(" \nq")
        self.value = val
        self.n = n
        
    def next(self):
        return self.n
    
    def insert(self, new_node):
        new_node.n = self.n
        self.n = new_node
        #print ("inserting", new_node.loci, new_node.value)
        


def read_sec_locations_cheating(file_name):
    """Reads a file with sequence id, chromosomal location and geometric
    locations separated by taps and produces a lnk_list with the 
    relevant information stores chromosome arm and geometeical 
    coordinates sum instead of loci"""
    with open(file_name) as fh:
        fi=1
        for line in fh:
            loci = line.split("\t")[1]
            location = ( tuple(float(x) 
                for x in re.split('\\(|,|\\)',line)[1:3]))
            ident = (int(re.split('p|q',loci)[0]),
    re.search('p|q',loci)[0], sum(location))

            if fi:
                to_return = lnk_list(ident,location)
                fi=0
            else:
                to_return.new_node(ident,location)
        
    return(to_return)    

def count_close_reads_cheating(sorted_lnk_list, threshold):
    """This function assumes it is giben a lnk_list sorted using 
    gt_by_chom_arm as discriminant criteria and counts how many reads
    on the same chromosom arm are closer than threshold.
    Theorical basis for loop breaking:
    gt_by_chom_arm sorts by chromosome arm but also by the sum of the
    coordinates having the sum of the coordinates we know a point falls 
    in the line x + y = n and the mininum distance between two lines
    like those is equal to min_dist([0,n1], line2)= |n1-n2|/sqrt(2)"""
    max_diference_coord_sum = threshold * 1.5 # I use 1.5 as sqrt(2) to
    # avoid decimal errors in reality would be 1.4142135623730951
    max_distance_squared = threshold**2
    node1 = sorted_lnk_list.root
    chrom1 = str(node1.loci[0])+node1.loci[1]
    count_result = lnk_list(chrom1, 0)
    
    while node1.n:
        node2 = node1.n
        chrom2 = str(node2.loci[0])+node2.loci[1]
        dif = 0
        while node2 and chrom1==chrom2 and dif < max_diference_coord_sum:
            if ((node1.value[0]-node2.value[0])**2+(node1.value[1]
            -node2.value[1])**2) <= max_distance_squared:
                count_result.last.value+=1
            dif = sum(node1.value)- sum(node2.value)
            dif = max(dif,-dif)
            node2 = node2.n
            if not node2:
                break
            chrom2 = str(node2.loci[0])+node2.loci[1]
        node1 = node1.n
        chrom1 = str(node1.loci[0])+node1.loci[1]
        # There are repetitive pices of code but otherwise to know the
        # chromosome arm without lossing loci information would require
        # some kind of aditional data structure
        if chrom1 != count_result.last.loci:
            count_result.new_node(chrom1,0)
    return(count_result)
            
    

if __name__=="__main__":
    our_data = read_sec_locations_cheating(sys.argv[1])
    our_data.start()
    our_data.insert_sort(gt_by_chom_arm_cheating)
    counts = count_close_reads_cheating(our_data, float(sys.argv[2]))
    counts.insert_sort(gt_by_chom_alone) 
    print(counts)
