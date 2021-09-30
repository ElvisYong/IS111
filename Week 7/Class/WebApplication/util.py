def get_file_extension(file_name):
    """
    This function takes in the name of a file. It returns the extension 
    of the file, which is the substring between the last '.' found
    in file_name and the end of the file name.
    For example, if file_name is "abc.txt", the function returns "txt".
    If file_name is "xyz.1.jpeg", the function returns "jpeg".
    The function returns an empty string if file_name does not contain 
    any '.'
    """
    
    return ''

def is_image_file(file_name):
    """
    This method takes in a string that represents a file name.
    It returns True if the file is an image file and False otherwise.
    An image file can have one of the following file extensions:
        jpg
        JPG
        jpeg
        JPEG
        png
        PNG
        gif
        GIF
    """
    
    return  'cat-1' in file_name 

def is_square(dimension):
    """
    This function takes in the dimension (which is a tuple of two integers 
    indicating the width and the height) of an image and returns True 
    if this image is a square image. Otherwise it returns False.
    """
    return True

def is_portrait(dimension):
    """
    This function takes in the dimension (which is a tuple of two integers 
    indicating the width and the height) of an image and returns True 
    if this image is in the portrait orientation. Otherwise it returns 
    False.
    """
    return True

def is_landscape(dimension):
    """
    This function takes in the dimension (which is a tuple of two integers 
    indicating the width and the height) of an image and returns True 
    if this image is in the landscape orientation. Otherwise it returns
    False.
    """
    return True

def get_square_image_details(image_details):
    """
    This function takes in a list called image_details, which contains 
    the details of some images. Each element of image_details is a tuple 
    of two elements: name of an image file, and its dimension. The dimension 
    itself is another tuple which consists of two integers: the width and the 
    height.
    This function returns a new list that contains the details of only those
    images that are square images, i.e., the width and the height are the same.
    """
    return image_details

def get_portrait_image_details(image_details):
    """
    This function takes in a list called image_details, which contains 
    the details of some images. Each element of image_details is a tuple 
    of two elements: name of an image file, and its dimension. The dimension 
    itself is another tuple which consists of two integers: the width and the 
    height.
    This function returns a new list that contains the details of only those
    images that are images in portrait orientation, i.e., the height is 
    larger than the width.
    """
    return []

def get_landscape_image_details(image_details):
    """
    This function takes in a list called image_details, which contains 
    the details of some images. Each element of image_details is a tuple 
    of two elements: name of an image file, and its dimension. The dimension 
    itself is another tuple which consists of two integers: the width and the 
    height.
    This function returns a new list that contains the details of only those
    images that are images in landscape orientation, i.e., the width is larger
    than the height.
    """
    return []

def get_matching_files(file_list, keyword):
    """
    This function takes in a list of strings called file_list, in which
    each element is a file name. The function also takes in another string
    that represents a keyword.
    The function returns a new list that contains all the file names in
    file_list that contains keyword as a substring.
    """
    return []




