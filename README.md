# ansible-ec2

A collection of commands to simplify common tasks built on top of Ansible and the EC2 external inventory plugin.

## Examples

    # Tell me what the heck the 'info' command does
    ansible-ec2 help info

    # SSH into the EC2 instance with the Name tag 'Web1'
    ansible-ec2 ssh --name Web1
    
    # List all instances in the us-east-1a availability zone
    ansible-ec2 list --zone us-east-1a
    
    # Give me detailed information about all m1.xlarge instances in the 'database' security group 
    ansible-ec2 info --type m1.xlarge --sg database
    
## Setup and Installation

1. Set up Ansible

   http://ansible.cc/docs/gettingstarted.html
   
1. Configure the EC2 inventory plugin
   
    cp ansible/plugins/inventory/ec2.py /etc/ansible/hosts
    cp ansible/plugins/inventory/ec2.ini /etc/ansible/ec2.ini
    cat > ~/.boto <<EOF
    [Credentials]
    aws_access_key_id = AKIA123
    aws_secret_access_key = SeCrEt123
    EOF
   
1. Put `ansible-ec2` on your path somewhere

Now you can run through the examples above or simply list all instance

    ansible-ec2 list
    


