class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    # invalid user check
    if (isinstance(user, str) is False or user == ""):
        return "Please enter a valid user"
    # invalid group check
    elif (isinstance(group, Group) is False):
        return "Please enter a valid group"

    else:
        # group that isn't a Group entered
        sub_groups = group.get_groups()
        users = group.get_users()

        if (user in users):
            return True
        for grp in sub_groups:
            if (is_user_in_group(user, grp)):
                return True
            
        return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("sub_child_user", parent)) # returns True
print(is_user_in_group("sub_child_user", child)) # returns True
print(is_user_in_group("sub_child_user_1", parent)) # returns False

# edge cases - invalid group
print(is_user_in_group("sub_child_user_1", "")) # returns Please enter a valid gorup

# edge case - invalid user
print(is_user_in_group("", parent)) # returns Please enter a valid user

# edge case - None for both
print(is_user_in_group(None, None)) # returns Please enter a valid user


