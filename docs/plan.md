# Video Compression

### Proof of Concept 

Before diving into performing transformations and computations on a video, let's first prove that we can succesfully compress an image. 
Since a video is a series of images (or frames), we can apply our logic to compressing an image to each image in the video.

To avoid pre-mature optimization, we will start with applying SVD on an image. In the future, we should try to search for better ways of compressing videos.

#### Singular Value Decomposition

The essence: SVD provides us with three outputs that tell us how MUCH data from the matrix contributes to the matrix itself (i.e. the important data). This allows us to approximate an image by using only the important parts of it.
  
In CS506, we learned that plotting the singular values of gray scale images often show that a majority of the singular values are not needed.
When we run SVD on a gray scale image file, we get three values:
1. left singular values
2. singular values
3. right singular values (transposed)
We mainly care about singular values because they tell us the importance of data within the image


#### Psuedocode
Extract Left Unitary arrays, Singular values, Right Unitary arrays
Create a copy of singular values, svc
Define what k rank your image should be with svc[k:]
Create k rank image by multiplying left unitary arrays with the product of diagonal matrix created from svc and right unitary arrays3.
Create a diagonal matrix using the singular values from svc
Reconstruct the original matrix using SVD components


### Plan Revised (1.29.24)

After some experimenting, I found out the k-rank approximation of images doesn't change the actual size, in bytes, of the original image. 

I think utilizing SVD to get a k-rank approximation of an image is still an integral step in compressing an image, so I'll be researching for other methods that I should combine with SVD to actually reduce image size.

### Log (1.30.24)

Nevermind, I ran the code again and the compressed image is 3.1 MB, whereas the original image is 5.1 MB. We were able to achieve some degree of compression with SVD! Though I'm not sure how the compression actually works because the shape of the compressed image and original image matrices are the same. Maybe it has something to do with when the matrices are converted to images? 
