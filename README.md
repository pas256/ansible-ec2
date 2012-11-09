# ansible-ec2

A collection of commands to simplify common tasks built on top of Ansible and the EC2 external inventory plugin.


## Examples

    # Tell me what the heck the 'info' command does
    ansible-ec2 help info

    # SSH into the EC2 instance with the 'Name' tag 'Web1'
    ansible-ec2 ssh --name Web1
    
    # List all instances in the us-east-1a availability zone
    ansible-ec2 list --zone us-east-1a
    
    # Give me detailed information about all m1.xlarge instances in the 'database' security group 
    ansible-ec2 info --type m1.xlarge --sg database


## Setup and Installation

1.  Set up Ansible

    http://ansible.cc/docs/gettingstarted.html
   
1.  Configure the EC2 inventory plugin
   
        cp ansible/plugins/inventory/ec2.py /etc/ansible/hosts
        cp ansible/plugins/inventory/ec2.ini /etc/ansible/ec2.ini
        cat > ~/.boto <<EOF
        [Credentials]
        aws_access_key_id = AKIA123
        aws_secret_access_key = SeCrEt123
        EOF
    
    Confirm it is working by running
  
        /etc/ansible/hosts
   
1.  Put `ansible-ec2` on your path somewhere, or change your path

        export PATH="${PATH}:/path/to/ansible-ec2/bin"

Now you can run through the [examples](#examples) above or simply list all instance

    ansible-ec2 list
    

## Commands

-   `help`
    Get help about a command
    
-   `list`
    Get a list of instances
    
-   `info`
    Get detailed information about instances
    
-   `ssh`
    Open an interactive SSH connection to a specific instance


## Filters

By default, `ansible-ec2` performs a command against all instances. This might be fine for `list`, but far from ideal for `ssh`. This is where filters become powerful, by limiting the set of instances a command runs on.

### Name

EC2 instances can have tags (simple key/value pairs) associated with them. The 'Name' tag is of particular interest as it is the first column in the [AWS Web Console](https://console.aws.amazon.com/ec2/home#s=Instances). To run only against instances with a specific value for the 'Name' tag, use:

    --name NAME
    
### Security Group

Run a command only against instances in a specific security group

    --sg SECURITY_GROUP
    
    E.g. --sg=default


### Key Pair

    --key KEY_PAIR        The name of the key pair to filter on. E.g.
                        --key=superadmin
    --type INSTANCE_TYPE  Return only host using the specific instance type.
                        E.g. --type=m1.xlarge
    --region REGION       Limit to only one region. E.g. --region=us-east-1
    --zone AVAILABILITY_ZONE
                        Limit to only one availability zone. E.g. --zone=us-
                        east-1a
    GROUP_NAME            The raw group name to filter on based on the groups
                        produced by the Inventory. This can also be the
                        Instance ID. E.g. i-abcd1234
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        