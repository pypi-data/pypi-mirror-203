import numpy as np

def find_similarity(arr1, arr2, min_value = 1, max_value = 6):
  """
  Calculates the similarity in the frequency of occurance of different elements in two arrays.
  Both the arrays should be of same size and should contain discrete numbers.

  Parameters:
  arr1 (np.ndarray): First numpy array.
  arr2 (np.ndarray): Second numpy array.
  min_value (int): Minimum discrete value whose frequency we are interested in.
  max_value (int): Maximum discrete value whose frequency we are interested in.

  Returns:
  float: A similarity index between two arrays.
  
  >>> arr1 = np.array([[1,2,3,4],[1,2,4,5]])
  >>> arr2 = np.array([[2,2,3,4],[1,2,5,5]])
  >>> find_similarity(arr1, arr2, max_value = 5)
  0.75
  """
  arcount1 = np.bincount(arr1.ravel(), minlength = max_value + 1)[min_value:max_value + 1]
  arcount2 = np.bincount(arr2.ravel(), minlength = max_value + 1)[min_value:max_value + 1]
  diff = arcount1 - arcount2
  #return  1 - np.sqrt(np.sum(diff**2))/arr1.size
  #if not np.sum(arcount1) == 0:
  #  ans = 1 - np.sum(np.abs(diff))/(2*np.sum(arcount1))
  #else:
  #  ans = 0
  #return ans
  return 1 - np.sum(np.abs(diff))/(2*np.sum(arcount1))

def calculate_similarity(array1, array2, f = 9, s = None, skipval = 0):
  """
  Calculates the degree of similarity between two categorical arrays within the
  given neighborhood filter size.
  Minimum similarity is 0, if two arrays don't contain any common values
  Maximum similarity is 1, if the count for each distict value in array 1
  is same as the count for that value in array 2.

  Parameters:
  array1 (numpy.ndarray): First input array.
  array2 (numpy.ndarray): Second input array.
  f (int): The size of neighborhood filter, preferably an odd number,
          where a similar value will be searched.
  s (int): The stride value to move the filter,
          preferably the same as the filter size f.

  Returns:
  float: Normalized similarity score that show 
  """
  assert array1.shape == array2.shape, "The arrays must be same size."
  
  # if filter size of 1 is provided, it will return the similarity based on 
  # pixel to pixel match
  if f == 1:
    return np.mean(array1 == array2)
  
  # if stride is not provided, set it equal to filter size
  if s is None:
    s = f

  n, m = array1.shape
  similarity = 0
  subtract = 0
  # Find the number of subsets in row and column directions
  n_, m_ = len(range(0, n - f + 1, s)), len(range(0, m - f + 1, s))
  
  min_value = min(np.min(array1), np.min(array2))
  min_value = min_value if min_value !=0 else 1
  max_value = max(np.max(array1), np.max(array2))
  
  # Subset both arrays to the filter size and successively calculate similarity for all subsets
  for i in range(0, n - f + 1, s):
    for j in range(0, m - f + 1, s):
      arr1 = array1[i:i+f, j:j+f]
      arr2 = array2[i:i+f, j:j+f]
      if np.all(arr1 == skipval):
        subtract += 1
        continue

      # Find similarity between the two subsets
      sim = find_similarity(arr1, arr2, min_value, max_value)

      similarity += sim

  return similarity/(n_ * m_ - subtract)
  #return similarity/np.sum(array2 > 0)

def find_multiresolution_similarity(array1, array2, min_size = 1, max_size = None, steps = None):
  """
  Finds similarity between two arrays at multiple resolutions.
  
  Parameters:
  array1 (numpy.ndarray): First input array of dimension 2.
  array2 (numpy.ndarray): Second input array of dimension 2.
  min_size (int) : The minimum filter size to find similarity at.
  max_size (int): The maximum filter size to find similarity at.
  steps (int): The steps size to increase the filter size in each iteration.

  Returns:
  Tuple: A tuple containing a list of filter sizes and
        a list of corresponing similarity indices.
  
  >>> array1 = gdal.Open("path/to/imag1.tif").ReadAsArray()
  >>> array2 = gdal.Open("path/to/image2.tif").ReadAsArray()
  >>> find_multiresolution_similarity(array1, array2)

  """
  assert array1.ndim == 2
  assert array1.shape == array2.shape, "The arrays must be same size."
  if max_size is None:
    max_size = np.min(array1.shape)

  if steps is None:
    steps = (max_size - min_size)//10

  # Run similarity calculation for multiple filter sizes.
  filters = []
  similarities = []
  for i in range(min_size, max_size + 1, steps):
    print(i)
    try: 
      similarity = calculate_similarity(array1, array2, f = i)
      filters.append(i)
      similarities.append(similarity)
    except: 
      continue
  return (filters, similarities)
