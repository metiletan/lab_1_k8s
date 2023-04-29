resource "aws_iam_role" "control_plane_role" {
  name               = "control_plane_role"
  assume_role_policy = data.aws_iam_policy_document.control_plane_role_assume_policy.json
}


# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Allow",
#             "Principal": {
#                 "Service": "eks.amazonaws.com"
#             },
#             "Action": "sts:AssumeRole"
#         }
#     ]
# }

data "aws_iam_policy_document" "control_plane_role_assume_policy" {
  statement {
    sid = "1"

    actions = [
      "sts:AssumeRole",
    ]
    principals {
      type        = "Service"
      identifiers = ["eks.amazonaws.com"]
    }

    effect = "Allow"

  }

} 

# arn:aws:iam::aws:policy/AmazonEKSClusterPolicy
resource "aws_iam_policy_attachment" "control_plane_role_policy_attachment" {
  name       = "control_plane_role_policy_attachment"
  roles      = [aws_iam_role.control_plane_role.name]
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
}