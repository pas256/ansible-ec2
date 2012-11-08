# ansible-ec2

A collection of commands to simplify common tasks built on top of Ansible and the EC2 external inventory plugin.

## Examples

    # SSH into the EC2 instance whos Name tag is Web1
    ansible-ec2 ssh --name Web1
    
    # List all instances in the us-east-1a zone
    ansible-ec2 list --zone us-east-1a
    
    # Give me detailed information about all instances in the 'database' security group
    ansible-ec2 info --sg database
    
    


    
