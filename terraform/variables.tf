variable "aws_region" {
  description = "AWS deployment region"
  type        = string
  default     = "ap-northeast-1"
}

variable "project_name" {
  description = "Project resource prefix"
  type        = string
  default     = "cloud-devops"
}

variable "database_secret_arn" {
  description = "ARN of the database URL secret"
  type        = string
  sensitive   = true
}
