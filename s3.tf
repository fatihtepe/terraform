terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.74.1"
    }
  }
}

provider "aws" {
	region = "us-east-1"
  # Configuration options
}

resource "aws_s3_bucket" "tepe" {
  bucket = "benimbucketimfatih"
  acl    = "private"


}
