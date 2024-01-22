variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default     = "strong-arbor-411111"
}

variable "region" {
  description = "Region"
  default     = "europe-west9-a"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "demo-bucket-terraform-zoomcamp"
}

variable "gcs_storage_class" {
  description = "Bucket Stoarage Class"
  default     = "STANDART"
}

variable "location" {
  description = "Project Location"
  default     = "EU"
}