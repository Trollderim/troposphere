# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, PropsDictType, Tags


class Hypervisor(AWSObject):
    """
    `Hypervisor <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backupgateway-hypervisor.html>`__
    """

    resource_type = "AWS::BackupGateway::Hypervisor"

    props: PropsDictType = {
        "Host": (str, False),
        "KmsKeyArn": (str, False),
        "LogGroupArn": (str, False),
        "Name": (str, False),
        "Password": (str, False),
        "Tags": (Tags, False),
        "Username": (str, False),
    }
