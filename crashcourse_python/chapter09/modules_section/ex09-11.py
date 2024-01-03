# ex 9-11
# save classes User, Privileges and Admin in a separate module 
# import those classes 

from users_module import User, Privileges, Admin

admin1 = Admin("Maxi", "Muster", "vip_admin")
admin1.privileges.add_privileges(["can add post", "can delete post", "can ban user"])
admin1.privileges.show_privileges()