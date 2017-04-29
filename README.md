# neural-net-image-processing
AWS Lambda function for Neural Network Image processing

Added Necessary files from:
  PIL, Scipy, and Numpy

AWS Lambda needs these dependencies to be packaged along with the Lambda function in order to execute it.

What this function sets up on AWS:
  1. Sets up AWS endpoint (using AWS API Gateway)
  2. Connects the AWS Lambda function to that endpoint to process data recieved through "params"
  
What the function does:
  1. Takes as an input-param a web-url link of an image
  2. Converts that images pixel values into grayscale and formats it into a single array of 784 pixel values

Why I created it:
  1. I wanted to create an application that uses a Neural Network to convert a handwritten digit into its numerical counterpart
  2. The neural network I created is trained on 60,000 images that are in a 28x28 (784) pixel format and needs input data to be consistent with that
  
How to use it:
  1. Install serverless (a tool for packaging aws functions)
  2. Run "serverless create -t aws-python"
  3. Run "serverless deploy"
  4. Send request to endpoint in form: AWS_ENDPOINT?urlLink=WEB_URLLINK
  5. Response is an array of 784 pixel values
