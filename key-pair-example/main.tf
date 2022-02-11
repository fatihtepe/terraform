provider "aws" {
  profile = "default"
  region = "us-east-1"
}

resource "aws_key_pair" "terraform_key_pair" {
  key_name = "ec2_key_pair"
  public_key = file("keys/terraform-key-pair.pub")
}

resource "aws_instance" "ec2-with-key-pair" {
  ami = "ami-038b3df3312ddf25d"
  instance_type = "t2.micro"
  key_name = "${aws_key_pair.terraform_key_pair.key_name}"
}
