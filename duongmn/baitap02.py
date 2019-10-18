import numpy as np
class danhsach:
    A = np.int_((0.0, 1.1))
    #read array from file
    def __init__(self, filename):
        f = open(filename, 'r')
        #read line and strip white char at the end of line
        self.A = [float(line.rstrip('\n')) for line in f]
        f.close()

    #write array to new file
    def writeFile(self, filename):
        f = open(filename, 'w')
        for item in self.A:
            f.write("%s\n" %item)

    #find max and second-max value
    def findMax(self):
        maxElement = np.max(self.A)
        print("Gia tri lon nhat: " + str(maxElement))
        indexMax = np.where(self.A == np.amax(self.A))
        print("Index gia tri lon nhat: " + str(np.argmax(self.A)))

    #sort array in reverse
    def sortArray(self):
        self.A.sort(reverse = True)

    #insert value to sorted array
    def insertArray(self, n):
        #find position to insert
        for i in range(len(self.A)):
            if self.A[i]  < float(n):
                index = i
                break
        #insert value to sorted array
        self.A = self.A[:i] + [float(n)] + self.A[i:]

    #delete element from array
    def deleteArray(self,n):
        #find if n in Array
        if float(n) in self.A:
            #if n in array, remove all element has same value with n
            while float(n) in self.A:
                self.A.remove(float(n))
        else:
            print("Khong ton tai gia tri can xoa trong mang")

def main():
    p1 = danhsach("input.txt")
    p1.findMax()
    p1.sortArray()
    p1.insertArray("13.1")
    p1.deleteArray(3)
    print(p1.A)
    p1.writeFile("output.txt")


if __name__ == '__main__':
    main()
