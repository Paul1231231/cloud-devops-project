output "vpc_id" {
  value = data.aws_vpc.default.id
}

output "alb_security_group_id" {
  value = aws_security_group.alb.id
}

output "api_security_group_id" {
  value = aws_security_group.api.id
}

output "db_security_group_id" {
  value = aws_security_group.db.id
}

output "ecs_cluster_name" {
  value = aws_ecs_cluster.main.name
}
