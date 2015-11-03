from newarray import Array
from arrayMultiArray import MultiArray

# store all data into multi array
def storeDataIntoArray():
    saleFile = open("salesData.txt")
    numOfStore = int(saleFile.readline().strip())
    numOfItem = int(saleFile.readline().strip())
    numOfMonth = 12
    
    salesData = MultiArray(numOfStore, numOfItem, numOfMonth)
    salesData.clear(0)
    
    for line in saleFile:
        lines = line.split()
        
        idOfStore = int(lines[0]) - 1
        idOfMonth = int(lines[1]) - 1
        idOfItem = int(lines[2]) - 1
        amountOfSales = float(lines[3])
    
        salesData[idOfStore, idOfItem, idOfMonth] = amountOfSales
    
    saleFile.close() 
    
    for store in range(numOfStore):
        for item in range(numOfItem):
            for month in range(numOfMonth):
                if salesData[store, item, month] != 0:
                    print salesData[store, item, month],store+1,month+1,item+1
                    
    return salesData

# Compute the total sales of all items for all months in a given store
def totalSalesByStore(salesData, store):
    # Subtract 1 from the store # since the array indices are 1 less 
    # than the given store 
    s = store - 1
    # Accumulate the total sales for the given store
    total = 0.0

    # Iterate over item
    for i in range(salesData.length(2)):
        # Iterate over each month of the i item
        for m in range(salesData.length(3)):
            total += salesData[s, i, m]

    return total

# Compute the total sales of all items in all stores for a given month
def totalSalesByMonth(salesData, month):
    # The monmth number must be offset by 1
    m = month - 1
    # Accumulate the total sales for the given month
    total = 0.0

    # Iterate over each store
    for s in range(salesData.length(1)):
        # Iterate over each item of the s store
        for i in range(salesData.length(2)):
            total += salesData[s, i, m]

    return total

# Compute the total sales of a single item in 
# all stores over all months
def totalSalesByItem(salesData, item):
    # The item number must be offset by 1
    i = item - 1

    # Accumulate the total sales for the given month
    total = 0.0

    # Iterate over each store
    for s in range(salesData.length(1)):
        # Iterate over each month of the s store
        for m in range(salesData.length(3)):
            total += salesData[s, i, m]

    return total

# Compute the total sales per month for a given store 
# A 1D array is returned that contains the totals for each month
def totalSalesPerMonth(salesData, store):
    # The store number must be offset by 1
    s = store - 1

    # The totals will be returned in a 1D array
    totals = Array(12)

    # Iterate over the sales of each month
    for m in range(salesData.length(3)):
        sum_ = 0.0

        # Iterate over the sales of each item sold during the m month
        for i in range(salesData.length(2)):
            sum_ += salesData[s, i, m]

        # Store the result in the corresponding month of the totals array
        totals[m] = sum_

    # Return the 1D array
    return totals

if __name__ == "__main__":    
    salesDate = storeDataIntoArray()