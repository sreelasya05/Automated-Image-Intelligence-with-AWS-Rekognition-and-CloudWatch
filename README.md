# Automated-Image-Intelligence-with-AWS-Rekognition-and-CloudWatch

This project demonstrates how to build an image labeling pipeline using **AWS Rekognition**, **AWS Lambda**, and **Amazon S3**. It automatically detects objects, scenes, and concepts in images uploaded to an S3 bucket and logs the results using CloudWatch.

---

## Features

- Upload any image to the S3 bucket.
- Lambda function is triggered on image upload.
- AWS Rekognition scans the image for labels.
- Logs are stored and viewable in AWS CloudWatch.

---

## Technologies Used

- **AWS S3** - Stores the uploaded images.
- **AWS Lambda** - Executes Python code automatically on S3 events.
- **AWS Rekognition** - Detects labels in the images.
- **IAM** - Controls access between services.
- **CloudWatch** - Stores and monitors Lambda logs.

---

## Flow Diagram

1. **Upload image to S3**
2. **S3 triggers Lambda**
3. **Lambda calls Rekognition**
4. **Labels are logged to CloudWatch**

---

## Sample Outputs (From CloudWatch)

```text
Image: catanddog.jpg
Labels: ['Animal', 'Canine', 'Dog', 'Mammal', 'Pet', 'Hound', 'Cat', 'Puppy', 'Snout']

Image: flower.jpg
Labels: ['Flower', 'Plant', 'Rose']
