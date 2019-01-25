"""
implementation of a basic binary serach
time complexity : O(log N)
"""

def binarySearch(search_list, search_element):
  if len(search_list)==0:
    return False
  else:
    mid_point = len(search_list)//2
    if search_list[mid_point]==search_element:
      return True
    elif search_list[mid_point] > search_element:
      return binarySearch(search_list[:mid_point],search_element)
    else:
      return binarySearch(search_list[mid_point+1:], search_element)

# if __name__ == "__main__":
#   print("Element found in search :",binarySearch([10,3,7,9,12,6,8], 6))