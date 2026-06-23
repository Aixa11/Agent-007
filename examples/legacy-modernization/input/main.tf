terraform {
  required_version = ">= 1.5.0"
}

provider "aws" {
  region = var.region
}

variable "region" {
  type    = string
  default = "us-east-1"
}

resource "aws_instance" "legacy_app" {
  ami           = "ami-1234567890abcdef0"
  instance_type = "t3.small"

  tags = {
    Name    = "legacy-app"
    Service = "core-platform"
  }
}
